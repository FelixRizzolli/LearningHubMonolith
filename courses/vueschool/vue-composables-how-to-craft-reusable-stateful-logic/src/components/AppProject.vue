<template>
  <div
    class="mx-auto max-w-2xl px-4 py-16 sm:px-6 sm:py-24 lg:max-w-7xl lg:px-8"
  >
    <h1 class="text-base font-semibold text-gray-900 dark:text-white">
      {{ state }}
    </h1>
    <button
      @click="prev"
      class="mt-6 rounded-md bg-indigo-600 px-3.5 py-2.5 text-sm font-semibold text-white shadow-xs hover:bg-indigo-500 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600 dark:bg-indigo-500 dark:shadow-none dark:hover:bg-indigo-400 dark:focus-visible:outline-indigo-500"
    >
      Previous
    </button>
    <button
      @click="next"
      class="mt-6 ml-4 rounded-md bg-indigo-600 px-3.5 py-2.5 text-sm font-semibold text-white shadow-xs hover:bg-indigo-500 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600 dark:bg-indigo-500 dark:shadow-none dark:hover:bg-indigo-400 dark:focus-visible:outline-indigo-500"
    >
      Next
    </button>
  </div>
</template>

<script setup>
import { useCycleList } from "@/composables/useCycleList";

const { state, prev, next } = useCycleList(["Dog", "Cat", "Bird", "Iguana"]);
</script>
