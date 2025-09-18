<script setup>
import { ref } from "vue";

const count = ref(0);
</script>

<template>
  <button @click="($event) => count++" class="btn">{{ count }}</button>
</template>
