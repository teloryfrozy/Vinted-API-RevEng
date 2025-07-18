<script lang="ts">
    import { Mail, Trash2, MessageSquare, Printer, Settings2, Plus, Edit, Copy } from "@lucide/svelte";
    import { fetchData } from "../../global/fetchData";
    import Notification from "../../global/components/NotificationCard.svelte";
    import { onMount } from "svelte";
    import Chart from "chart.js/auto";
    import { _ } from 'svelte-i18n';

    interface FavoriteMessage {
        id: number | null;
        name: string;
        message: string;
        createdAt: string;
        updatedAt: string | null;
        userId: number;
    }

    let monthsToKeep = 2;
    let autoMessage = "Merci pour votre achat ! N'oubliez pas de laisser un avis 😊";

    let favoriteMessages: FavoriteMessage[] = [];
    let newMessageName = "";
    let newMessageContent = "";
    let editingMessage: FavoriteMessage | null = null;
    let editMessageName = "";
    let editMessageContent = "";

    let showNotif = false;
    let message = "";
    let type = "";
    let selectedPeriod = "last1Y";

    onMount(async () => {
        await loadFavoriteMessages();
        console.log(favoriteMessages);
    });

    async function loadFavoriteMessages() {
        const result = await fetchData("GET", "accounting/favorite-messages");
        if (result.success) {
            favoriteMessages = result.data.messages;
        } else {
            showNotif = true;
            message = result.error as string;
            type = "error";
        }
    }

    async function addFavoriteMessage() {
        if (!newMessageName.trim() || !newMessageContent.trim()) {
            showNotif = true;
            message = $_('accountingPage.messages.fillFields');
            type = "error";
            return;
        }

        const result = await fetchData("POST", "accounting/add-favorite-message", {
            name: newMessageName,
            message: newMessageContent,
        });

        if (result.success) {
            showNotif = true;
            message = $_('accountingPage.messages.messageAdded');
            type = "success";
            newMessageName = "";
            newMessageContent = "";
            await loadFavoriteMessages();
        } else {
            showNotif = true;
            message = result.error as string;
            type = "error";
        }
    }

    async function deleteFavoriteMessage(id: number) {
        const result = await fetchData("DELETE", "accounting/delete-favorite-message", {
            id: id,
        });

        if (result.success) {
            showNotif = true;
            message = $_('accountingPage.messages.messageDeleted');
            type = "success";
            await loadFavoriteMessages();
        } else {
            showNotif = true;
            message = result.error as string;
            type = "error";
        }
    }

    async function updateFavoriteMessage() {
        if (!editMessageName.trim() || !editMessageContent.trim()) {
            showNotif = true;
            message = $_('accountingPage.messages.fillFields');
            type = "error";
            return;
        }

        if (!editingMessage || !editingMessage.id) {
            showNotif = true;
            message = $_('accountingPage.messages.noEditingMessage');
            type = "error";
            return;
        }

        const result = await fetchData("PATCH", "accounting/update-favorite-message", {
            id: editingMessage.id as number,
            name: editMessageName,
            message: editMessageContent,
        });

        if (result.success) {
            showNotif = true;
            message = $_('accountingPage.messages.messageUpdated');
            type = "success";
            editingMessage = null;
            await loadFavoriteMessages();
        } else {
            showNotif = true;
            message = result.error as string;
            type = "error";
        }
    }

    function startEdit(message: FavoriteMessage) {
        editingMessage = message;
        editMessageName = message.name;
        editMessageContent = message.message;
    }

    function cancelEdit() {
        editingMessage = null;
        editMessageName = "";
        editMessageContent = "";
    }

    function copyToClipboard(text: string) {
        navigator.clipboard.writeText(text);
        showNotif = true;
        message = $_('accountingPage.messages.messageCopied');
        type = "success";
    }

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
            message = $_('accountingPage.messages.conversationsCleaned');
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
        message = $_('accountingPage.messages.salesDataExported');
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
    let activeTab = "favorites";

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
                            label: $_('accountingPage.sales.chart.grossProfit'),
                            borderColor: "#2563eb",
                            data: [],
                            backgroundColor: "#3b82f6",
                            order: 0,
                        },
                        {
                            label: $_('accountingPage.sales.chart.turnover'),
                            data: [],
                            borderColor: "#059669",
                            backgroundColor: "#10b981",
                            order: 1,
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
                            text: $_('accountingPage.sales.chart.title'),
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
        <h1 class="text-3xl font-bold text-gray-900">{$_('accountingPage.title')}</h1>
    </div>

    <div class="mb-8 flex border-b">
        <button
            class="mr-4 border-b-2 px-4 py-2 {activeTab === 'favorites'
                ? 'border-purple-600 text-purple-600'
                : 'border-transparent text-gray-500 hover:text-gray-700'}"
            on:click={() => (activeTab = "favorites")}
        >
            {$_('accountingPage.tabs.favorites')}
        </button>
        <button
            class="mr-4 border-b-2 px-4 py-2 {activeTab === 'sales'
                ? 'border-purple-600 text-purple-600'
                : 'border-transparent text-gray-500 hover:text-gray-700'}"
            on:click={() => (activeTab = "sales")}
        >
            {$_('accountingPage.tabs.sales')}
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
            {$_('accountingPage.tabs.management')}
        </button>
    </div>

    {#if activeTab === "favorites"}
        <div class="space-y-6">
            <div class="rounded-lg bg-white p-6 shadow">
                <div class="mb-4">
                    <div class="flex items-center text-lg font-medium text-gray-900">
                        <MessageSquare class="mr-2 h-6 w-6 text-purple-600" />
                        <h2>{$_('accountingPage.favorites.title')}</h2>
                    </div>
                </div>

                <div class="mb-6 space-y-4">
                    <div class="grid grid-cols-1 gap-4 md:grid-cols-2">
                        <div>
                            <p class="block text-sm font-medium text-gray-700 mb-2">{$_('accountingPage.favorites.addMessage.nameLabel')}</p>
                            <input
                                type="text"
                                bind:value={newMessageName}
                                placeholder={$_('accountingPage.favorites.addMessage.namePlaceholder')}
                                class="block w-full rounded-md border border-gray-300 px-3 py-2 shadow-sm focus:border-purple-500 focus:outline-none focus:ring-purple-500"
                            />
                        </div>
                        <div>
                            <p class="block text-sm font-medium text-gray-700 mb-2">{$_('accountingPage.favorites.addMessage.contentLabel')}</p>
                            <textarea
                                bind:value={newMessageContent}
                                placeholder={$_('accountingPage.favorites.addMessage.contentPlaceholder')}
                                class="block w-full rounded-md border border-gray-300 px-3 py-2 shadow-sm focus:border-purple-500 focus:outline-none focus:ring-purple-500"
                            ></textarea>
                        </div>
                    </div>
                    <button
                        on:click={addFavoriteMessage}
                        class="inline-flex items-center justify-center space-x-2 rounded-md bg-purple-600 px-4 py-2 text-sm font-medium text-white transition-colors hover:bg-purple-700 focus:outline-none focus:ring-2 focus:ring-purple-500 focus:ring-offset-2"
                    >
                        <Plus class="h-4 w-4" />
                        <span>{$_('accountingPage.favorites.addMessage.button')}</span>
                    </button>
                </div>

                <div class="space-y-4">
                    {#if favoriteMessages.length === 0}
                        <div class="text-center py-8 text-gray-500">
                            <MessageSquare class="mx-auto h-12 w-12 text-gray-300 mb-4" />
                            <p>{$_('accountingPage.favorites.emptyState.title')}</p>
                            <p class="text-sm">{$_('accountingPage.favorites.emptyState.subtitle')}</p>
                        </div>
                    {:else}
                        {#each favoriteMessages as message}
                            <div class="border border-gray-200 rounded-lg p-4">
                                {#if editingMessage?.id === message.id}
                                    <div class="space-y-4">
                                        <div class="grid grid-cols-1 gap-4 md:grid-cols-2">
                                            <div>
                                                <p class="block text-sm font-medium text-gray-700 mb-2">{$_('accountingPage.favorites.edit.nameLabel')}</p>
                                                <input
                                                    type="text"
                                                    bind:value={editMessageName}
                                                    class="block w-full rounded-md border border-gray-300 px-3 py-2 shadow-sm focus:border-purple-500 focus:outline-none focus:ring-purple-500"
                                                />
                                            </div>
                                            <div>
                                                <p class="block text-sm font-medium text-gray-700 mb-2">{$_('accountingPage.favorites.edit.contentLabel')}</p>
                                                <input
                                                    type="text"
                                                    bind:value={editMessageContent}
                                                    class="block w-full rounded-md border border-gray-300 px-3 py-2 shadow-sm focus:border-purple-500 focus:outline-none focus:ring-purple-500"
                                                />
                                            </div>
                                        </div>
                                        <div class="flex space-x-2">
                                            <button
                                                on:click={updateFavoriteMessage}
                                                class="inline-flex items-center justify-center space-x-2 rounded-md bg-green-600 px-3 py-1.5 text-sm font-medium text-white transition-colors hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-green-500 focus:ring-offset-2"
                                            >
                                                {$_('accountingPage.favorites.edit.saveButton')}
                                            </button>
                                            <button
                                                on:click={cancelEdit}
                                                class="inline-flex items-center justify-center space-x-2 rounded-md border border-gray-300 px-3 py-1.5 text-sm font-medium text-gray-700 transition-colors hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-gray-500 focus:ring-offset-2"
                                            >
                                                {$_('accountingPage.favorites.edit.cancelButton')}
                                            </button>
                                        </div>
                                    </div>
                                {:else}
                                    <div class="flex items-start justify-between">
                                        <div class="flex-1">
                                            <h3 class="font-medium text-gray-900 mb-1">{message.name}</h3>
                                            <p class="text-gray-600 text-sm">{message.message}</p>
                                        </div>
                                        <div class="flex space-x-2 ml-4">
                                            <button
                                                on:click={() => copyToClipboard(message.message)}
                                                class="inline-flex items-center justify-center space-x-1 rounded-md border border-gray-300 px-2 py-1 text-xs font-medium text-gray-700 transition-colors hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-gray-500 focus:ring-offset-2"
                                                title={$_('accountingPage.favorites.actions.copy')}
                                            >
                                                <Copy class="h-4 w-4" />
                                            </button>
                                            <button
                                                on:click={() => startEdit(message)}
                                                class="inline-flex items-center justify-center space-x-1 rounded-md border border-gray-300 px-2 py-1 text-xs font-medium text-gray-700 transition-colors hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-gray-500 focus:ring-offset-2"
                                                title={$_('accountingPage.favorites.actions.edit')}
                                            >
                                                <Edit class="h-3 w-3" />
                                            </button>
                                            <button
                                                on:click={() => message.id && deleteFavoriteMessage(message.id)}
                                                class="inline-flex items-center justify-center space-x-1 rounded-md border border-red-300 px-2 py-1 text-xs font-medium text-red-700 transition-colors hover:bg-red-50 focus:outline-none focus:ring-2 focus:ring-red-500 focus:ring-offset-2"
                                                title={$_('accountingPage.favorites.actions.delete')}
                                            >
                                                <Trash2 class="h-3 w-3" />
                                            </button>
                                        </div>
                                    </div>
                                {/if}
                            </div>
                        {/each}
                    {/if}
                </div>
            </div>
        </div>
    {:else if activeTab === "sales"}
        <div class="space-y-6">
            <div class="rounded-lg bg-white p-6 shadow">
                <div class="mb-4">
                    <div class="flex items-center text-lg font-medium text-gray-900">
                        <MessageSquare class="mr-2 h-6 w-6 text-purple-600" />
                        <h2>{$_('accountingPage.sales.title')}</h2>
                    </div>
                    <div class="mt-2">
                        <div
                            class="inline-flex items-center rounded-full bg-blue-100 px-2.5 py-0.5 text-xs font-medium text-blue-800"
                        >
                            <Settings2 class="mr-1 h-3 w-3" />
                            {$_('accountingPage.sales.tokenRequired')}
                        </div>
                    </div>
                </div>

                <div class="space-y-4">
                    <div>
                        <div class="flex items-center gap-4">
                            <p class="mb-2 text-sm font-medium text-gray-700 whitespace-nowrap">{$_('accountingPage.sales.periodLabel')}</p>
                            <select
                                on:change={handlePeriodChange}
                                value={selectedPeriod}
                                class="px-4 py-2 text-sm bg-gray-50 border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#0E49B5] focus:border-transparent"
                            >
                                <option value="last1M">{$_('accountingPage.sales.periods.last1M')}</option>
                                <option value="last3M">{$_('accountingPage.sales.periods.last3M')}</option>
                                <option value="last6M">{$_('accountingPage.sales.periods.last6M')}</option>
                                <option value="ytd">{$_('accountingPage.sales.periods.ytd')}</option>
                                <option value="last1Y">{$_('accountingPage.sales.periods.last1Y')}</option>
                                <option value="sinceBegin">{$_('accountingPage.sales.periods.sinceBegin')}</option>
                            </select>
                        </div>
                    </div>

                    <div class="grid grid-cols-1 gap-3">
                        <button
                            on:click={exportSalesData}
                            class="inline-flex items-center justify-center space-x-2 rounded-md border border-blue-600 px-4 py-2 text-sm font-medium text-blue-600 transition-colors hover:bg-blue-50 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2"
                        >
                            {$_('accountingPage.sales.exportButton')}
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
                        <h3 class="text-lg font-semibold text-gray-900 mb-3">{$_('accountingPage.sales.stats.turnover.title')}</h3>
                        <div class="space-y-2 text-sm">
                            <p>
                                <span class="font-medium">{$_('accountingPage.sales.stats.turnover.total')} :</span>
                                {totalTurnover.toFixed(2)} €
                            </p>
                            <p>
                                <span class="font-medium">{$_('accountingPage.sales.stats.turnover.maximum')} :</span>
                                {maximumTurnover.toFixed(2)} €
                            </p>
                            <p>
                                <span class="font-medium">{$_('accountingPage.sales.stats.turnover.minimum')} :</span>
                                {minimumTurnover.toFixed(2)} €
                            </p>
                            <p>
                                <span class="font-medium">{$_('accountingPage.sales.stats.turnover.average')} :</span>
                                {averageTurnover.toFixed(2)} €
                            </p>
                        </div>
                    </div>

                    <div class="rounded-lg bg-white p-4 shadow border-l-4 border-blue-500">
                        <h3 class="text-lg font-semibold text-gray-900 mb-3">{$_('accountingPage.sales.stats.grossProfit.title')}</h3>
                        <div class="space-y-2 text-sm">
                            <p>
                                <span class="font-medium">{$_('accountingPage.sales.stats.grossProfit.total')} :</span>
                                {totalGrossProfit.toFixed(2)} €
                            </p>
                            <p>
                                <span class="font-medium">{$_('accountingPage.sales.stats.grossProfit.maximum')} :</span>
                                {maximumGrossProfit.toFixed(2)} €
                            </p>
                            <p>
                                <span class="font-medium">{$_('accountingPage.sales.stats.grossProfit.minimum')} :</span>
                                {minimumGrossProfit.toFixed(2)} €
                            </p>
                            <p>
                                <span class="font-medium">{$_('accountingPage.sales.stats.grossProfit.average')} :</span>
                                {averageGrossProfit.toFixed(2)} €
                            </p>
                        </div>
                    </div>

                    <div class="rounded-lg bg-white p-4 shadow border-l-4 border-orange-500">
                        <h3 class="text-lg font-semibold text-gray-900 mb-3">{$_('accountingPage.sales.stats.bought.title')}</h3>
                        <div class="space-y-2 text-sm">
                            <p>
                                <span class="font-medium">{$_('accountingPage.sales.stats.bought.total')} :</span>
                                {totalArticlesBought}
                            </p>
                            <p>
                                <span class="font-medium">{$_('accountingPage.sales.stats.bought.averagePrice')} :</span>
                                {averageArticleBoughtPrice.toFixed(2)} €
                            </p>
                            <p>
                                <span class="font-medium">{$_('accountingPage.sales.stats.bought.averageCount')} :</span>
                                {averageNbArticlesBought.toFixed(1)}
                            </p>
                            <p>
                                <span class="font-medium">{$_('accountingPage.sales.stats.bought.mostExpensive')} :</span>
                                {mostExpensiveArticleBought.toFixed(2)} €
                            </p>
                            <p>
                                <span class="font-medium">{$_('accountingPage.sales.stats.bought.leastExpensive')} :</span>
                                {leastExpensiveArticleBought.toFixed(2)} €
                            </p>
                        </div>
                    </div>

                    <div class="rounded-lg bg-white p-4 shadow border-l-4 border-purple-500">
                        <h3 class="text-lg font-semibold text-gray-900 mb-3">{$_('accountingPage.sales.stats.sold.title')}</h3>
                        <div class="space-y-2 text-sm">
                            <p>
                                <span class="font-medium">{$_('accountingPage.sales.stats.sold.total')} :</span>
                                {totalArticlesSold.toFixed(0)}
                            </p>
                            <p>
                                <span class="font-medium">{$_('accountingPage.sales.stats.sold.averagePrice')} :</span>
                                {averageArticleSoldPrice.toFixed(2)} €
                            </p>
                            <p>
                                <span class="font-medium">{$_('accountingPage.sales.stats.sold.averageCount')} :</span>
                                {averageNbArticlesSold.toFixed(1)}
                            </p>
                            <p>
                                <span class="font-medium">{$_('accountingPage.sales.stats.sold.mostExpensive')} :</span>
                                {mostExpensiveArticleSold.toFixed(2)} €
                            </p>
                            <p>
                                <span class="font-medium">{$_('accountingPage.sales.stats.sold.leastExpensive')} :</span>
                                {leastExpensiveArticleSold.toFixed(2)} €
                            </p>
                        </div>
                    </div>
                </div>
            {/if}
        </div>
    {:else if activeTab === "management"}
        <div class="grid gap-6 md:grid-cols-2">
            <div class="rounded-lg bg-white p-6 shadow">
                <div class="mb-4">
                    <div class="flex items-center text-lg font-medium text-gray-900">
                        <Mail class="mr-2 h-6 w-6 text-purple-600" />
                        <h2>{$_('accountingPage.management.email.title')}</h2>
                    </div>
                    <div class="mt-2 flex flex-wrap gap-2">
                        <div
                            class="inline-flex items-center rounded-full bg-blue-100 px-2.5 py-0.5 text-xs font-medium text-blue-800"
                        >
                            <Settings2 class="mr-1 h-3 w-3" />
                            {$_('accountingPage.management.email.tokenRequired')}
                        </div>
                        <div
                            class="inline-flex items-center rounded-full bg-green-100 px-2.5 py-0.5 text-xs font-medium text-green-800"
                        >
                            <Mail class="mr-1 h-3 w-3" />
                            {$_('accountingPage.management.email.imapRequired')}
                        </div>
                    </div>
                </div>

                <div class="space-y-4">
                    <div>
                        <p class="mb-2 text-sm font-medium text-gray-700">{$_('accountingPage.management.email.thankMessageLabel')}</p>
                        <textarea
                            bind:value={autoMessage}
                            rows="3"
                            class="block w-full rounded-md border border-gray-300 px-3 py-2 shadow-sm focus:border-purple-500 focus:outline-none focus:ring-purple-500"
                            placeholder={$_('accountingPage.management.email.thankMessagePlaceholder')}
                        ></textarea>
                    </div>

                    <div class="grid grid-cols-2 gap-3">
                        <button
                            class="inline-flex items-center justify-center space-x-2 rounded-md bg-purple-600 px-4 py-2 text-sm font-medium text-white transition-colors hover:bg-purple-700 focus:outline-none focus:ring-2 focus:ring-purple-500 focus:ring-offset-2"
                        >
                            <Mail class="h-4 w-4" />
                            <span>{$_('accountingPage.management.email.processButton')}</span>
                        </button>
                        <button
                            class="inline-flex items-center justify-center space-x-2 rounded-md border border-purple-600 px-4 py-2 text-sm font-medium text-purple-600 transition-colors hover:bg-purple-50 focus:outline-none focus:ring-2 focus:ring-purple-500 focus:ring-offset-2"
                        >
                            <Printer class="h-4 w-4" />
                            <span>{$_('accountingPage.management.email.printButton')}</span>
                        </button>
                    </div>
                </div>
            </div>

            <div class="rounded-lg bg-white p-6 shadow">
                <div class="mb-4">
                    <div class="flex items-center text-lg font-medium text-gray-900">
                        <MessageSquare class="mr-2 h-6 w-6 text-purple-600" />
                        <h2>{$_('accountingPage.management.conversations.title')}</h2>
                    </div>
                    <div class="mt-2">
                        <div
                            class="inline-flex items-center rounded-full bg-blue-100 px-2.5 py-0.5 text-xs font-medium text-blue-800"
                        >
                            <Settings2 class="mr-1 h-3 w-3" />
                            {$_('accountingPage.management.conversations.tokenRequired')}
                        </div>
                    </div>
                </div>

                <div class="space-y-4">
                    <div>
                        <div class="flex items-center gap-4">
                            <p class="mb-2 text-sm font-medium text-gray-700 whitespace-nowrap">
                                {$_('accountingPage.management.conversations.deleteLabel')}
                            </p>
                            <div class="flex w-full items-center space-x-2">
                                <input
                                    type="number"
                                    bind:value={monthsToKeep}
                                    min="1"
                                    max="12"
                                    class="block rounded-md border border-gray-300 px-3 py-2 shadow-sm focus:border-purple-500 focus:outline-none focus:ring-purple-500"
                                />
                                <p class="text-sm text-gray-600">{$_('accountingPage.management.conversations.months')}</p>
                            </div>
                        </div>
                    </div>

                    <div class="grid grid-cols-1 gap-3">
                        <button
                            on:click={cleanConversations}
                            class="inline-flex items-center justify-center space-x-2 rounded-md border border-red-600 px-4 py-2 text-sm font-medium text-red-600 transition-colors hover:bg-red-50 focus:outline-none focus:ring-2 focus:ring-red-500 focus:ring-offset-2"
                        >
                            <Trash2 class="h-4 w-4" />
                            <span>{$_('accountingPage.management.conversations.cleanButton')}</span>
                        </button>
                    </div>
                </div>
            </div>
        </div>
    {/if}
</div>
