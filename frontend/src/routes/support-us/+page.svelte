<script>
  import { 
    HeartIcon, 
    CreditCardIcon,
    GiftIcon,
    CopyIcon,
    CheckIcon
  } from '@lucide/svelte';
  import { _ } from 'svelte-i18n';

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
      <h2 class="text-xl font-semibold">{$_('supportUsPage.title')}</h2>
    </div>
    
    <p class="text-gray-600">
      {$_('supportUsPage.description')}
    </p>
  </div>

  <!-- Coupert -->
  <div class="mb-6 rounded-lg bg-white p-6 shadow">
    <div class="mb-4 flex items-center justify-between">
      <h3 class="text-lg font-medium text-gray-900">{$_('supportUsPage.coupert.title')}</h3>
      <span class="rounded-full bg-green-100 px-3 py-1 text-sm font-medium text-green-800">{$_('supportUsPage.coupert.offer')}</span>
    </div>
    
    <p class="mb-4 text-gray-600">
      {$_('supportUsPage.coupert.description')}
    </p>
    
    <a 
      href="https://www.coupert.com?invite_code=4822D6&inviter_source=web5"
      target="_blank"
      rel="noopener noreferrer"
      class="inline-flex items-center rounded-md bg-purple-600 px-4 py-2 text-sm font-medium text-white hover:bg-purple-700"
    >
      <GiftIcon class="mr-2 h-4 w-4" />
      {$_('supportUsPage.coupert.button')}
    </a>
  </div>

  <!-- Boursorama -->
  <div class="rounded-lg bg-white p-6 shadow">
    <div class="mb-4 flex items-center justify-between">
      <h3 class="text-lg font-medium text-gray-900">{$_('supportUsPage.boursorama.title')}</h3>
      <span class="rounded-full bg-green-100 px-3 py-1 text-sm font-medium text-green-800">{$_('supportUsPage.boursorama.offer')}</span>
    </div>
    
    <ul class="mb-4 list-inside list-disc text-gray-600">
      {#each $_('supportUsPage.boursorama.benefits') as benefit}
        <li>{benefit}</li>
      {/each}
    </ul>
    
    <div class="flex items-center gap-4">
      <a 
        href="https://www.boursobank.com/landing/parrainage?code_parrain=AURO2755"
        target="_blank"
        rel="noopener noreferrer"
        class="inline-flex items-center rounded-md bg-purple-600 px-4 py-2 text-sm font-medium text-white hover:bg-purple-700"
      >
        <CreditCardIcon class="mr-2 h-4 w-4" />
        {$_('supportUsPage.boursorama.openAccountButton')}
      </a>

      <button
        on:click={copyToClipboard}
        class="inline-flex items-center rounded-md border border-gray-300 px-4 py-2 text-sm font-medium text-gray-700 hover:bg-gray-50"
      >
        {#if codeCopied}
          <CheckIcon class="mr-2 h-4 w-4 text-green-500" />
          {$_('supportUsPage.boursorama.codeCopied')}
        {:else}
          <CopyIcon class="mr-2 h-4 w-4" />
          {$_('supportUsPage.boursorama.copyCodeButton')}
        {/if}
      </button>
    </div>
  </div>
</div>

