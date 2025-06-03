<script lang="ts">
    import { Mail, Trash2, MessageSquare, Printer, Star, Settings2 } from "@lucide/svelte";
    import { fetchData } from "../../global/fetchData";
    import Notification from "../../global/components/NotificationCard.svelte";

    let monthsToKeep = 2;
    let autoMessage = "Merci pour votre achat ! N'oubliez pas de laisser un avis 😊";

    let showNotif = false;
    let message = "";
    let type = "";

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
</script>

{#if showNotif}
    <Notification bind:visible={showNotif} {message} {type} />
{/if}
<div class="mx-auto max-w-7xl px-4 py-8">
    <div class="mb-8 flex items-center justify-between">
        <h1 class="text-3xl font-bold text-gray-900">Secrétariat</h1>
    </div>

    <div class="grid gap-6 md:grid-cols-2">
        <!-- Gestion des Mails -->
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

        <!-- Gestion des Conversations -->
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
</div>
