<script lang="ts">
    import { Globe, Mail,  Shield, Wrench } from "@lucide/svelte";
    import { fetchData } from "../../global/fetchData";
    import Notification from "../../global/components/NotificationCard.svelte";
    import { _ } from 'svelte-i18n';

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
            message = $_('settingsPage.messages.tokenRequired');
            type = "error";
            return;
        }

        const result = await fetchData("POST", "auth/vinted-token", tokenData);
        if (result.success) {
            showNotif = true;
            message = $_('settingsPage.messages.tokenSaved');
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
            message = $_('settingsPage.messages.settingsSaved');
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
        <h1 class="text-3xl font-bold text-gray-900">{$_('settingsPage.title')}</h1>
        <button
            on:click={saveSettings}
            class="inline-flex items-center rounded-md bg-purple-600 px-4 py-2 text-sm font-medium text-white hover:bg-purple-700 focus:outline-none focus:ring-2 focus:ring-purple-500 focus:ring-offset-2"
        >
            <Wrench class="mr-2 h-4 w-4" />
            {$_('settingsPage.saveButton')}
        </button>
    </div>

    <div class="grid gap-6 md:grid-cols-2"> 
        <div class="rounded-lg bg-white p-6 shadow">
            <div class="mb-6 flex items-center border-b pb-4">
                <Globe class="mr-2 h-5 w-5 text-purple-600" />
                <h2 class="text-xl font-semibold text-gray-900">{$_('settingsPage.generalPreferences.title')}</h2>
            </div>

            <div class="space-y-4"> 
                <div>
                    <p>{$_('settingsPage.generalPreferences.language')}</p>
                    <select
                        bind:value={settings.language}
                        class="mt-1 block w-full rounded-md border border-gray-300 bg-white py-2 px-3 shadow-sm focus:border-purple-500 focus:outline-none focus:ring-purple-500"
                    >
                        <option value="fr">{$_('settingsPage.generalPreferences.languageOptions.fr')}</option>
                        <option value="en">{$_('settingsPage.generalPreferences.languageOptions.en')}</option>
                    </select>
                </div>
                <div>
                    <p class="block text-sm font-medium text-gray-700">{$_('settingsPage.generalPreferences.vintedProfile')}</p>
                    <div class="mt-1 flex rounded-md shadow-sm">
                        <input
                            bind:value={settings.userProfileURL}
                            placeholder={$_('settingsPage.generalPreferences.vintedProfilePlaceholder')}
                            class="block w-full flex-1 rounded-md border border-gray-300 px-3 py-2 focus:border-purple-500 focus:outline-none focus:ring-purple-500"
                        />
                    </div>
                </div>
            </div>
        </div>
 
        <div class="rounded-lg bg-white p-6 shadow">
            <div class="mb-6 flex items-center border-b pb-4">
                <Mail class="mr-2 h-5 w-5 text-purple-600" />
                <h2 class="text-xl font-semibold text-gray-900">{$_('settingsPage.emailConfig.title')}</h2>
            </div>

            <div class="space-y-4">
                <div class="grid grid-cols-2 gap-4">
                    <div>
                        <p class="block text-sm font-medium text-gray-700">{$_('settingsPage.emailConfig.imapServer')}</p>
                        <input
                            type="text"
                            bind:value={settings.emailSettings.host}
                            placeholder={$_('settingsPage.emailConfig.imapServerPlaceholder')}
                            class="mt-1 block w-full rounded-md border border-gray-300 px-3 py-2 shadow-sm focus:border-purple-500 focus:outline-none focus:ring-purple-500"
                        />
                    </div>
                    <div>
                        <p class="block text-sm font-medium text-gray-700">{$_('settingsPage.emailConfig.port')}</p>
                        <input
                            type="text"
                            bind:value={settings.emailSettings.port}
                            placeholder={$_('settingsPage.emailConfig.portPlaceholder')}
                            class="mt-1 block w-full rounded-md border border-gray-300 px-3 py-2 shadow-sm focus:border-purple-500 focus:outline-none focus:ring-purple-500"
                        />
                    </div>
                </div>

                <div>
                    <p class="block text-sm font-medium text-gray-700">{$_('settingsPage.emailConfig.email')}</p>
                    <input
                        type="email"
                        bind:value={settings.emailSettings.username}
                        placeholder={$_('settingsPage.emailConfig.emailPlaceholder')}
                        class="mt-1 block w-full rounded-md border border-gray-300 px-3 py-2 shadow-sm focus:border-purple-500 focus:outline-none focus:ring-purple-500"
                    />
                </div>

                <div>
                    <p class="block text-sm font-medium text-gray-700">{$_('settingsPage.emailConfig.password')}</p>
                    <input
                        type="password"
                        bind:value={settings.emailSettings.password}
                        placeholder={$_('settingsPage.emailConfig.passwordPlaceholder')}
                        class="mt-1 block w-full rounded-md border border-gray-300 px-3 py-2 shadow-sm focus:border-purple-500 focus:outline-none focus:ring-purple-500"
                    />
                </div>
            </div>
        </div>
 
        <div class="rounded-lg bg-white p-6 shadow md:col-span-2">
            <div class="mb-6 flex items-center border-b pb-4">
                <Shield class="mr-2 h-5 w-5 text-purple-600" />
                <h2 class="text-xl font-semibold text-gray-900">{$_('settingsPage.vintedToken.title')}</h2>
                <p class="mt-2 text-sm text-gray-500 ml-2">
                    {$_('settingsPage.vintedToken.description')}
                </p>
            </div>

            <div class="space-y-4">
                <div>
                    <p class="block text-sm font-medium text-gray-700">{$_('settingsPage.vintedToken.accessToken')}</p>
                    <div class="mt-1 flex rounded-md shadow-sm">
                        <input
                            bind:value={settings.vintedAccessToken}
                            placeholder={$_('settingsPage.vintedToken.accessTokenPlaceholder')}
                            class="block w-full flex-1 rounded-md border border-gray-300 px-3 py-2 focus:border-purple-500 focus:outline-none focus:ring-purple-500"
                        />
                    </div>
                </div>
                <div>
                    <p class="block text-sm font-medium text-gray-700">{$_('settingsPage.vintedToken.refreshToken')}</p>
                    <div class="mt-1 flex rounded-md shadow-sm">
                        <input
                            bind:value={settings.vintedRefreshToken}
                            placeholder={$_('settingsPage.vintedToken.refreshTokenPlaceholder')}
                            class="block w-full flex-1 rounded-md border border-gray-300 px-3 py-2 focus:border-purple-500 focus:outline-none focus:ring-purple-500"
                        />
                    </div>
                    <button
                        on:click={saveToken}
                        class="mt-4 inline-flex w-full items-center justify-center rounded-md bg-purple-600 px-4 py-2 text-sm font-medium text-white hover:bg-purple-700 focus:outline-none focus:ring-2 focus:ring-purple-500 focus:ring-offset-2"
                    >
                        {$_('settingsPage.vintedToken.saveTokensButton')}
                    </button>
                </div>
            </div>
        </div>
    </div>
</div>
