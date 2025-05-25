<script lang="ts">
	import '../app.css';
	import Navbar from '$lib/components/Navbar.svelte';
	let { children } = $props();
</script>

<div class="min-h-screen bg-gray-50">
	<Navbar />
	{@render children()}
</div>
