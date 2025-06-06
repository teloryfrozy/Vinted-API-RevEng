<script lang="ts">
    import { Globe, Mail,  Shield, Wrench } from "@lucide/svelte";
    import { fetchData } from "../../global/fetchData";
    import Notification from "../../global/components/NotificationCard.svelte";

    let showNotif = false;
    let message = "";
    let type = "";

    let settings = {
        language: "fr",
        notifications: true,
        darkMode: false,
        emailSettings: {
            host: "",
            port: "",
            username: "",
            password: "",
        },
        vintedToken: "",
        vintedAccessToken: "",
        vintedRefreshToken: "",
        userProfileURL: "",
    };

    async function saveToken() {
        const tokenData = {
            vintedAccessToken: settings.vintedAccessToken ,
            vintedRefreshToken: settings.vintedRefreshToken ,
        };

        if (!tokenData.vintedAccessToken && !tokenData.vintedRefreshToken) {
            showNotif = true;
            message = "Au moins un token est requis";
            type = "error";
            return;
        }

        const result = await fetchData("POST", "auth/vinted-token", tokenData);
        if (result.success) {
            showNotif = true;
            message = "Token(s) sauvegardé(s) avec succès";
            type = "success";
        } else {
            showNotif = true;
            message = result.error as string;
            type = "error";
        }
    }

    async function saveSettings() {
        const result = await fetchData("POST", "auth/settings", settings);
        if (result.success) {
            showNotif = true;
            message = "Paramètres sauvegardés avec succès";
            type = "success";
        } else {
            showNotif = true;
            message = result.error as string;
            type = "error";
        }
    } 
</script>

{#if showNotif}
    <Notification bind:visible={showNotif} {message} {type} />
{/if}
<div class="mx-auto max-w-4xl px-4 py-8">
    <div class="mb-8 flex items-center justify-between">
        <h1 class="text-3xl font-bold text-gray-900">Paramètres</h1>
        <button
            on:click={saveSettings}
            class="inline-flex items-center rounded-md bg-purple-600 px-4 py-2 text-sm font-medium text-white hover:bg-purple-700 focus:outline-none focus:ring-2 focus:ring-purple-500 focus:ring-offset-2"
        >
            <Wrench class="mr-2 h-4 w-4" />
            Sauvegarder
        </button>
    </div>

    <div class="grid gap-6 md:grid-cols-2"> 
        <div class="rounded-lg bg-white p-6 shadow">
            <div class="mb-6 flex items-center border-b pb-4">
                <Globe class="mr-2 h-5 w-5 text-purple-600" />
                <h2 class="text-xl font-semibold text-gray-900">Préférences Générales</h2>
            </div>

            <div class="space-y-4"> 
                <div>
                    <p>Langue</p>
                    <select
                        bind:value={settings.language}
                        class="mt-1 block w-full rounded-md border border-gray-300 bg-white py-2 px-3 shadow-sm focus:border-purple-500 focus:outline-none focus:ring-purple-500"
                    >
                        <option value="fr">Français</option>
                        <option value="en">English</option>
                    </select>
                </div>
                <div>
                    <p class="block text-sm font-medium text-gray-700">Profil Vinted</p>
                    <div class="mt-1 flex rounded-md shadow-sm">
                        <input
                            bind:value={settings.userProfileURL}
                            placeholder="https://www.vinted.fr/users/ID"
                            class="block w-full flex-1 rounded-md border border-gray-300 px-3 py-2 focus:border-purple-500 focus:outline-none focus:ring-purple-500"
                        />
                    </div>
                </div>
            </div>
        </div>
 
        <div class="rounded-lg bg-white p-6 shadow">
            <div class="mb-6 flex items-center border-b pb-4">
                <Mail class="mr-2 h-5 w-5 text-purple-600" />
                <h2 class="text-xl font-semibold text-gray-900">Configuration Email</h2>
            </div>

            <div class="space-y-4">
                <div class="grid grid-cols-2 gap-4">
                    <div>
                        <p class="block text-sm font-medium text-gray-700">Serveur IMAP</p>
                        <input
                            type="text"
                            bind:value={settings.emailSettings.host}
                            placeholder="imap.gmail.com"
                            class="mt-1 block w-full rounded-md border border-gray-300 px-3 py-2 shadow-sm focus:border-purple-500 focus:outline-none focus:ring-purple-500"
                        />
                    </div>
                    <div>
                        <p class="block text-sm font-medium text-gray-700">Port</p>
                        <input
                            type="text"
                            bind:value={settings.emailSettings.port}
                            placeholder="993"
                            class="mt-1 block w-full rounded-md border border-gray-300 px-3 py-2 shadow-sm focus:border-purple-500 focus:outline-none focus:ring-purple-500"
                        />
                    </div>
                </div>

                <div>
                    <p class="block text-sm font-medium text-gray-700">Email</p>
                    <input
                        type="email"
                        bind:value={settings.emailSettings.username}
                        placeholder="exemple@gmail.com"
                        class="mt-1 block w-full rounded-md border border-gray-300 px-3 py-2 shadow-sm focus:border-purple-500 focus:outline-none focus:ring-purple-500"
                    />
                </div>

                <div>
                    <p class="block text-sm font-medium text-gray-700">Mot de passe</p>
                    <input
                        type="password"
                        bind:value={settings.emailSettings.password}
                        placeholder="••••••••"
                        class="mt-1 block w-full rounded-md border border-gray-300 px-3 py-2 shadow-sm focus:border-purple-500 focus:outline-none focus:ring-purple-500"
                    />
                </div>
            </div>
        </div>
 
        <div class="rounded-lg bg-white p-6 shadow md:col-span-2">
            <div class="mb-6 flex items-center border-b pb-4">
                <Shield class="mr-2 h-5 w-5 text-purple-600" />
                <h2 class="text-xl font-semibold text-gray-900">Token Vinted</h2>
                <p class="mt-2 text-sm text-gray-500 ml-2">
                    Les tokens sont nécessaires pour automatiser les actions sur Vinted
                </p>
            </div>

            <div class="space-y-4">
                <div>
                    <p class="block text-sm font-medium text-gray-700">Access Token</p>
                    <div class="mt-1 flex rounded-md shadow-sm">
                        <input
                            bind:value={settings.vintedAccessToken}
                            placeholder="Collez votre access token Vinted ici"
                            class="block w-full flex-1 rounded-md border border-gray-300 px-3 py-2 focus:border-purple-500 focus:outline-none focus:ring-purple-500"
                        />
                    </div>
                </div>
                <div>
                    <p class="block text-sm font-medium text-gray-700">Refresh Token</p>
                    <div class="mt-1 flex rounded-md shadow-sm">
                        <input
                            bind:value={settings.vintedRefreshToken}
                            placeholder="Collez votre refresh token Vinted ici"
                            class="block w-full flex-1 rounded-md border border-gray-300 px-3 py-2 focus:border-purple-500 focus:outline-none focus:ring-purple-500"
                        />
                    </div>
                    <button
                        on:click={saveToken}
                        class="mt-4 inline-flex w-full items-center justify-center rounded-md bg-purple-600 px-4 py-2 text-sm font-medium text-white hover:bg-purple-700 focus:outline-none focus:ring-2 focus:ring-purple-500 focus:ring-offset-2"
                    >
                        Sauvegarder les tokens
                    </button>
                </div>
            </div>
        </div>
    </div>
</div>
