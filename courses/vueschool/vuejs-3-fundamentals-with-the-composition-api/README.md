# Lessons Learned

## Lesson 1

```html
<script setup>
  import { ref } from "vue";

  const msg = ref("Hello World!");
</script>

<template>
  <!-- 
      {{  }} is called the Vue templating syntax / double mustache syntax
      Only one expression is allowed and we also can't declare new variables 
  -->
  <h1>{{ msg || "Welcome" }}</h1>

  <!-- 
      v-model provides two-way data binding for reactive references,
      which means if the content is changed in one input it will be
      also changed in the other one and the h1 
  -->
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
        To help Vue know when to re-render which items, it's always recommended to add the key attribute to loops.
        The key attribute should be set to some unique ID per item (such as an id from a database).
        This isn't always absolutely necessary for simpler arrays but it's still a good practice.

        ----

        Note:
        You might be tempted to use the index as the key. But this is actually what Vue does by default anyway 
        under the hood, so really it's the exact same thing as not providing a key at all. And worse, it gives you
        the false security that you have provided a key when you actually haven't. 
        
        ----

        You can also use objects. In this case the indexes will become 'item-1', 'item-2', ...
        const items = ref({
            'item-1': { id: 1, label: "10 party hats" },
            'item-2': { id: 2, label: "2 board games" },
            'item-3': { id: 3, label: "20 cups" },
        });

        ----

        v-for is reactive as well. If we push an item to the items array then the loop will automatically 
        update and the item will be included on the page. Likewise for remove.
     -->
    <li v-for="({ id, label }, index) in items" :key="id">
      {{ index }}: {{ label }}
    </li>
  </ul>
</template>
```

## Lesson 3

- `v-model` can also take modifiers. Modifiers can alter the behavior of the model and are defined by adding a period followed by the modifier name.
  - `v-model.lazy="item"` updates the item only after the input loses focus (on blur)
  - `v-model.number="item"` casts the data to a number
  - `v-model.trim="item"` automatically removes any surrounding white space from your data
- `v-model` can also be used with textareas, selects, checkboxes, radio buttons, and more

## Lesson 4

- With `v-on` you can define event listeners like `v-on:click` or the shorthand `@click`.
- `v-on:keyup` is used to listen for keyboard events on an input or element. It triggers every time a key is released while the element is focused.
  - Example: `<input v-on:keyup="handler" />` will call `handler` on any key release.
- You can use key modifiers to listen for specific keys:
  - `v-on:keyup.enter` triggers the event only when the Enter key is pressed.
  - Other key modifiers include `.esc`, `.tab`, `.space`, etc. (e.g., `v-on:keyup.esc`)
- You can also use event modifiers to change the default behavior:
  - `v-on:submit.prevent` prevents the default form submission and allows you to handle the submit event in JavaScript.
- `v-on` can be written as `@` as a short form (e.g., `@click`, `@keyup.enter`).
