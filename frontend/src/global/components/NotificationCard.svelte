<script>
    import { onDestroy } from "svelte";
    import { _ } from 'svelte-i18n';

    export let message = $_('notificationCard.defaultMessage');
    export let type = "success";
    export let visible = true;

    $: status = type === "success" ? "success" : "error";

    const timer = setTimeout(() => {
        visible = false;
    }, 3000);

    onDestroy(() => {
        clearTimeout(timer);
    });
</script>

{#if visible}
    <div
        class={`fixed top-5 right-5 px-6 py-4 rounded-xl shadow-lg text-white text-sm font-medium transition-opacity duration-300 opacity-80
      ${status === "success" ? "bg-green-500" : "bg-red-600"}
    `}
    >
        {message}
    </div>
{/if}
