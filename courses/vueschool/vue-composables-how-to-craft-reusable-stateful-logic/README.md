# Lessons Learned

## Lesson 1 - Introduction to Composables

- **Composable functions** in Vue are similar to helper or utility functions in other languages, but they encapsulate **reusable, stateful logic** using Vue's Composition API.
- Composables typically use Vue's `ref` or `reactive` to define reactive state inside the function.
- The convention is to name composables with a `use` prefix (e.g., `useMouse`, `useTitle`), though this is not required.
- Composables are widely used in libraries like [VueUse](https://vueuse.org/) and component libraries such as Quasar, providing ready-to-use utilities for common tasks.
- Examples of composables from VueUse:
  - `useTitle`: Manipulates the document title reactively.
  - `useMouse`: Tracks mouse coordinates reactively.
  - `useNow`: Provides a reactive `Date` object that updates automatically.
  - `useArrayDifference`: Computes the difference between two reactive arrays and keeps the result in sync.
  - `useCycleList`: Cycles through a list/array reactively, exposing state and navigation functions.
- **Key characteristics:**
  - Encapsulate logic and state for reuse across components.
  - Leverage Vue's reactivity system for automatic updates.
  - Simplify working with browser APIs or user events by abstracting away manual event handling.

**General Example:**

```js
import { ref } from "vue";

// A simple composable to track a counter
export function useCounter() {
  const count = ref(0);
  const increment = () => count.value++;
  return { count, increment };
}
```

**Usage in a component:**

```js
import { useCounter } from "./composables/useCounter";

export default {
  setup() {
    const { count, increment } = useCounter();
    return { count, increment };
  },
};
```

// In template:
// <button @click="increment">Clicked {{ count }} times</button>

## Lesson 2 - Write your first Composable

- By convention, store all composables in a dedicated `composables` folder for better organization.
- Each composable should be placed in its own file, named after the composable (e.g., `useCycleList.ts`).
- A composable is simply a function (can use function or arrow function syntax) and should be exported for use in components.
- Prefixing composable names with `use` is a community convention for predictability and clarity.
- Using TypeScript (`.ts` files) for composables is recommended for type safety, but not required.
- You can create VS Code snippets to quickly scaffold new composable files.

**Basic Composable Template Example:**

```ts
// File: composables/useExample.ts
export function useExample() {
  // define reactive state and logic here
  return {};
}
```

```ts
// Or with arrow function syntax:
export const useExample = () => {
  // define reactive state and logic here
  return {};
};
```

## Lesson 3 - Accept Arguments For Flexible Composables

## Lesson 4 - Return Data and Functions From Composables

## Lesson 5 - Define Reactive State and Functions within a Composable

## Lesson 6 - Accept Reactive Composable Arguments

## Lesson 7 - Accept Flexible Component Arguments (Reactive, Getters, or Plain Data)

## Lesson 8 - Refine A Composable API with Getter / Setter Computed Props

## Lesson 9 - Extend Composable Functionality with a Config Argument

## Lesson 10 - Extend Composable Functionality with a Config Argument 2

## Lesson 11 - Provide Composable TypeSafety with TypeScript
