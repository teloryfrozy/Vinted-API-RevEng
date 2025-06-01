<script>
    import { CameraIcon, FileTextIcon, UsersRound, HeartHandshakeIcon, HistoryIcon } from "@lucide/svelte";

    let activeTab = "tips";
</script>

<div class="mx-auto max-w-7xl px-4 py-8">
    <h1 class="mb-8 text-3xl font-bold text-gray-900">Guide et Conseils</h1>

    <div class="mb-8 flex border-b">
        <button
            class="mr-4 border-b-2 px-4 py-2 {activeTab === 'tips'
                ? 'border-purple-600 text-purple-600'
                : 'border-transparent text-gray-500 hover:text-gray-700'}"
            on:click={() => (activeTab = "tips")}
        >
            Astuces de Vente
        </button>
        <button
            class="border-b-2 px-4 py-2 {activeTab === 'story'
                ? 'border-purple-600 text-purple-600'
                : 'border-transparent text-gray-500 hover:text-gray-700'}"
            on:click={() => (activeTab = "story")}
        >
            Mon Parcours
        </button>
    </div>

    {#if activeTab === "tips"}
        <div class="grid gap-6 md:grid-cols-2">
            <div class="rounded-lg bg-white p-6 shadow">
                <div class="mb-4 flex items-center">
                    <CameraIcon class="mr-2 h-6 w-6 text-purple-600" />
                    <h2 class="text-xl font-semibold">Photos</h2>
                </div>
                <div class="space-y-2 text-gray-600">
                    <p>Prenez des photos de loin car elles apparaissent rognées sur Vinted.</p>
                    <p>Des photos de qualité :</p>
                    <ul class="list-inside list-disc pl-4">
                        <li>Inspirent confiance</li>
                        <li>Montrent le soin apporté aux articles</li>
                        <li>Augmentent les chances de vente</li>
                    </ul>
                </div>
            </div>
            <div class="rounded-lg bg-white p-6 shadow">
                <div class="mb-4 flex items-center">
                    <FileTextIcon class="mr-2 h-6 w-6 text-purple-600" />
                    <h2 class="text-xl font-semibold">Description</h2>
                </div>
                <div class="space-y-2 text-gray-600">
                    <p>La clé d'une bonne description :</p>
                    <ul class="list-inside list-disc pl-4">
                        <li>Texte simple et court</li>
                        <li>Répondre aux questions dans la description</li>
                        <li>Informations claires et précises</li>
                    </ul>
                    <p>Une description soignée reflète la qualité de vos articles.</p>
                </div>
            </div>
            <div class="rounded-lg bg-white p-6 shadow">
                <div class="mb-4 flex items-center">
                    <UsersRound class="mr-2 h-6 w-6 text-purple-600" />
                    <h2 class="text-xl font-semibold">Followers</h2>
                </div>
                <div class="space-y-2 text-gray-600">
                    <p>Développez votre réseau :</p>
                    <ul class="list-inside list-disc pl-4">
                        <li>Gagnez en visibilité grâce à vos abonnés</li>
                        <li>Utilisez Follow Mass pour gagner pleins d'abonnés</li>
                    </ul>
                    <p class="mt-2 text-sm italic">Plus d'abonnés = Plus de visibilité</p>
                </div>
            </div>
            <div class="rounded-lg bg-white p-6 shadow">
                <div class="mb-4 flex items-center">
                    <HeartHandshakeIcon class="mr-2 h-6 w-6 text-purple-600" />
                    <h2 class="text-xl font-semibold">Remerciements</h2>
                </div>
                <div class="space-y-2 text-gray-600">
                    <p>Personnalisez l'expérience client :</p>
                    <ul class="list-inside list-disc pl-4">
                        <li>Ajoutez un message personnalisé dans chaque colis</li> 
                        <li>Essayer toujours de trouver un compromis si problème</li>
                        <li>Si mauvaise note, expliquer en répondant au commentaire</li>
                    </ul>
                    <p class="mt-2 text-sm italic">Un client satisfait peut vous recommander à ses proches</p>
                </div>
            </div>
        </div>
    {/if}

    {#if activeTab === "story"}
        <div class="rounded-lg bg-white p-6 shadow">
            <div class="mb-6 flex items-center">
                <HistoryIcon class="mr-2 h-6 w-6 text-purple-600" />
                <h2 class="text-xl font-semibold">Mon Expérience Vinted</h2>
            </div>

            <div class="prose prose-sm max-w-none text-gray-600">
                <p class="mb-4">
                    J'ai commencé par la vente de PC customisés avant de me lancer dans la revente de consoles de jeux
                    sur Vinted. Cette expérience m'a permis de réaliser un chiffre d'affaires de 15k€, mais m'a aussi
                    confronté à plusieurs défis :
                </p>

                <ul class="mb-4 list-disc pl-5">
                    <li>Gestion chronophage des messages et des envois</li>
                    <li>Complexités administratives et fiscales</li>
                    <li>Blocages temporaires de fonds</li>
                </ul>

                <p class="mb-4">
                    Ces challenges m'ont poussé à développer des outils d'automatisation pour optimiser le processus de
                    vente. Je vous partage cette application pour vous aider gratuitement. N'hésitez pas à contribuer si vous êtes développeur.
                </p>

                <div class="mt-8 space-y-6">
                    <div class="rounded-lg bg-gray-50 p-4">
                        <h3 class="mb-2 text-lg font-semibold text-purple-600">🔍 Vérification status micro-entreprise</h3>
                        <p>
                            À un moment donné, Vinted a bloqué nos retraits d'argent car nous devions prouver notre statut d'entreprise. 
                            Après plusieurs semaines de recherche, j'ai trouvé la solution : le site 
							<a href="https://data.inpi.fr" target="_blank" class="text-purple-600 hover:text-purple-700">data.inpi.fr</a>
							permet d'obtenir gratuitement le document officiel nécessaire. Pas besoin de payer pour des services tiers 
							qui vous ne vous fourniront même pas le bon document !
                        </p>
                    </div>

                    <div class="rounded-lg bg-gray-50 p-4">
                        <h3 class="mb-2 text-lg font-semibold text-purple-600">🚫 Éviter le bannissement</h3>
                        <p>
                            Ce conseil vaut de l'or : ne JAMAIS accepter de paiements hors Vinted, même pour arranger un client qui 
                            veut ajouter des articles à sa commande. Nous avons été bannis pour avoir utilisé PayPal dans ce cas. 
							Je sais que c'est énervant mais il faut toujours annuler la vente si vous devez modifier un lot et créez une nouvelle annonce.
                        </p>
                    </div>
                </div>
            </div>
        </div>
    {/if}
</div>
