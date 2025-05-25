 

<script>
  import { Users, AlertCircle, Key, History, Loader2 } from '@lucide/svelte';

  let showAlert = true;
  let isFollowing = false;
  let followCount = 0;
  let targetCount = 50;
</script>

<div class="mx-auto max-w-7xl px-4 py-8">
  <div class="mb-8 flex items-center justify-between">
    <h1 class="text-3xl font-bold text-gray-900">Suivi en Masse</h1>
  </div>

  {#if showAlert}
    <div class="mb-6 rounded-md bg-yellow-50 p-4">
      <div class="flex">
        <div class="flex-shrink-0">
          <AlertCircle class="h-5 w-5 text-yellow-400" />
        </div>
        <div class="ml-3">
          <h3 class="text-sm font-medium text-yellow-800">Configuration requise</h3>
          <div class="mt-2 text-sm text-yellow-700">
            <p>Cette fonctionnalité nécessite votre token Vinted. Configurez-le dans les <a href="/settings" class="font-medium text-yellow-800 underline hover:text-yellow-900">paramètres</a>.</p>
          </div>
        </div>
        <div class="ml-auto pl-3">
          <div class="-mx-1.5 -my-1.5">
            <button
              type="button"
              on:click={() => showAlert = false}
              class="inline-flex rounded-md bg-yellow-50 p-1.5 text-yellow-500 hover:bg-yellow-100"
            >
              <span class="sr-only">Dismiss</span>
              <svg class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                <path d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" />
              </svg>
            </button>
          </div>
        </div>
      </div>
    </div>
  {/if}

  <div class="grid gap-6 md:grid-cols-2">
    <!-- Configuration du Suivi -->
    <div class="rounded-lg bg-white p-6 shadow">
      <div class="mb-4">
        <div class="flex items-center text-lg font-medium text-gray-900">
          <Users class="mr-2 h-6 w-6 text-purple-600" />
          <h2>Suivi Automatique</h2>
        </div>
        <div class="mt-2">
          <div class="inline-flex items-center rounded-full bg-blue-100 px-2.5 py-0.5 text-xs font-medium text-blue-800">
            <Key class="mr-1 h-3 w-3" />
            Token Vinted requis
          </div>
        </div>
      </div>

      <div class="mb-6 space-y-4">
        <div>
          <p class="mb-1 block text-sm font-medium text-gray-700">Nombre d'utilisateurs à suivre</p>
          <input
            type="number"
            bind:value={targetCount}
            min="1"
            max="100"
            class="block w-full rounded-md border border-gray-300 px-3 py-2 shadow-sm focus:border-purple-500 focus:outline-none focus:ring-purple-500"
          />
        </div>

        {#if isFollowing}
          <div class="rounded-lg bg-gray-50 p-4">
            <div class="flex items-center justify-between">
              <div class="flex items-center">
                <Loader2 class="mr-2 h-5 w-5 animate-spin text-purple-600" />
                <span class="text-sm text-gray-700">Suivi en cours...</span>
              </div>
              <span class="text-sm font-medium text-purple-600">{followCount}/{targetCount}</span>
            </div>
            <div class="mt-2">
              <div class="relative h-2 overflow-hidden rounded-full bg-gray-200">
                <div
                  class="absolute h-full bg-purple-600 transition-all duration-300"
                  style="width: {(followCount / targetCount) * 100}%"
                ></div>
              </div>
            </div>
          </div>
        {/if}

        <button
          class="inline-flex w-full items-center justify-center space-x-2 rounded-md bg-purple-600 px-4 py-2 text-sm font-medium text-white transition-colors hover:bg-purple-700 focus:outline-none focus:ring-2 focus:ring-purple-500 focus:ring-offset-2"
          on:click={() => isFollowing = !isFollowing}
        >
          <Users class="h-5 w-5" />
          <span>{isFollowing ? 'Arrêter' : 'Démarrer'} le suivi</span>
        </button>
      </div>
    </div>

    <!-- Historique -->
    <div class="rounded-lg bg-white p-6 shadow">
      <div class="mb-4 flex items-center text-lg font-medium text-gray-900">
        <History class="mr-2 h-6 w-6 text-purple-600" />
        <h2>Historique des Suivis</h2>
      </div>

      <div class="space-y-4">
        <div class="rounded-lg border border-gray-200 p-4">
          <div class="flex items-center justify-between">
            <div>
              <p class="font-medium text-gray-900">Suivi automatique</p>
              <p class="text-sm text-gray-500">50 utilisateurs suivis</p>
            </div>
            <span class="text-sm text-gray-500">Il y a 2 heures</span>
          </div>
        </div>

        <div class="rounded-lg border border-gray-200 p-4">
          <div class="flex items-center justify-between">
            <div>
              <p class="font-medium text-gray-900">Suivi automatique</p>
              <p class="text-sm text-gray-500">25 utilisateurs suivis</p>
            </div>
            <span class="text-sm text-gray-500">Hier</span>
          </div>
        </div>

        <div class="rounded-lg border border-gray-200 p-4">
          <div class="flex items-center justify-between">
            <div>
              <p class="font-medium text-gray-900">Suivi automatique</p>
              <p class="text-sm text-gray-500">75 utilisateurs suivis</p>
            </div>
            <span class="text-sm text-gray-500">Il y a 2 jours</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>