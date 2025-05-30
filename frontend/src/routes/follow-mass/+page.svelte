<script lang="ts">
    import { Users, AlertCircle, TreePine, FileText, Link2, UserPlus, History, Save } from "@lucide/svelte";
    import { fetchData } from "../../global/fetchData";
    import Notification from "../../global/components/NotificationCard.svelte";

    let showAlert = true;
    let isFollowing = false;
    let targetCount = 50;
    let vintieUrl = "";
    let followMode: "tree" | "reviews" = "tree";
    let scrapeMode: "followers" | "followings" = "followers";

    let showNotif = false;
    let message = "";
    let type = "";

    async function backupFollowings() {
        const result = await fetchData("GET", "follow-mass/backup-followed-users");
        if (!result.success) {
            showNotif = true;
            message = result.error as string;
            type = "error";
        } else {
            showNotif = true;
            message = "Abonnements sauvegardés avec succès";
            type = "success";
        }
    }

    async function startFollowing() {
        const result = await fetchData("GET", "follow-mass/start-following", {
            followMode: followMode,
            targetCount: targetCount,
        });

        if (!result.success) {
            showNotif = true;
            message = result.error as string;
            type = "error";
        } else {
            showNotif = true;
            message = "Utilisateurs suivis avec succès";
            type = "success";
        }
    }

    async function scrapeVintie() {
        if (!vintieUrl) {
            showNotif = true;
            message = "URL Vinted manquante";
            type = "error";
            return;
        }

        const result = fetchData("GET", "follow-mass/scrap-vinted-user", {
            urlSeller: vintieUrl,
            mode: scrapeMode,
        });

        isFollowing = true;

        result.then((result) => {
            if (!result.success) {
                showNotif = true;
                message = result.error as string;
                type = "error";
            } else {
                showNotif = true;
                message = "Utilisateurs suivis avec succès";
                type = "success";
            }
        });
    }

    async function recoverFollowedUsers() {
        const result = await fetchData("GET", "follow-mass/recover-followed-users");
        if (!result.success) {
            showNotif = true;
            message = result.error as string;
            type = "error";
        } else {
            showNotif = true;
            message = "Abonnements récupérés avec succès";
            type = "success";
        }
    }
</script>

{#if showNotif}
    <Notification bind:visible={showNotif} {message} {type} />
{/if}
<div class="mx-auto max-w-7xl px-4 py-8">
    <h1 class="mb-8 text-3xl font-bold text-gray-900">Suivi en Masse</h1>

    {#if showAlert}
        <div class="mb-6 rounded-md bg-yellow-50 p-4">
            <div class="flex">
                <div class="flex-shrink-0">
                    <AlertCircle class="h-5 w-5 text-yellow-400" />
                </div>
                <div class="ml-3">
                    <h3 class="text-sm font-medium text-yellow-800">Configuration requise</h3>
                    <div class="mt-2 text-sm text-yellow-700">
                        <p>
                            Cette fonctionnalité nécessite votre token Vinted. Configurez-le dans les <a
                                href="/settings"
                                class="font-medium text-yellow-800 underline hover:text-yellow-900"
                            >
                                paramètres
                            </a>
                            .
                        </p>
                    </div>
                </div>
                <button
                    type="button"
                    on:click={() => (showAlert = false)}
                    class="ml-auto -mx-1.5 -my-1.5 rounded-md bg-yellow-50 p-1.5 text-yellow-500 hover:bg-yellow-100"
                >
                    <span class="sr-only">Dismiss</span>
                    <svg class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                        <path
                            d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z"
                        />
                    </svg>
                </button>
            </div>
        </div>
    {/if}

    <div class="mb-6">
        <div class="rounded-lg bg-white p-6 shadow">
            <div class="flex items-center space-x-2">
                <Save class="h-6 w-6 text-green-600" />
                <h2 class="text-lg font-medium text-gray-900">Gestion des abonnements</h2>
            </div>
            <p class="mt-2 text-sm text-gray-600">Sauvegardez ou restaurez vos abonnements Vinted</p>
            <div class="mt-4 flex gap-4">
                <button
                    on:click={backupFollowings}
                    class="flex flex-1 items-center justify-center gap-2 rounded-md bg-green-600 px-4 py-2 text-white hover:bg-green-700"
                >
                    <Save class="h-5 w-5" />
                    Sauvegarder
                </button>
                <button
                    on:click={recoverFollowedUsers}
                    class="flex flex-1 items-center justify-center gap-2 rounded-md bg-red-600 px-4 py-2 text-white hover:bg-red-700"
                >
                    <History class="h-5 w-5" />
                    Restaurer
                </button>
            </div>
        </div>
    </div>

    <div class="grid gap-6 md:grid-cols-2">
        <div class="rounded-lg bg-white p-6 shadow">
            <div class="mb-4">
                <div class="flex items-center text-lg font-medium text-gray-900">
                    <UserPlus class="mr-2 h-6 w-6 text-blue-600" />
                    <h2>Suivi en Masse</h2>
                </div>
                <p class="mt-2 text-sm text-gray-600">Suivez automatiquement des utilisateurs selon le mode choisi.</p>
            </div>

            <div class="space-y-4">
                <div class="space-y-2">
                    <label class="flex items-center space-x-2">
                        <input type="radio" bind:group={followMode} value="tree" class="text-blue-600" />
                        <TreePine class="h-4 w-4" />
                        <span>Mode Arborescence</span>
                    </label>
                    <p class="text-sm text-gray-600">Regarde vos abonnements et les abonnements de vos abonnements</p>
                    <label class="flex items-center space-x-2">
                        <input type="radio" bind:group={followMode} value="reviews" class="text-blue-600" />
                        <FileText class="h-4 w-4" />
                        <span>Mode Avis</span>
                    </label>
                    <p class="text-sm text-gray-600">Suit les utilisateurs qui ont laissé des avis sur vos articles</p>
                </div>

                {#if followMode === "tree"}
                    <div>
                        <p class="block text-sm font-medium text-gray-700">Nombre d'utilisateurs</p>
                        <input
                            type="number"
                            bind:value={targetCount}
                            min="1"
                            max="10000"
                            step="10"
                            class="mt-1 block w-full rounded-md border border-gray-300 px-3 py-2 shadow-sm focus:border-blue-500 focus:outline-none focus:ring-blue-500"
                        />
                    </div>
                {/if}

                <button
                    on:click={startFollowing}
                    class="w-full rounded-md bg-blue-600 px-4 py-2 text-white hover:bg-blue-700"
                >
                    Suivre
                </button>
            </div>
        </div>

        <div class="rounded-lg bg-white p-6 shadow relative items-center block">
            {#if isFollowing}
                <div role="status" class="absolute -translate-x-1/2 -translate-y-1/2 top-2/4 left-1/2">
                    <svg
                        aria-hidden="true"
                        class="w-8 h-8 text-gray-200 animate-spin dark:text-gray-600 fill-blue-600"
                        viewBox="0 0 100 101"
                        fill="none"
                        xmlns="http://www.w3.org/2000/svg"
                    >
                        <path
                            d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z"
                            fill="currentColor"
                        />
                        <path
                            d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z"
                            fill="currentFill"
                        />
                    </svg>
                    <span class="sr-only">Loading...</span>
                </div>
            {/if}

            <div class={isFollowing ? "dark:text-gray-400 opacity-20" : ""}>
                <div class="mb-4">
                    <div class="flex items-center text-lg font-medium text-gray-900">
                        <Link2 class="mr-2 h-6 w-6 text-orange-600" />
                        <h2>Récupération par URL</h2>
                    </div>
                </div>

                <div class="space-y-4">
                    <div>
                        <p class="block text-sm font-medium text-gray-700">URL Vinted</p>
                        <input
                            type="text"
                            bind:value={vintieUrl}
                            placeholder="https://www.vinted.fr/member/..."
                            class="mt-1 block w-full rounded-md border border-gray-300 px-3 py-2 shadow-sm focus:border-orange-500 focus:outline-none focus:ring-orange-500"
                        />
                    </div>

                    <div class="space-y-2">
                        <label class="flex items-center space-x-2">
                            <input type="radio" bind:group={scrapeMode} value="followers" class="text-orange-600" />
                            <Users class="h-4 w-4" />
                            <span>Abonnés</span>
                        </label>
                        <label class="flex items-center space-x-2">
                            <input type="radio" bind:group={scrapeMode} value="followings" class="text-orange-600" />
                            <Users class="h-4 w-4" />
                            <span>Abonnements</span>
                        </label>
                    </div>

                    <button
                        on:click={scrapeVintie}
                        class="w-full rounded-md bg-orange-600 px-4 py-2 text-white hover:bg-orange-700"
                    >
                        Récupérer
                    </button>
                </div>
            </div>
        </div>
    </div>
</div>
