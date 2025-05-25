<script>
  import { 
    CameraIcon, 
    FileTextIcon, 
    Users2Icon, 
    HeartHandshakeIcon, 
    LightbulbIcon, 
    HistoryIcon,
    ListIcon,
    SmileIcon,
    UsersIcon,
    StarIcon
  } from '@lucide/svelte';

  let activeTab = 'tips';
</script>

<div class="mx-auto max-w-7xl px-4 py-8">
  <h1 class="mb-8 text-3xl font-bold text-gray-900">Guide et Conseils</h1>

  <!-- Tabs Navigation -->
  <div class="mb-8 flex border-b">
    <button
      class="mr-4 border-b-2 px-4 py-2 {activeTab === 'tips' ? 'border-purple-600 text-purple-600' : 'border-transparent text-gray-500 hover:text-gray-700'}"
      on:click={() => activeTab = 'tips'}
    >
      Astuces de Vente
    </button>
    <button
      class="border-b-2 px-4 py-2 {activeTab === 'story' ? 'border-purple-600 text-purple-600' : 'border-transparent text-gray-500 hover:text-gray-700'}"
      on:click={() => activeTab = 'story'}
    >
      Mon Parcours
    </button>
  </div>

  <!-- Tips Content -->
  {#if activeTab === 'tips'}
    <div class="grid gap-6 md:grid-cols-2">
      <!-- Photos -->
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

      <!-- Description -->
      <div class="rounded-lg bg-white p-6 shadow">
        <div class="mb-4 flex items-center">
          <FileTextIcon class="mr-2 h-6 w-6 text-purple-600" />
          <h2 class="text-xl font-semibold">Description</h2>
        </div>
        <div class="space-y-2 text-gray-600">
          <p>La clé d'une bonne description :</p>
          <ul class="list-inside list-disc pl-4">
            <li>Texte simple et structuré en liste</li>
            <li>Utilisation d'émojis pour plus de dynamisme <SmileIcon class="inline h-4 w-4" /></li>
            <li>Informations claires et précises</li>
          </ul>
          <p>Une description soignée reflète la qualité de vos articles.</p>
        </div>
      </div>

      <!-- Followers -->
      <div class="rounded-lg bg-white p-6 shadow">
        <div class="mb-4 flex items-center">
          <Users2Icon class="mr-2 h-6 w-6 text-purple-600" />
          <h2 class="text-xl font-semibold">Followers</h2>
        </div>
        <div class="space-y-2 text-gray-600">
          <p>Développez votre réseau :</p>
          <ul class="list-inside list-disc pl-4">
            <li>Suivez d'autres vendeurs activement</li>
            <li>Gagnez en visibilité grâce aux abonnés</li>
            <li>Utilisez Follow Mass pour automatiser ce processus</li>
          </ul>
          <p class="mt-2 text-sm italic">Plus d'abonnés = Plus de crédibilité</p>
        </div>
      </div>

      <!-- Remerciements -->
      <div class="rounded-lg bg-white p-6 shadow">
        <div class="mb-4 flex items-center">
          <HeartHandshakeIcon class="mr-2 h-6 w-6 text-purple-600" />
          <h2 class="text-xl font-semibold">Remerciements</h2>
        </div>
        <div class="space-y-2 text-gray-600">
          <p>Personnalisez l'expérience client :</p>
          <ul class="list-inside list-disc pl-4">
            <li>Ajoutez un message manuscrit dans le colis</li>
            <li>Créez une relation personnelle avec l'acheteur</li>
            <li>Encouragez les retours positifs et le bouche-à-oreille</li>
          </ul>
          <p class="mt-2 text-sm italic">Un client satisfait reviendra et parlera de vous !</p>
        </div>
      </div>
    </div>
  {/if}

  <!-- Story Content -->
  {#if activeTab === 'story'}
    <div class="rounded-lg bg-white p-6 shadow">
      <div class="mb-6 flex items-center">
        <HistoryIcon class="mr-2 h-6 w-6 text-purple-600" />
        <h2 class="text-xl font-semibold">Mon Expérience Vinted</h2>
      </div>
      
      <div class="prose prose-sm max-w-none text-gray-600">
        <p class="mb-4">
          J'ai commencé par la vente de PC customisés avant de me lancer dans la revente de consoles de jeux sur Vinted. Cette expérience m'a permis de réaliser un chiffre d'affaires de 15k€, mais m'a aussi confronté à plusieurs défis :
        </p>
        
        <ul class="mb-4 list-disc pl-5">
          <li>Gestion chronophage des messages et des envois</li>
          <li>Complexités administratives et fiscales</li>
          <li>Blocages temporaires de fonds</li>
        </ul>

        <p>
          Ces challenges m'ont poussé à développer des outils d'automatisation pour optimiser le processus de vente. Aujourd'hui, je partage cette application pour aider d'autres vendeurs à être plus efficaces.
        </p>
      </div>
    </div>
  {/if}
</div>

