<template>
  <div class="bg-white">
    <div
      class="mx-auto max-w-2xl px-4 py-16 sm:px-6 sm:py-24 lg:max-w-7xl lg:px-8"
    >
      <h2 class="text-xl font-bold text-gray-900">GitHub Profiles</h2>

      <div
        class="mt-8 grid grid-cols-1 gap-y-12 sm:grid-cols-2 sm:gap-x-6 lg:grid-cols-4 xl:gap-x-8"
      >
        <div v-for="profile in profiles" :key="profile.id">
          <GithubCard :username="profile.username" />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import GithubCard from "./GithubCard.vue";

const profiles = [
  {
    id: 1,
    username: "felixrizzolli",
  },
  {
    id: 2,
    username: "ThePi2K",
  },
  {
    id: 3,
    username: "TheArled",
  },
  {
    id: 4,
    username: "Poerntii",
  },
];
</script>
