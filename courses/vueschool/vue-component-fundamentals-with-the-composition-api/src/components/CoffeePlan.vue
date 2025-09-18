<script setup>
import { ref } from "vue";

const props = defineProps({
  name: { type: String, default: "Default Plan" },
  selected: { type: Boolean, default: false },
});
</script>

<template>
  <div
    class="m-8 rounded-sm bg-indigo-600 px-4 py-2 text-l font-semibold text-white shadow-xs hover:bg-indigo-500 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600 dark:bg-indigo-500 dark:shadow-none dark:hover:bg-indigo-400 dark:focus-visible:outline-indigo-500"
    :class="{ 'dark:bg-lime-600 light:bg-lime-600': selected }"
  >
    <div class="description">
      <span class="title">{{ name }} </span>
    </div>
  </div>
</template>
