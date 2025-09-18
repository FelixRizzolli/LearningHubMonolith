# Lessons Learned

## Lesson 1 - Intro to Vue 3 Components

- **Vue 3 Components Introduction**

  - Components are reusable pieces of markup and logic, bundled together.
  - Used to build different parts of websites or web apps (e.g., headers, cards, filters, badges).

- **Creating a Component**

  - Create a new `.vue` file in the `components` directory (e.g., `CounterButton.vue`).
  - Add a `<template>` section for markup:
    ```vue
    <template>
      <button @click="count++">{{ count }}</button>
    </template>
    ```
  - Add a `<script setup>` section for logic:
    ```vue
    <script setup>
    import { ref } from "vue";
    const count = ref(0);
    </script>
    ```

- **Using a Component**

  - Import the component in `App.vue`:
    ```vue
    <script setup>
    import CounterButton from "./components/CounterButton.vue";
    </script>
    ```
  - Use the component in the template (multiple possibilities):
    ```vue
    <!-- PascalCase, standard tag -->
    <CounterButton></CounterButton>
    <!-- kebab-case, standard tag -->
    <counter-button></counter-button>
    <!-- PascalCase, self-closing -->
    <CounterButton />
    <!-- kebab-case, self-closing -->
    <counter-button />
    ```

- **Component Naming**

  - PascalCase is recommended for Vue files.
  - Can also use kebab-case in templates.

- **Reusability**

  - Components can be used multiple times on a page.
  - Each instance maintains its own state:
    ```vue
    <CounterButton />
    <CounterButton />
    <CounterButton />
    ```

- **Self-Closing Tags**

  - If no slot/content is needed, use self-closing syntax:
    ```vue
    <CounterButton />
    ```

- **Key Takeaway**
  - Components are the building blocks of Vue apps, enabling modular and reusable code.

## Lesson 2 - Reusable Components with Props

## Lesson 3 - Nested Components in Vue

## Lesson 4 - Global vs Local Vue Components

## Lesson 5 - Communication Between Vue Components with Custom Events

## Lesson 6 - Vue Component Prop and Event Validation

## Lesson 7 - Component Naming Best Practices in Vue

## Lesson 8 - Vue Component Lifecycle Hooks

## Lesson 9 - Vue Component Slots

## Lesson 10 - Build a GitHub User Profile Vue Component

## Lesson 11 - Build an Alert Vue Component
