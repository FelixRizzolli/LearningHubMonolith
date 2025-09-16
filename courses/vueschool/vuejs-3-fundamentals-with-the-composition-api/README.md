# Lessons Learnd

## Lesson 1

```html
<script setup>
  import { ref } from "vue";

  const msg = ref("Hello World!");
</script>

<template>
  <!-- {{  }} - is called the vue templating syntax / double mustache syntax -->
  <!-- Only one expression is allowed and we also can't declare new variables -->
  <h1>{{ msg || "Welcome" }}</h1>

  <!-- v-model provides two-way data binding for reactive references,
       which means if the content is changed in one input it will be
       also changed in the other one and the h1 -->
  <input v-model="msg" />
  <input v-model="msg" />
</template>
```

## Lesson 2

```html
<script setup>
  import { ref } from "vue";

  const header = ref("Shopping List App");
  const items = ref([
    { id: 1, label: "10 party hats" },
    { id: 2, label: "2 board games" },
    { id: 3, label: "20 cups" },
  ]);
</script>

<template>
  <h1>{{ header }}</h1>
  <ul>
    <!-- 
        To help vue know when to re-render what items, it's always recommended to add the key attribute to loops.
        The key attribute should be set to some unique ID per item (such as an id from a database).
        This isn't always absolutely necessary for simpler arrays but it's still a good practice.

        ----

        Note:
        You migth be tempted to use the index as the key. But this is actually what Vue does by default anyways 
        under the hood, so really it's the exact same thing as not providing a key at all. And worse, it gives you
        the false security that you have provided a key when you actually haven't. 
        
        ----

        You can use also objects. In this case the indexes will become 'item-1', 'item-2', ...
        const items = ref({
            'item-1': { id: 1, label: "10 party hats" },
            'item-2': { id: 2, label: "2 board games" },
            'item-3': { id: 3, label: "20 cups" },
        });

        ----

        v-for is reactive as well. If we would have pushed an item to the items array then the loop would automatically 
        update and the item will be included on the page. Likewise for remove.
     -->
    <li v-for="({ id, label }, index) in items" :key="id">
      {{ index }}: {{ label }}
    </li>
  </ul>
</template>
```
