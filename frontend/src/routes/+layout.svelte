<script lang="ts">
	import '../app.css';
	import "../i18n/init.ts";
	import Navbar from '../global/components/Navbar.svelte';
	let { children } = $props();
</script>

<div class="min-h-screen bg-gray-50">
	<Navbar />
	{@render children()}
</div>
