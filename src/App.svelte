<script>
import { onMount } from 'svelte';
import { getData } from './printfulAPI.js';

let events = [];
console.log(events);
onMount(async () => events = await getData());
</script>

<events />
