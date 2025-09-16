<script setup>
import { ref } from "vue";

const header = ref("Shopping List App");
const editing = ref(false);
const items = ref([]);
const newItem = ref("");
const newItemHighPriority = ref(false);

const saveItem = () => {
  items.value.push({
    id: items.value.length + 1,
    label: newItem.value,
    highPriority: newItemHighPriority.value,
  });
  newItem.value = "";
  newItemHighPriority.value = false;
};

const doEdit = (e) => {
  editing.value = e;
  newItem.value = "";
  newItemHighPriority.value = false;
};

const togglePurchased = (item) => {
  item.purchased = !item.purchased;
};
</script>

<template>
  <div class="header">
    <h1>{{ header }}</h1>
    <button v-if="editing" @click="doEdit(false)" class="btn">Cancel</button>
    <button v-else @click="doEdit(true)" class="btn btn-primary">Edit</button>
  </div>
  <form v-if="editing" @submit.prevent="saveItem" class="add-item-form">
    <input v-model="newItem" type="text" placeholder="Add an item" />
    <label>
      <input type="checkbox" v-model="newItemHighPriority" />
      High Priority
    </label>
    <button :disabled="newItem.trim().length < 5" class="btn btn-primary">
      Save Item
    </button>
  </form>
  <ul>
    <li
      v-for="(item, index) in items"
      @click="togglePurchased(item)"
      :key="item.id"
      :class="{ strikeout: item.purchased, priority: item.highPriority }"
    >
      {{ item.label }}
    </li>
  </ul>
  <p v-if="!items.length">Nothing to see here</p>
</template>
