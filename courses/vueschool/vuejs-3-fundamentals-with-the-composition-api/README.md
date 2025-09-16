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

## Lesson 2 & 3

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
        The key attribute should be set to a unique ID per item (such as an id from a database).
        This isn't always absolutely necessary for simple arrays but it's still a good practice.

        ----

        Note:
        You might be tempted to use the index as the key. But this is actually what Vue does by default anyway 
        under the hood, so really it's the exact same thing as not providing a key at all. Worse, it gives you
        the false security that you have provided a key when you actually haven't. 
        
        ----

        You can also use objects. In this case the indexes will become 'item-1', 'item-2', ...
        const items = ref({
            'item-1': { id: 1, label: "10 party hats" },
            'item-2': { id: 2, label: "2 board games" },
            'item-3': { id: 3, label: "20 cups" },
        });

        ----

        v-for is reactive as well. If we push an item to the items array, the loop will automatically 
        update and the item will be included on the page. Likewise for remove.
     -->
    <li v-for="({ id, label }, index) in items" :key="id">
      {{ index }}: {{ label }}
    </li>
  </ul>
</template>
```

## Lesson 4

- `v-model` can also take modifiers. Modifiers can alter the behavior of the model and are defined by adding a period followed by the modifier name.
  - `v-model.lazy="item"` updates the item only after the input loses focus (on blur).
  - `v-model.number="item"` casts the data to a number.
  - `v-model.trim="item"` automatically removes any surrounding white space from your data.
- `v-model` can also be used with textareas, selects, checkboxes, radio buttons, and more.

## Lesson 5

- With `v-on` you can define event listeners like `v-on:click` or the shorthand `@click`.
- `v-on:keyup` is used to listen for keyboard events on an input or element. It triggers every time a key is released while the element is focused.
  - Example: `<input v-on:keyup="handler" />` will call `handler` on any key release.
- You can use key modifiers to listen for specific keys:
  - `v-on:keyup.enter` triggers the event only when the Enter key is pressed.
  - Other key modifiers include `.esc`, `.tab`, `.space`, etc. (e.g., `v-on:keyup.esc`).
- You can also use event modifiers to change the default behavior:
  - `v-on:submit.prevent` prevents the default form submission and allows you to handle the submit event in JavaScript.
- `v-on` can be written as `@` as a short form (e.g., `@click`, `@keyup.enter`).

## Lesson 6

- Inside the `script` section, in order to access the value of a reactive reference, you have to use the `.value` property. The reason for this is that Vue uses proxies to create reactive data.

## Lesson 7

- `v-if`, `v-else-if`, and `v-else` can be used to conditionally render components.

## Lesson 8

- `v-bind` is used to dynamically bind one or more attributes, or a component prop, to an expression. The most common use is to bind the value of an attribute to a variable or computed value in your Vue instance.
  - Example: `<img v-bind:src="imageUrl" />` will set the `src` attribute of the image to the value of `imageUrl`.
- You can use the shorthand `:` for `v-bind`, so `<img :src="imageUrl" />` is equivalent.
- `v-bind` can also be used to bind multiple attributes at once using an object: `<div v-bind="objectOfAttrs"></div>`

## Lesson 9

- `:class` is a special binding for dynamically setting the `class` attribute on an element.
- There are several ways to use `:class`:
  - **Object syntax (`{}`):**
    - Example: `<div :class="{ active: isActive, 'text-danger': hasError }"></div>`
    - The keys are class names, and the values are boolean expressions. The class is applied if the value is true.
  - **Array syntax (`[]`):**
    - Example: `<div :class="[activeClass, errorClass]"></div>`
    - Each item in the array can be a string (class name) or an object (as in the object syntax above).
  - **Static classes:**
    - You can use the normal `class` attribute for static classes together with `:class` for dynamic ones.
    - Example: `<div class="static-class" :class="{ active: isActive }"></div>`
  - **Mixed array/object syntax:**
    - You can mix array and object syntax inside the array.
    - Example: `<div :class="['static-class', { active: isActive, error: hasError }]"></div>`
    - This allows you to combine static and dynamic classes flexibly.

## Lesson 10

- Like `ref`, `computed` is a Vue helper function that helps us interact with its reactivity system.
- `computed` properties are used to define reactive values that are derived from other reactive sources (like refs or reactive objects).
- The function passed to `computed` must return a value; this value will be cached and only recomputed when its dependencies change.
- `computed` properties are lazily evaluated and efficiently cached, so they are only recalculated when needed.
- Use `computed` when you want to transform or combine data for the presentation layer, but do not use them to cause side effects or modify state.
- `computed` properties are accessed like refs, so you need to use `.value` to get their value in the script section.
- You can use `computed` properties in templates without `.value` (Vue unwraps them automatically in templates).
- Compared to methods, `computed` properties are cached based on their dependencies, while methods are re-executed every time they are called in the template.
- Example:
  ```js
  import { ref, computed } from "vue";
  const count = ref(1);
  const double = computed(() => count.value * 2);
  ```
  In the template: `<span>{{ double }}</span>`
