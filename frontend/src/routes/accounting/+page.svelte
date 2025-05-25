<script>
  import { Mail, Trash2, AlertCircle, MessageSquare, Printer, Star, Settings2 } from 'lucide-svelte';

  let showAlert = true;
  let monthsToKeep = 2;
  let autoMessage = "Merci pour votre achat ! N'oubliez pas de laisser un avis 😊";
</script>

<div class="mx-auto max-w-7xl px-4 py-8">
  <div class="mb-8 flex items-center justify-between">
    <h1 class="text-3xl font-bold text-gray-900">Secrétariat</h1>
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
            <p>Certaines fonctionnalités nécessitent votre token Vinted et/ou vos identifiants IMAP. Configurez-les dans les <a href="/settings" class="font-medium text-yellow-800 underline hover:text-yellow-900">paramètres</a>.</p>
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
    <!-- Gestion des Mails -->
    <div class="rounded-lg bg-white p-6 shadow">
      <div class="mb-4">
        <div class="flex items-center text-lg font-medium text-gray-900">
          <Mail class="mr-2 h-6 w-6 text-purple-600" />
          <h2>Gestion des Mails</h2>
        </div>
        <div class="mt-2 flex flex-wrap gap-2">
          <div class="inline-flex items-center rounded-full bg-blue-100 px-2.5 py-0.5 text-xs font-medium text-blue-800">
            <Settings2 class="mr-1 h-3 w-3" />
            Token Vinted requis
          </div>
          <div class="inline-flex items-center rounded-full bg-green-100 px-2.5 py-0.5 text-xs font-medium text-green-800">
            <Mail class="mr-1 h-3 w-3" />
            IMAP requis
          </div>
        </div>
      </div>

      <div class="space-y-4">
        <div>
          <p class="mb-2 text-sm font-medium text-gray-700">Message de remerciement</p>
          <textarea
            bind:value={autoMessage}
            rows="3"
            class="block w-full rounded-md border border-gray-300 px-3 py-2 shadow-sm focus:border-purple-500 focus:outline-none focus:ring-purple-500"
            placeholder="Message à inclure dans le colis..."
          ></textarea>
        </div>

        <div class="grid grid-cols-2 gap-3">
          <button class="inline-flex items-center justify-center space-x-2 rounded-md bg-purple-600 px-4 py-2 text-sm font-medium text-white transition-colors hover:bg-purple-700 focus:outline-none focus:ring-2 focus:ring-purple-500 focus:ring-offset-2">
            <Mail class="h-4 w-4" />
            <span>Traiter les mails</span>
          </button>
          <button class="inline-flex items-center justify-center space-x-2 rounded-md border border-purple-600 px-4 py-2 text-sm font-medium text-purple-600 transition-colors hover:bg-purple-50 focus:outline-none focus:ring-2 focus:ring-purple-500 focus:ring-offset-2">
            <Printer class="h-4 w-4" />
            <span>Imprimer bordereaux</span>
          </button>
        </div>
      </div>
    </div>

    <!-- Gestion des Conversations -->
    <div class="rounded-lg bg-white p-6 shadow">
      <div class="mb-4">
        <div class="flex items-center text-lg font-medium text-gray-900">
          <MessageSquare class="mr-2 h-6 w-6 text-purple-600" />
          <h2>Gestion des Conversations</h2>
        </div>
        <div class="mt-2">
          <div class="inline-flex items-center rounded-full bg-blue-100 px-2.5 py-0.5 text-xs font-medium text-blue-800">
            <Settings2 class="mr-1 h-3 w-3" />
            Token Vinted requis
          </div>
        </div>
      </div>

      <div class="space-y-4">
        <div>
          <p class="mb-2 text-sm font-medium text-gray-700">Supprimer les conversations plus anciennes que</p>
          <div class="flex items-center space-x-2">
            <input
              type="number"
              bind:value={monthsToKeep}
              min="1"
              max="12"
              class="block w-20 rounded-md border border-gray-300 px-3 py-2 shadow-sm focus:border-purple-500 focus:outline-none focus:ring-purple-500"
            />
            <span class="text-sm text-gray-600">mois</span>
          </div>
        </div>

        <div>
          <p class="mb-2 text-sm font-medium text-gray-700">Évaluation automatique</p>
          <textarea
            rows="2"
            class="block w-full rounded-md border border-gray-300 px-3 py-2 shadow-sm focus:border-purple-500 focus:outline-none focus:ring-purple-500"
            placeholder="Message d'évaluation personnalisé..."
          ></textarea>
        </div>

        <div class="grid grid-cols-2 gap-3">
          <button class="inline-flex items-center justify-center space-x-2 rounded-md bg-purple-600 px-4 py-2 text-sm font-medium text-white transition-colors hover:bg-purple-700 focus:outline-none focus:ring-2 focus:ring-purple-500 focus:ring-offset-2">
            <Star class="h-4 w-4" />
            <span>Évaluer</span>
          </button>
          <button class="inline-flex items-center justify-center space-x-2 rounded-md border border-red-600 px-4 py-2 text-sm font-medium text-red-600 transition-colors hover:bg-red-50 focus:outline-none focus:ring-2 focus:ring-red-500 focus:ring-offset-2">
            <Trash2 class="h-4 w-4" />
            <span>Nettoyer</span>
          </button>
        </div>
      </div>
    </div>
  </div>
</div>
