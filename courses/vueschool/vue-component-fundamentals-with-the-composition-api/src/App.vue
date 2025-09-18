<script setup>
import { shallowRef, markRaw, ref } from "vue";
import AppNavbar from "./components/AppNavbar.vue";
import AppCoffeeProject from "./components/AppCoffeeProject.vue";
import AppGithubProject from "./components/AppGithubProject.vue";
import AppAlertsProject from "./components/AppAlertsProject.vue";

const navigation = shallowRef([
  { name: "Coffee", component: markRaw(AppCoffeeProject), current: true },
  { name: "GitHub", component: markRaw(AppGithubProject), current: false },
  { name: "Alerts", component: markRaw(AppAlertsProject), current: false },
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
