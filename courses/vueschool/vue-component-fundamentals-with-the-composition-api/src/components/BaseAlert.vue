<template>
  <div
    v-if="!closed"
    class="rounded-md p-4 dark:outline"
    :class="{
      'bg-yellow-50 dark:bg-yellow-500/10 dark:outline-yellow-500/15':
        type === 'warning',
      'bg-red-50 dark:bg-red-500/15 dark:outline-red-500/25': type === 'error',
      'bg-green-50 dark:bg-green-500/10 dark:outline-green-500/20':
        type === 'success',
      'bg-blue-50 dark:bg-blue-500/10 dark:outline-blue-500/20':
        type === 'info',
    }"
  >
    <div class="flex">
      <div class="shrink-0">
        <ExclamationTriangleIcon
          v-if="type === 'warning'"
          class="size-5 text-yellow-400 dark:text-yellow-300"
          aria-hidden="true"
        />
        <XCircleIcon
          v-if="type === 'error'"
          class="size-5 text-red-400"
          aria-hidden="true"
        />
        <CheckCircleIcon
          v-if="type === 'success'"
          class="size-5 text-green-400"
          aria-hidden="true"
        />
        <InformationCircleIcon
          v-if="type === 'info'"
          class="size-5 text-blue-400"
          aria-hidden="true"
        />
      </div>
      <div class="ml-3">
        <h3
          v-if="title"
          class="text-sm font-medium text-yellow-800 dark:text-yellow-100"
          :class="{
            'text-yellow-800 dark:text-yellow-100': type === 'warning',
            'text-red-800 dark:text-red-100': type === 'error',
            'text-green-800 dark:text-green-100': type === 'success',
            'text-blue-800 dark:text-blue-100': type === 'info',
          }"
        >
          {{ title }}
        </h3>
        <div
          class="text-sm"
          :class="{
            'mt-2': title,
            'text-yellow-700 dark:text-yellow-100/80': type === 'warning',
            'text-red-700 dark:text-red-100/80': type === 'error',
            'text-green-700 dark:text-green-100/80': type === 'success',
            'text-blue-700 dark:text-blue-100/80': type === 'info',
          }"
        >
          <p>
            <slot></slot>
          </p>
        </div>
      </div>
      <div class="ml-auto pl-3">
        <div class="-mx-1.5 -my-1.5">
          <button
            type="button"
            class="inline-flex rounded-md p-1.5 focus-visible:ring-2 focus-visible:ring-offset-2 focus-visible:outline-hidden dark:bg-transparent dark:focus-visible:ring-offset-1"
            :class="{
              'bg-yellow-50 text-yellow-500 hover:bg-yellow-100 focus-visible:ring-yellow-600 focus-visible:ring-offset-yellow-50 dark:text-yellow-400 dark:hover:bg-yellow-500/10 dark:focus-visible:ring-yellow-500 dark:focus-visible:ring-offset-yellow-900':
                type === 'warning',
              'bg-red-50 text-red-500 hover:bg-red-100 focus-visible:ring-red-600 focus-visible:ring-offset-red-50 dark:text-red-400 dark:hover:bg-red-500/10 dark:focus-visible:ring-red-500 dark:focus-visible:ring-offset-red-900':
                type === 'error',
              'bg-green-50 text-green-500 hover:bg-green-100 focus-visible:ring-green-600 focus-visible:ring-offset-green-50 dark:text-green-400 dark:hover:bg-green-500/10 dark:focus-visible:ring-green-500 dark:focus-visible:ring-offset-green-900':
                type === 'success',
              'bg-blue-50 text-blue-500 hover:bg-blue-100 focus-visible:ring-blue-600 focus-visible:ring-offset-blue-50 dark:text-blue-400 dark:hover:bg-blue-500/10 dark:focus-visible:ring-blue-500 dark:focus-visible:ring-offset-blue-900':
                type === 'info',
            }"
            @click="close"
          >
            <span class="sr-only">Dismiss</span>
            <XMarkIcon class="size-5" aria-hidden="true" />
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import {
  ExclamationTriangleIcon,
  XMarkIcon,
  XCircleIcon,
  CheckCircleIcon,
  InformationCircleIcon,
} from "@heroicons/vue/20/solid";

const props = defineProps({
  type: { type: String, required: true },
  title: { type: String },
});

const emit = defineEmits(["closed"]);

const closed = ref(false);
const close = () => {
  closed.value = true;
  emit("closed");
};
</script>
