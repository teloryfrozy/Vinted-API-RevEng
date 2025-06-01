<script>
    import {
        ShoppingBagIcon,
        MailCheckIcon,
        ArrowUpCircleIcon,
        CopyIcon,
        Trash2Icon,
        UsersRound,
        SaveIcon,
        NetworkIcon,
        MailIcon,
        InboxIcon,
        MessageSquareIcon,
        LightbulbIcon,
        CameraIcon,
        FileTextIcon,
        HeartHandshakeIcon,
    } from "@lucide/svelte";
</script>

<div class="mx-auto max-w-7xl px-4 py-12">
    <h1 class="mb-12 text-center text-4xl font-bold text-gray-900">Vinted Automation Tools</h1>

    <div class="grid gap-8">
        <a
            href="/ads-management"
            class="group relative overflow-hidden rounded-xl bg-white p-8 shadow-md transition-all hover:-translate-y-1 hover:shadow-xl"
        >
            <div
                class="absolute right-0 top-0 h-32 w-32 translate-x-8 translate-y-[-50%] transform opacity-5 transition-transform group-hover:translate-x-4"
            >
                <ShoppingBagIcon class="h-full w-full" />
            </div>
            <div class="relative">
                <div class="mb-6 flex items-center">
                    <ShoppingBagIcon class="mr-3 h-8 w-8 text-purple-600" />
                    <h2 class="text-2xl font-semibold text-gray-900 group-hover:text-purple-600">Gérer les annonces</h2>
                </div>
                <div class="grid gap-4 md:grid-cols-3">
                    <div class="flex items-start space-x-3">
                        <ArrowUpCircleIcon class="mt-0.5 h-5 w-5 flex-shrink-0 text-purple-500" />
                        <p class="text-sm text-gray-600">Remonter vos annonces en tête de liste</p>
                    </div>
                    <div class="flex items-start space-x-3">
                        <CopyIcon class="mt-0.5 h-5 w-5 flex-shrink-0 text-purple-500" />
                        <p class="text-sm text-gray-600">Automatiser la vente de vos doublons</p>
                    </div>
                    <div class="flex items-start space-x-3">
                        <Trash2Icon class="mt-0.5 h-5 w-5 flex-shrink-0 text-purple-500" />
                        <p class="text-sm text-gray-600">Supprimer vos articles vendus</p>
                    </div>
                </div>
            </div>
        </a>

        <a
            href="/follow-mass"
            class="group relative overflow-hidden rounded-xl bg-white p-8 shadow-md transition-all hover:-translate-y-1 hover:shadow-xl"
        >
            <div
                class="absolute right-0 top-0 h-32 w-32 translate-x-8 translate-y-[-50%] transform opacity-5 transition-transform group-hover:translate-x-4"
            >
                <UsersRound class="h-full w-full" />
            </div>
            <div class="relative">
                <div class="mb-6 flex items-center">
                    <UsersRound class="mr-3 h-8 w-8 text-purple-600" />
                    <h2 class="text-2xl font-semibold text-gray-900 group-hover:text-purple-600">Follow Mass</h2>
                </div>
                <div class="grid gap-4 md:grid-cols-3">
                    <div class="flex items-start space-x-3">
                        <UsersRound class="mt-0.5 h-5 w-5 flex-shrink-0 text-purple-500" />
                        <p class="text-sm text-gray-600">Suivez des dizaines d'utilisateurs en un clic</p>
                    </div>
                    <div class="flex items-start space-x-3">
                        <SaveIcon class="mt-0.5 h-5 w-5 flex-shrink-0 text-purple-500" />
                        <p class="text-sm text-gray-600">Sauvegarde d'abonnements automatique</p>
                    </div>
                    <div class="flex items-start space-x-3">
                        <NetworkIcon class="mt-0.5 h-5 w-5 flex-shrink-0 text-purple-500" />
                        <p class="text-sm text-gray-600">Augmentez vos relations</p>
                    </div>
                </div>
            </div>
        </a>

        <a
            href="/accounting"
            class="group relative overflow-hidden rounded-xl bg-white p-8 shadow-md transition-all hover:-translate-y-1 hover:shadow-xl"
        >
            <div
                class="absolute right-0 top-0 h-32 w-32 translate-x-8 translate-y-[-50%] transform opacity-5 transition-transform group-hover:translate-x-4"
            >
                <MailCheckIcon class="h-full w-full" />
            </div>
            <div class="relative">
                <div class="mb-6 flex items-center">
                    <MailCheckIcon class="mr-3 h-8 w-8 text-purple-600" />
                    <h2 class="text-2xl font-semibold text-gray-900 group-hover:text-purple-600">Secrétariat</h2>
                </div>
                <div class="grid gap-4 md:grid-cols-3">
                    <div class="flex items-start space-x-3">
                        <MailIcon class="mt-0.5 h-5 w-5 flex-shrink-0 text-purple-500" />
                        <p class="text-sm text-gray-600">Paramétrer la gestion de vos mails</p>
                    </div>
                    <div class="flex items-start space-x-3">
                        <InboxIcon class="mt-0.5 h-5 w-5 flex-shrink-0 text-purple-500" />
                        <p class="text-sm text-gray-600">Trier vos mails de manière passive</p>
                    </div>
                    <div class="flex items-start space-x-3">
                        <MessageSquareIcon class="mt-0.5 h-5 w-5 flex-shrink-0 text-purple-500" />
                        <p class="text-sm text-gray-600">Supprimer vos anciennes conversations</p>
                    </div>
                </div>
            </div>
        </a>

        <a
            href="/help"
            class="group relative overflow-hidden rounded-xl bg-white p-8 shadow-md transition-all hover:-translate-y-1 hover:shadow-xl"
        >
            <div
                class="absolute right-0 top-0 h-32 w-32 translate-x-8 translate-y-[-50%] transform opacity-5 transition-transform group-hover:translate-x-4"
            >
                <LightbulbIcon class="h-full w-full" />
            </div>
            <div class="relative">
                <div class="mb-6 flex items-center">
                    <LightbulbIcon class="mr-3 h-8 w-8 text-yellow-500" />
                    <h2 class="text-2xl font-semibold text-gray-900 group-hover:text-yellow-500">Conseils de Vente</h2>
                </div>
                <div class="grid gap-4 md:grid-cols-3">
                    <div class="flex items-start space-x-3">
                        <CameraIcon class="mt-0.5 h-5 w-5 flex-shrink-0 text-yellow-500" />
                        <p class="text-sm text-gray-600">Rédiger une annonce qui vend</p>
                    </div>
                    <div class="flex items-start space-x-3">
                        <FileTextIcon class="mt-0.5 h-5 w-5 flex-shrink-0 text-yellow-500" />
                        <p class="text-sm text-gray-600">Notre expérience de vendeur sur Vinted</p>
                    </div>
                    <div class="flex items-start space-x-3">
                        <HeartHandshakeIcon class="mt-0.5 h-5 w-5 flex-shrink-0 text-yellow-500" />
                        <p class="text-sm text-gray-600">Expérience acheteur personnalisée</p>
                    </div>
                </div>
            </div>
        </a>
    </div>
</div>
