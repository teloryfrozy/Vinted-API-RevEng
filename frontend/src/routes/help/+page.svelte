<script>
    import { CameraIcon, FileTextIcon, UsersRound, HeartHandshakeIcon, HistoryIcon } from "@lucide/svelte";
    import { _ } from 'svelte-i18n';

    let activeTab = "tips";
</script>

<div class="mx-auto max-w-7xl px-4 py-8">
    <h1 class="mb-8 text-3xl font-bold text-gray-900">{$_('helpPage.title')}</h1>

    <div class="mb-8 flex border-b">
        <button
            class="mr-4 border-b-2 px-4 py-2 {activeTab === 'tips'
                ? 'border-purple-600 text-purple-600'
                : 'border-transparent text-gray-500 hover:text-gray-700'}"
            on:click={() => (activeTab = "tips")}
        >
            {$_('helpPage.tabs.tips')}
        </button>
        <button
            class="border-b-2 px-4 py-2 {activeTab === 'story'
                ? 'border-purple-600 text-purple-600'
                : 'border-transparent text-gray-500 hover:text-gray-700'}"
            on:click={() => (activeTab = "story")}
        >
            {$_('helpPage.tabs.story')}
        </button>
    </div>

    {#if activeTab === "tips"}
        <div class="grid gap-6 md:grid-cols-2">
            <div class="rounded-lg bg-white p-6 shadow">
                <div class="mb-4 flex items-center">
                    <CameraIcon class="mr-2 h-6 w-6 text-purple-600" />
                    <h2 class="text-xl font-semibold">{$_('helpPage.tips.photos.title')}</h2>
                </div>
                <div class="space-y-2 text-gray-600">
                    <p>{$_('helpPage.tips.photos.description')}</p>
                    <p>{$_('helpPage.tips.photos.qualityTitle')}</p>
                    <ul class="list-inside list-disc pl-4">
                        {#each $_('helpPage.tips.photos.benefits') as benefit}
                            <li>{benefit}</li>
                        {/each}
                    </ul>
                </div>
            </div>
            <div class="rounded-lg bg-white p-6 shadow">
                <div class="mb-4 flex items-center">
                    <FileTextIcon class="mr-2 h-6 w-6 text-purple-600" />
                    <h2 class="text-xl font-semibold">{$_('helpPage.tips.description.title')}</h2>
                </div>
                <div class="space-y-2 text-gray-600">
                    <p>{$_('helpPage.tips.description.keyTitle')}</p>
                    <ul class="list-inside list-disc pl-4">
                        {#each $_('helpPage.tips.description.tips') as tip}
                            <li>{tip}</li>
                        {/each}
                    </ul>
                    <p>{$_('helpPage.tips.description.conclusion')}</p>
                </div>
            </div>
            <div class="rounded-lg bg-white p-6 shadow">
                <div class="mb-4 flex items-center">
                    <UsersRound class="mr-2 h-6 w-6 text-purple-600" />
                    <h2 class="text-xl font-semibold">{$_('helpPage.tips.followers.title')}</h2>
                </div>
                <div class="space-y-2 text-gray-600">
                    <p>{$_('helpPage.tips.followers.description')}</p>
                    <ul class="list-inside list-disc pl-4">
                        {#each $_('helpPage.tips.followers.tips') as tip}
                            <li>{tip}</li>
                        {/each}
                    </ul>
                    <p class="mt-2 text-sm italic">{$_('helpPage.tips.followers.conclusion')}</p>
                </div>
            </div>
            <div class="rounded-lg bg-white p-6 shadow">
                <div class="mb-4 flex items-center">
                    <HeartHandshakeIcon class="mr-2 h-6 w-6 text-purple-600" />
                    <h2 class="text-xl font-semibold">{$_('helpPage.tips.thanks.title')}</h2>
                </div>
                <div class="space-y-2 text-gray-600">
                    <p>{$_('helpPage.tips.thanks.description')}</p>
                    <ul class="list-inside list-disc pl-4">
                        {#each $_('helpPage.tips.thanks.tips') as tip}
                            <li>{tip}</li>
                        {/each}
                    </ul>
                    <p class="mt-2 text-sm italic">{$_('helpPage.tips.thanks.conclusion')}</p>
                </div>
            </div>
        </div>
    {/if}

    {#if activeTab === "story"}
        <div class="rounded-lg bg-white p-6 shadow">
            <div class="mb-6 flex items-center">
                <HistoryIcon class="mr-2 h-6 w-6 text-purple-600" />
                <h2 class="text-xl font-semibold">{$_('helpPage.story.title')}</h2>
            </div>

            <div class="prose prose-sm max-w-none text-gray-600">
                <p class="mb-4">
                    {$_('helpPage.story.intro')}
                </p>

                <ul class="mb-4 list-disc pl-5">
                    {#each $_('helpPage.story.challenges') as challenge}
                        <li>{challenge}</li>
                    {/each}
                </ul>

                <p class="mb-4">
                    {$_('helpPage.story.conclusion')}
                </p>

                <div class="mt-8 space-y-6">
                    <div class="rounded-lg bg-gray-50 p-4">
                        <h3 class="mb-2 text-lg font-semibold text-purple-600">{$_('helpPage.story.tips.verification.title')}</h3>
                        <p>
                            {$_('helpPage.story.tips.verification.content')}
                        </p>
                    </div>

                    <div class="rounded-lg bg-gray-50 p-4">
                        <h3 class="mb-2 text-lg font-semibold text-purple-600">{$_('helpPage.story.tips.ban.title')}</h3>
                        <p>
                            {$_('helpPage.story.tips.ban.content')}
                        </p>
                    </div>
                </div>
            </div>
        </div>
    {/if}
</div>
