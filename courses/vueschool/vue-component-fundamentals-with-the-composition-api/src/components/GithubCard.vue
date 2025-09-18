<script setup>
import { ref } from "vue";

const props = defineProps({
  username: { type: String, default: "felixrizzolli", required: true },
});

const user = ref();

fetch(`https://api.github.com/users/${props.username}`).then(async (res) => {
  const data = await res.json();
  user.value = data;
});
</script>

<template>
  <div v-if="user" class="relative">
    <div class="relative h-72 w-full overflow-hidden rounded-lg">
      <img
        :src="user.avatar_url"
        :alt="'Profile Picture of ' + user.name"
        class="size-full object-cover"
      />
    </div>
    <div class="relative mt-4">
      <h3 class="text-sm font-medium text-gray-900">{{ user.name }}</h3>
      <p class="mt-1 text-sm text-gray-500">
        Followers: {{ user.followers }} / Following: {{ user.following }}
      </p>
    </div>
  </div>
  <div v-if="user?.html_url" class="mt-6">
    <a
      :href="user?.html_url"
      class="relative flex items-center justify-center rounded-md border border-transparent bg-gray-100 px-8 py-2 text-sm font-medium text-gray-900 hover:bg-gray-200"
      >View Profile</a
    >
  </div>
</template>
