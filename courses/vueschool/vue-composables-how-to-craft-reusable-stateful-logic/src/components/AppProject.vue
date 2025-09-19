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

    <br />

    <input
      type="number"
      v-model="goTo"
      class="mt-8 block rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm/6 dark:bg-white/5 dark:text-white dark:outline-white/10 dark:placeholder:text-gray-500 dark:focus:outline-indigo-500"
    />
    <button
      @click="($event) => go(goTo)"
      class="mt-6 rounded-md bg-indigo-600 px-3.5 py-2.5 text-sm font-semibold text-white shadow-xs hover:bg-indigo-500 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600 dark:bg-indigo-500 dark:shadow-none dark:hover:bg-indigo-400 dark:focus-visible:outline-indigo-500"
    >
      Go To {{ goTo }}
    </button>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useCycleList } from "@/composables/useCycleList";

const { state, prev, next, go } = useCycleList([
  "Dog",
  "Cat",
  "Bird",
  "Iguana",
], {
    fallbackIndex: 0,
    fallbackValue: 'Dog'
});

const goTo = ref(0);
</script>
