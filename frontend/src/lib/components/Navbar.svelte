<script>
  import { Home, Heart, Github, Settings } from 'lucide-svelte';
</script>

<nav class="bg-white shadow-lg">
  <div class="mx-auto max-w-7xl px-4">
    <div class="flex h-16 justify-between">
      <div class="flex">
        <!-- Logo/Home -->
        <div class="flex items-center">
          <a href="/" class="flex items-center space-x-2">
            <Home class="h-8 w-8 text-purple-600" />
            <span class="text-xl font-semibold">Vinted Tools</span>
          </a>
        </div>
      </div>

      <!-- Navigation Links -->
      <div class="flex items-center space-x-4">
        <!-- Sponsor Button -->
        <a 
          href="/support-us" 
          class="inline-flex items-center space-x-2 rounded-md bg-purple-600 px-4 py-2 text-sm font-medium text-white transition-colors hover:bg-purple-700 focus:outline-none focus:ring-2 focus:ring-purple-500 focus:ring-offset-2"
        >
          <Heart class="h-5 w-5" />
          <span>Sponsor</span>
        </a>

        <!-- GitHub Star Button -->
        <a 
          href="https://github.com/your-repo" 
          target="_blank" 
          rel="noopener noreferrer"
          class="inline-flex items-center space-x-2 rounded-md bg-gray-800 px-4 py-2 text-sm font-medium text-white transition-colors hover:bg-gray-700 focus:outline-none focus:ring-2 focus:ring-gray-500 focus:ring-offset-2"
        >
          <Github class="h-5 w-5" />
          <span>Star us</span>
        </a>

        <!-- Settings Button -->
        <a 
          href="/settings" 
          class="inline-flex items-center space-x-2 rounded-md px-4 py-2 text-sm font-medium text-gray-700 transition-colors hover:bg-gray-100 hover:text-purple-600 focus:outline-none focus:ring-2 focus:ring-purple-500 focus:ring-offset-2"
        >
          <Settings class="h-5 w-5" />
          <span>Paramètres</span>
        </a>
      </div>
    </div>
  </div>
</nav> 