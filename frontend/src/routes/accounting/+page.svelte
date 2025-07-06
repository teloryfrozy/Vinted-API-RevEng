<script lang="ts">
    import { Mail, Trash2, MessageSquare, Printer, Star, Settings2 } from "@lucide/svelte";
    import { fetchData } from "../../global/fetchData";
    import Notification from "../../global/components/NotificationCard.svelte";
    import { onMount } from "svelte";
    import Chart from "chart.js/auto";

    let monthsToKeep = 2;
    let autoMessage = "Merci pour votre achat ! N'oubliez pas de laisser un avis 😊";

    let showNotif = false;
    let message = "";
    let type = "";
    let selectedPeriod = "last1Y";

    async function cleanConversations() {
        const result = await fetchData("POST", "accounting/clean-conversations", {
            monthsToKeep: monthsToKeep,
        });
        if (!result.success) {
            showNotif = true;
            message = result.error as string;
            type = "error";
        } else {
            showNotif = true;
            message = "Conversations nettoyées avec succès";
            type = "success";
        }
    }

    async function exportSalesData() {
        // switching btw tabs removes canvas from DOM
        // so chart.canvas is null => re-init chart with new DOM element
        if (!chart?.canvas) {
            initChart();
        }

        const result = await fetchData("POST", "accounting/export-sales-data", { period: selectedPeriod });
        if (!result.success) {
            showNotif = true;
            message = result.error as string;
            type = "error";
            return;
        }
        showNotif = true;
        message = "Données de vente exportées";
        type = "success";

        totalTurnover = result.data.total_turnover;
        maximumTurnover = result.data.maximum_turnover;
        minimumTurnover = result.data.minimum_turnover;
        averageTurnover = result.data.average_turnover;
        totalGrossProfit = result.data.total_gross_profit;
        maximumGrossProfit = result.data.maximum_gross_profit;
        minimumGrossProfit = result.data.minimum_gross_profit;
        averageGrossProfit = result.data.average_gross_profit;
        totalArticlesBought = result.data.total_articles_bought;
        averageArticleBoughtPrice = result.data.average_article_bought_price;
        averageNbArticlesBought = result.data.average_nb_articles_bought;
        mostExpensiveArticleBought = result.data.most_expensive_article_bought;
        leastExpensiveArticleBought = result.data.least_expensive_article_bought;
        totalArticlesSold = result.data.total_articles_sold;
        averageArticleSoldPrice = result.data.average_article_sold_price;
        averageNbArticlesSold = result.data.average_nb_article_sold;
        mostExpensiveArticleSold = result.data.most_expensive_article_sold;
        leastExpensiveArticleSold = result.data.least_expensive_article_sold;

        if (chart) {
            chart.data.labels = result.data.labels;
            chart.data.datasets[0].data = result.data.turnover_data;
            chart.data.datasets[1].data = result.data.gross_profit_data;
            chart.update();
            showSalesGraph = true;
        }
    }
    let showSalesGraph = false;
    let canvas: HTMLCanvasElement | null = null;
    let chart: Chart | null = null;
    let activeTab = "sales";

    let totalTurnover = 0;

    let maximumTurnover = 0;
    let minimumTurnover = 0;
    let averageTurnover = 0;
    let totalGrossProfit = 0;
    let maximumGrossProfit = 0;
    let minimumGrossProfit = 0;
    let averageGrossProfit = 0;
    let totalArticlesBought = 0;
    let averageArticleBoughtPrice = 0;
    let averageNbArticlesBought = 0;
    let mostExpensiveArticleBought = 0;
    let leastExpensiveArticleBought = 0;
    let totalArticlesSold = 0;
    let averageArticleSoldPrice = 0;
    let averageNbArticlesSold = 0;
    let mostExpensiveArticleSold = 0;
    let leastExpensiveArticleSold = 0;

    function initChart() {
        canvas = document.getElementById("salesData") as HTMLCanvasElement;
        if (canvas) {
            chart = new Chart(canvas, {
                type: "bar",
                data: {
                    labels: [],
                    datasets: [
                        {
                            label: "Chiffre d'affaires (€)",
                            data: [],
                            borderColor: "#059669",
                            backgroundColor: "#10b981",
                            order: 1,
                        },
                        {
                            label: "Bénéfice brut (€)",
                            borderColor: "#2563eb",
                            data: [],
                            backgroundColor: "#3b82f6",
                            order: 0,
                        },
                    ],
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: {
                            position: "top",
                        },
                        title: {
                            display: true,
                            text: "Chiffre d'affaires et bénéfice brut dans le temps",
                            font: {
                                size: 20,
                            },
                        },
                    },
                },
            });
        }
    }

    function handlePeriodChange(event: Event) {
        selectedPeriod = (event.target as HTMLSelectElement).value;
        exportSalesData();
    }
</script>

{#if showNotif}
    <Notification bind:visible={showNotif} {message} {type} />
{/if}

<div class="mx-auto max-w-7xl px-4 py-8">
    <div class="mb-8 flex items-center justify-between">
        <h1 class="text-3xl font-bold text-gray-900">Secrétariat</h1>
    </div>

    <div class="mb-8 flex border-b">
        <button
            class="mr-4 border-b-2 px-4 py-2 {activeTab === 'sales'
                ? 'border-purple-600 text-purple-600'
                : 'border-transparent text-gray-500 hover:text-gray-700'}"
            on:click={() => (activeTab = "sales")}
        >
            Données de Vente
        </button>
        <button
            class="border-b-2 px-4 py-2 {activeTab === 'management'
                ? 'border-purple-600 text-purple-600'
                : 'border-transparent text-gray-500 hover:text-gray-700'}"
            on:click={() => {
                activeTab = "management";
                showSalesGraph = false;
                chart?.destroy();
            }}
        >
            Gestion
        </button>
    </div>

    {#if activeTab === "sales"}
        <div class="space-y-6">
            <div class="rounded-lg bg-white p-6 shadow">
                <div class="mb-4">
                    <div class="flex items-center text-lg font-medium text-gray-900">
                        <MessageSquare class="mr-2 h-6 w-6 text-purple-600" />
                        <h2>Données de Vente</h2>
                    </div>
                    <div class="mt-2">
                        <div
                            class="inline-flex items-center rounded-full bg-blue-100 px-2.5 py-0.5 text-xs font-medium text-blue-800"
                        >
                            <Settings2 class="mr-1 h-3 w-3" />
                            Token Vinted requis
                        </div>
                    </div>
                </div>

                <div class="space-y-4">
                    <div>
                        <div class="flex items-center gap-4">
                            <p class="mb-2 text-sm font-medium text-gray-700 whitespace-nowrap">Période d'analyse</p>
                            <select
                                on:change={handlePeriodChange}
                                value={selectedPeriod}
                                class="px-4 py-2 text-sm bg-gray-50 border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#0E49B5] focus:border-transparent"
                            >
                                <option value="last1M">Dernier mois</option>
                                <option value="last3M">3 derniers mois</option>
                                <option value="last6M">6 derniers mois</option>
                                <option value="ytd">Année en cours</option>
                                <option value="last1Y">Dernière année</option>
                                <option value="sinceBegin">Depuis le début</option>
                            </select>
                        </div>
                    </div>

                    <div class="grid grid-cols-1 gap-3">
                        <button
                            on:click={exportSalesData}
                            class="inline-flex items-center justify-center space-x-2 rounded-md border border-blue-600 px-4 py-2 text-sm font-medium text-blue-600 transition-colors hover:bg-blue-50 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2"
                        >
                            Exporter les données
                        </button>
                    </div>
                </div>
            </div>

            <div class={`${showSalesGraph ? "block" : "hidden"} rounded-lg bg-white p-6 shadow`}>
                <div class="mb-6">
                    <canvas width="50" height="30" id="salesData"></canvas>
                </div>
            </div>

            {#if showSalesGraph}
                <div class="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
                    <div class="rounded-lg bg-white p-4 shadow border-l-4 border-green-500">
                        <h3 class="text-lg font-semibold text-gray-900 mb-3">Chiffre d'affaires</h3>
                        <div class="space-y-2 text-sm">
                            <p>
                                <span class="font-medium">Total :</span>
                                {totalTurnover.toFixed(2)} €
                            </p>
                            <p>
                                <span class="font-medium">Maximum :</span>
                                {maximumTurnover.toFixed(2)} €
                            </p>
                            <p>
                                <span class="font-medium">Minimum :</span>
                                {minimumTurnover.toFixed(2)} €
                            </p>
                            <p>
                                <span class="font-medium">Moyenne :</span>
                                {averageTurnover.toFixed(2)} €
                            </p>
                        </div>
                    </div>

                    <div class="rounded-lg bg-white p-4 shadow border-l-4 border-blue-500">
                        <h3 class="text-lg font-semibold text-gray-900 mb-3">Bénéfice brut</h3>
                        <div class="space-y-2 text-sm">
                            <p>
                                <span class="font-medium">Total :</span>
                                {totalGrossProfit.toFixed(2)} €
                            </p>
                            <p>
                                <span class="font-medium">Maximum :</span>
                                {maximumGrossProfit.toFixed(2)} €
                            </p>
                            <p>
                                <span class="font-medium">Minimum :</span>
                                {minimumGrossProfit.toFixed(2)} €
                            </p>
                            <p>
                                <span class="font-medium">Moyenne :</span>
                                {averageGrossProfit.toFixed(2)} €
                            </p>
                        </div>
                    </div>

                    <div class="rounded-lg bg-white p-4 shadow border-l-4 border-orange-500">
                        <h3 class="text-lg font-semibold text-gray-900 mb-3">Articles achetés</h3>
                        <div class="space-y-2 text-sm">
                            <p>
                                <span class="font-medium">Total :</span>
                                {totalArticlesBought}
                            </p>
                            <p>
                                <span class="font-medium">Prix moyen :</span>
                                {averageArticleBoughtPrice.toFixed(2)} €
                            </p>
                            <p>
                                <span class="font-medium">Nombre moyen :</span>
                                {averageNbArticlesBought.toFixed(1)}
                            </p>
                            <p>
                                <span class="font-medium">Plus cher :</span>
                                {mostExpensiveArticleBought.toFixed(2)} €
                            </p>
                            <p>
                                <span class="font-medium">Moins cher :</span>
                                {leastExpensiveArticleBought.toFixed(2)} €
                            </p>
                        </div>
                    </div>

                    <div class="rounded-lg bg-white p-4 shadow border-l-4 border-purple-500">
                        <h3 class="text-lg font-semibold text-gray-900 mb-3">Articles vendus</h3>
                        <div class="space-y-2 text-sm">
                            <p>
                                <span class="font-medium">Total :</span>
                                {totalArticlesSold.toFixed(0)}
                            </p>
                            <p>
                                <span class="font-medium">Prix moyen :</span>
                                {averageArticleSoldPrice.toFixed(2)} €
                            </p>
                            <p>
                                <span class="font-medium">Nombre moyen :</span>
                                {averageNbArticlesSold.toFixed(1)}
                            </p>
                            <p>
                                <span class="font-medium">Plus cher :</span>
                                {mostExpensiveArticleSold.toFixed(2)} €
                            </p>
                            <p>
                                <span class="font-medium">Moins cher :</span>
                                {leastExpensiveArticleSold.toFixed(2)} €
                            </p>
                        </div>
                    </div>
                </div>
            {/if}
        </div>
    {/if}

    {#if activeTab === "management"}
        <div class="grid gap-6 md:grid-cols-2">
            <div class="rounded-lg bg-white p-6 shadow">
                <div class="mb-4">
                    <div class="flex items-center text-lg font-medium text-gray-900">
                        <Mail class="mr-2 h-6 w-6 text-purple-600" />
                        <h2>Gestion des Mails</h2>
                    </div>
                    <div class="mt-2 flex flex-wrap gap-2">
                        <div
                            class="inline-flex items-center rounded-full bg-blue-100 px-2.5 py-0.5 text-xs font-medium text-blue-800"
                        >
                            <Settings2 class="mr-1 h-3 w-3" />
                            Token Vinted requis
                        </div>
                        <div
                            class="inline-flex items-center rounded-full bg-green-100 px-2.5 py-0.5 text-xs font-medium text-green-800"
                        >
                            <Mail class="mr-1 h-3 w-3" />
                            IMAP requis
                        </div>
                    </div>
                </div>

                <div class="space-y-4">
                    <div>
                        <p class="mb-2 text-sm font-medium text-gray-700">Message de remerciement</p>
                        <textarea
                            bind:value={autoMessage}
                            rows="3"
                            class="block w-full rounded-md border border-gray-300 px-3 py-2 shadow-sm focus:border-purple-500 focus:outline-none focus:ring-purple-500"
                            placeholder="Message à inclure dans le colis..."
                        ></textarea>
                    </div>

                    <div class="grid grid-cols-2 gap-3">
                        <button
                            class="inline-flex items-center justify-center space-x-2 rounded-md bg-purple-600 px-4 py-2 text-sm font-medium text-white transition-colors hover:bg-purple-700 focus:outline-none focus:ring-2 focus:ring-purple-500 focus:ring-offset-2"
                        >
                            <Mail class="h-4 w-4" />
                            <span>Traiter les mails</span>
                        </button>
                        <button
                            class="inline-flex items-center justify-center space-x-2 rounded-md border border-purple-600 px-4 py-2 text-sm font-medium text-purple-600 transition-colors hover:bg-purple-50 focus:outline-none focus:ring-2 focus:ring-purple-500 focus:ring-offset-2"
                        >
                            <Printer class="h-4 w-4" />
                            <span>Imprimer bordereaux</span>
                        </button>
                    </div>
                </div>
            </div>

            <div class="rounded-lg bg-white p-6 shadow">
                <div class="mb-4">
                    <div class="flex items-center text-lg font-medium text-gray-900">
                        <MessageSquare class="mr-2 h-6 w-6 text-purple-600" />
                        <h2>Gestion des Conversations</h2>
                    </div>
                    <div class="mt-2">
                        <div
                            class="inline-flex items-center rounded-full bg-blue-100 px-2.5 py-0.5 text-xs font-medium text-blue-800"
                        >
                            <Settings2 class="mr-1 h-3 w-3" />
                            Token Vinted requis
                        </div>
                    </div>
                </div>

                <div class="space-y-4">
                    <div>
                        <div class="flex items-center gap-4">
                            <p class="mb-2 text-sm font-medium text-gray-700 whitespace-nowrap">
                                Supprimer les conversations datant de plus de
                            </p>
                            <div class="flex w-full items-center space-x-2">
                                <input
                                    type="number"
                                    bind:value={monthsToKeep}
                                    min="1"
                                    max="12"
                                    class="block rounded-md border border-gray-300 px-3 py-2 shadow-sm focus:border-purple-500 focus:outline-none focus:ring-purple-500"
                                />
                                <p class="text-sm text-gray-600">mois</p>
                            </div>
                        </div>
                    </div>

                    <div class="grid grid-cols-1 gap-3">
                        <button
                            on:click={cleanConversations}
                            class="inline-flex items-center justify-center space-x-2 rounded-md border border-red-600 px-4 py-2 text-sm font-medium text-red-600 transition-colors hover:bg-red-50 focus:outline-none focus:ring-2 focus:ring-red-500 focus:ring-offset-2"
                        >
                            <Trash2 class="h-4 w-4" />
                            <span>Nettoyer</span>
                        </button>
                    </div>
                </div>
            </div>
        </div>
    {/if}
</div>
