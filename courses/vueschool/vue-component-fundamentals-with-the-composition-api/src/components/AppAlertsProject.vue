<template>
  <div
    class="mx-auto max-w-2xl px-4 py-16 sm:px-6 sm:py-24 lg:max-w-7xl lg:px-8"
  >
    <BaseAlert
      v-for="alert in alerts"
      :key="alert.message"
      :type="alert.type"
      class="mt-4"
      @closed="alerts = alerts.filter((a) => a.message !== alert.message)"
      >{{ alert.message }}</BaseAlert
    >

    <pre>
      {{ alerts }}
    </pre>
  </div>
</template>

<script setup>
import { ref } from "vue";
import BaseAlert from "./BaseAlert.vue";

const alerts = ref([
  {
    type: "info",
    message: "New software update available.",
  },
  {
    type: "success",
    message: "Your purchase has been confirmed!",
  },
  {
    type: "warning",
    message: "Warning: Invalid email address!",
  },
  {
    type: "error",
    message: "Error! Task failed successfully.",
  },
]);
</script>
