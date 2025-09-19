<script setup>
import { shallowRef, markRaw, ref } from "vue";
import AppNavbar from "./components/AppNavbar.vue";
import AppProject from "./components/AppProject.vue";

const navigation = shallowRef([
  { name: "Project 1", component: markRaw(AppProject), current: true },
]);

const currentNav = ref(
  navigation.value.find((item) => item.current)?.component ||
    navigation.value[0].component
);

function handleNavSelect(component) {
  currentNav.value = component;
  navigation.value.forEach(
    (item) => (item.current = item.component === component)
  );
}
</script>

<template>
  <header>
    <AppNavbar :navigation="navigation" @select="handleNavSelect" />
  </header>
  <main>
    <Transition name="fade" mode="out-in">
      <component :is="currentNav" />
    </Transition>
  </main>
</template>

<style>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
.fade-enter-to,
.fade-leave-from {
  opacity: 1;
}
</style>
