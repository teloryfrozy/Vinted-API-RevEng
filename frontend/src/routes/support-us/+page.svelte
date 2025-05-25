<script>
  import { 
    HeartIcon, 
    CreditCardIcon,
    GiftIcon,
    CopyIcon,
    CheckIcon
  } from 'lucide-svelte';

  let codeCopied = false;

  const copyToClipboard = async () => {
    try {
      await navigator.clipboard.writeText('AURO2755');
      codeCopied = true;
      setTimeout(() => codeCopied = false, 2000);
    } catch (err) {
      console.error('Failed to copy text: ', err);
    }
  };
</script>

<div class="mx-auto max-w-4xl px-4 py-8">
  <div class="mb-8 rounded-lg bg-white p-6 shadow">
    <div class="mb-4 flex items-center">
      <HeartIcon class="mr-2 h-6 w-6 text-purple-600" />
      <h2 class="text-xl font-semibold">Nous Soutenir</h2>
    </div>
    
    <p class="text-gray-600">
      C'est une app de logistique qu'on a développée pour notre business Vinted il y a 2 ans, à côté de nos études. Si elle vous est utile, vous pouvez nous soutenir via ces offres avantageuses !
    </p>
  </div>

  <!-- Coupert -->
  <div class="mb-6 rounded-lg bg-white p-6 shadow">
    <div class="mb-4 flex items-center justify-between">
      <h3 class="text-lg font-medium text-gray-900">Coupert</h3>
      <span class="rounded-full bg-green-100 px-3 py-1 text-sm font-medium text-green-800">10€ offerts</span>
    </div>
    
    <p class="mb-4 text-gray-600">
      Extension qui trouve automatiquement les meilleurs codes promo. Gagnez 10€ en créant un compte et en dépensant 30€ sur l'un des 15 000 sites partenaires.
    </p>
    
    <a 
      href="https://www.coupert.com/ref/ju51oa"
      target="_blank"
      rel="noopener noreferrer"
      class="inline-flex items-center rounded-md bg-purple-600 px-4 py-2 text-sm font-medium text-white hover:bg-purple-700"
    >
      <GiftIcon class="mr-2 h-4 w-4" />
      Profiter de l'offre
    </a>
  </div>

  <!-- Boursorama -->
  <div class="rounded-lg bg-white p-6 shadow">
    <div class="mb-4 flex items-center justify-between">
      <h3 class="text-lg font-medium text-gray-900">Boursorama Banque</h3>
      <span class="rounded-full bg-green-100 px-3 py-1 text-sm font-medium text-green-800">Jusqu'à 170€ offerts</span>
    </div>
    
    <ul class="mb-4 list-inside list-disc text-gray-600">
      <li>80€ à 120€ de prime de bienvenue</li>
      <li>50€ supplémentaires avec EasyMove</li>
      <li>Carte bancaire gratuite avec 1 utilisation par mois (sinon 5€)</li>
    </ul>
    
    <div class="flex items-center gap-4">
      <a 
        href="https://bour.so/FHnn31mt9L"
        target="_blank"
        rel="noopener noreferrer"
        class="inline-flex items-center rounded-md bg-purple-600 px-4 py-2 text-sm font-medium text-white hover:bg-purple-700"
      >
        <CreditCardIcon class="mr-2 h-4 w-4" />
        Ouvrir un compte
      </a>

      <button
        on:click={copyToClipboard}
        class="inline-flex items-center rounded-md border border-gray-300 px-4 py-2 text-sm font-medium text-gray-700 hover:bg-gray-50"
      >
        {#if codeCopied}
          <CheckIcon class="mr-2 h-4 w-4 text-green-500" />
          Code copié !
        {:else}
          <CopyIcon class="mr-2 h-4 w-4" />
          Copier le code AURO2755
        {/if}
      </button>
    </div>
  </div>
</div>

