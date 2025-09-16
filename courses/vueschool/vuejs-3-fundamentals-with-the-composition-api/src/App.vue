<script setup>
import { ref } from "vue";

// Double
const msg = ref("Hello World!");
</script>

<template>
  <!-- {{  }} - is called the vue templating syntax / double mustache syntax -->
  <h1>{{ msg }}</h1>

  <!-- v-model provides two-way data binding for reactive references, 
       which means if the content is changed in one input it will be 
       also changed in the other one and the h1 -->
  <input v-model="msg" />
  <input v-model="msg" />
</template>
