<script lang="ts">
    import { RefreshCw, Trash2, RotateCw, AlertCircle, ShoppingBag, Key, Mail } from "@lucide/svelte";
    import { fetchData } from "../../global/fetchData";
    import Notification from "../../global/components/NotificationCard.svelte";

    let showNotif = false;
    let message = "";
    let type = "";

    async function deleteAllAds() {
        const result = await fetchData("DELETE", "ads-management/all-ads");
        if (result.success) {
            message = "Toutes les annonces ont été supprimées avec succès";
            type = "success";
            showNotif = true;
        }
    }

    async function deleteSoldAds() {
        const result = await fetchData("DELETE", "ads-management/sold-items");
        if (result.success) {
            message = "Toutes les annonces vendues ont été supprimées avec succès";
            type = "success";
            showNotif = true;
        }
    }

    async function refreshAllAds() {
        const result = await fetchData("GET", "ads-management/refresh-ads");
        if (result.success) {
            message = "Toutes les annonces ont été rafraîchies avec succès";
            type = "success";
            showNotif = true;
        }
    }
</script>

{#if showNotif}
    <Notification bind:visible={showNotif} {message} {type} />
{/if}

<div class="mx-auto max-w-7xl px-4 py-8">
    <div class="mb-8 flex items-center justify-between">
        <h1 class="text-3xl font-bold text-gray-900">Gestion des Annonces</h1>
    </div>

    <div class="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
        <!-- Rafraîchissement des Annonces -->
        <div class="rounded-lg bg-white p-6 shadow">
            <div class="mb-4">
                <div class="flex items-center text-lg font-medium text-gray-900">
                    <RefreshCw class="mr-2 h-6 w-6 text-purple-600" />
                    <h2>Rafraîchir les Annonces</h2>
                </div>
                <div class="mt-2">
                    <div
                        class="inline-flex items-center rounded-full bg-blue-100 px-2.5 py-0.5 text-xs font-medium text-blue-800"
                    >
                        <Key class="mr-1 h-3 w-3" />
                        Token Vinted requis
                    </div>
                </div>
            </div>
            <p class="mb-4 text-sm text-gray-600">
                Remontez vos annonces en tête de liste sur Vinted. Rafraîchissez une sélection ou toutes vos annonces en
                un clic.
            </p>
            <div class="grid grid-cols-2 gap-3">
                <!-- todo: sélection les n plus vieux articles à rafraichir -->
                <button
                    class="inline-flex items-center justify-center space-x-2 rounded-md bg-purple-600 px-4 py-2 text-sm font-medium text-white transition-colors hover:bg-purple-700 focus:outline-none focus:ring-2 focus:ring-purple-500 focus:ring-offset-2"
                >
                    <RefreshCw class="h-4 w-4" />
                    <span>Sélection</span>
                </button>
                <button
                    on:click={refreshAllAds}
                    class="inline-flex items-center justify-center space-x-2 rounded-md border border-purple-600 px-4 py-2 text-sm font-medium text-purple-600 transition-colors hover:bg-purple-50 focus:outline-none focus:ring-2 focus:ring-purple-500 focus:ring-offset-2"
                >
                    <RefreshCw class="h-4 w-4" />
                    <span>Tout</span>
                </button>
            </div>
        </div>

        <!-- Suppression des Annonces -->
        <div class="rounded-lg bg-white p-6 shadow">
            <div class="mb-4">
                <div class="flex items-center text-lg font-medium text-gray-900">
                    <Trash2 class="mr-2 h-6 w-6 text-red-600" />
                    <h2>Suppression des Annonces</h2>
                </div>
                <div class="mt-2">
                    <div
                        class="inline-flex items-center rounded-full bg-blue-100 px-2.5 py-0.5 text-xs font-medium text-blue-800"
                    >
                        <Key class="mr-1 h-3 w-3" />
                        Token Vinted requis
                    </div>
                </div>
            </div>
            <p class="mb-4 text-sm text-gray-600">
                Gérez efficacement vos annonces en supprimant les articles vendus ou en faisant un grand ménage de votre
                profil.
            </p>
            <div class="grid grid-cols-2 gap-3">
                <button
                    on:click={deleteSoldAds}
                    class="inline-flex items-center justify-center space-x-2 rounded-md bg-red-600 px-4 py-2 text-sm font-medium text-white transition-colors hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-red-500 focus:ring-offset-2"
                >
                    <Trash2 class="h-4 w-4" />
                    <span>Vendus</span>
                </button>
                <button
                    on:click={deleteAllAds}
                    class="inline-flex items-center justify-center space-x-2 rounded-md border border-red-600 px-4 py-2 text-sm font-medium text-red-600 transition-colors hover:bg-red-50 focus:outline-none focus:ring-2 focus:ring-red-500 focus:ring-offset-2"
                >
                    <Trash2 class="h-4 w-4" />
                    <span>Tout</span>
                </button>
            </div>
        </div>

        <!-- Vente Automatique -->
        <div class="rounded-lg bg-white p-6 shadow opacity-40">
            <div class="mb-4">
                <div class="flex items-center text-lg font-medium text-gray-900">
                    <RotateCw class="mr-2 h-6 w-6 text-purple-600" />
                    <h2>Vente Automatique</h2>
                    <span class="ml-auto text-xs text-gray-500">En cours de développement</span>
                </div>
                <div class="mt-2 flex flex-wrap gap-2">
                    <div
                        class="inline-flex items-center rounded-full bg-blue-100 px-2.5 py-0.5 text-xs font-medium text-blue-800"
                    >
                        <Key class="mr-1 h-3 w-3" />
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
            <p class="mb-4 text-sm text-gray-600">
                Automatisez la repose de vos annonces programmées en plusieurs exemplaires. Évitez les tâches
                répétitives et chronophages.
            </p>
            <button
                disabled
                class="inline-flex w-full items-center justify-center space-x-2 rounded-md bg-purple-600 px-4 py-2 text-sm font-medium text-white transition-colors hover:bg-purple-700 focus:outline-none focus:ring-2 focus:ring-purple-500 focus:ring-offset-2 cursor-not-allowed"
            >
                <ShoppingBag class="h-5 w-5" />
                <span>Sélectionner les articles</span>
            </button>
        </div>
    </div>
</div>
