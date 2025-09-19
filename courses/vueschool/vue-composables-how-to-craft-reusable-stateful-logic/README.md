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

- Not all composables require arguments, but accepting arguments makes them more flexible and reusable for different use cases.
- Required arguments are used to provide essential data (e.g., a list or array to cycle through).
- In TypeScript, you can type arguments for clarity and safety (e.g., `list: any[]` for an array of any type).
- Optional arguments are often provided as a configuration object, allowing users to customize the composable's behavior.
- Arguments can be required or optional, depending on the composable's purpose.

**General Example:**

```ts
// A composable that accepts a required list argument and an optional config
export function useCycleList(list: any[], config?: { startIndex?: number }) {
  // logic here
  return {};
}
```

## Lesson 4 - Return Data and Functions From Composables

- The arguments to a composable define its input (API), and the return value defines its output.
- Return values are typically provided via an object containing reactive state and functions, making the composable flexible and easy to use.
- For simple composables, you can return a single reactive value directly (e.g., a `ref`).
- For more complex composables, return an object with multiple properties (state and functions) to provide a richer API.
- Defining the input and output of your composable first (before implementation) helps clarify its intended usage and improves developer experience.

**General Examples:**

```ts
// Simple composable returning a single ref
export function useTitle() {
  const title = ref("");
  return title;
}

// More complex composable returning state and functions
export function useCycleList(list: any[]) {
  const state = ref("");
  const next = () => {};
  const prev = () => {};
  const go = (index: number) => {};
  return { state, next, prev, go };
}
```

## Lesson 5 - Define Reactive State and Functions within a Composable

- Use Vue's reactivity utilities (such as `ref` and `computed`) to manage and expose reactive state within composables.
- Keep implementation details private inside composables and only expose the necessary state and functions to consumers.
- Encapsulate logic and state updates within composables to promote reusability and maintainability.

## Lesson 6 - Accept Reactive Composable Arguments

- Composables may need to accept reactive data (e.g., refs) as arguments, not just plain values.
- TypeScript helps catch type mismatches when passing refs versus plain values to composables.
- You can type composable arguments to accept a `Ref<T>` for reactive data, but this requires accessing `.value` inside the composable.

## Lesson 7 - Accept Flexible Component Arguments (Reactive, Getters, or Plain Data)

- Composables can be made more flexible by accepting arguments as refs, plain values, or getter functions.
- Vue provides utility types (like `MaybeRefOrGetter`) and functions (like `toRef`) to normalize arguments, so your composable can work with any of these input types.
- Use `toRef` to convert any input (ref, getter, or plain value) into a reactive ref inside your composable, simplifying internal logic.
- The Vue reactivity API offers other helpful utilities (e.g., `toValue`) for normalizing and working with different types of reactive and non-reactive data.

**General Example:**

```ts
import { toRef, type MaybeRefOrGetter } from "vue";

export function useFlexibleList(list: MaybeRefOrGetter<any[]>) {
  const normalizedList = toRef(list);
  // Now you can safely use normalizedList.value inside your composable
  return { normalizedList };
}
```

## Lesson 8 - Refine A Composable API with Getter / Setter Computed Props

- Design composables with intuitive interfaces by considering how end developers will interact with them.
- Use getter/setter computed properties to allow both reading and updating reactive state in a natural way (e.g., `state.value = ...`).
- A getter returns the current value, while a setter updates internal state based on the new value.
- Throw an error in the setter if the new value is invalid or not found, to provide clear feedback.
- This approach makes composables more flexible and user-friendly, aligning with Vue's reactivity system.

**General Example:**

```ts
import { ref, computed } from "vue";

export function useSelectableList(list: string[]) {
  const activeIndex = ref(0);
  const state = computed({
    get: () => list[activeIndex.value],
    set: (val: string) => {
      const idx = list.indexOf(val);
      if (idx >= 0) {
        activeIndex.value = idx;
      } else {
        throw new Error("Value not found in list");
      }
    },
  });
  return { state };
}
```

## Lesson 9 - Extend Composable Functionality with a Config Argument

- Use a configuration object to provide optional settings for composables, grouping related options together.
- Define a TypeScript interface for the config object to enable type safety and IDE auto-completion.
- Mark config properties as optional with `?` so users can provide any or all options.
- Export the config interface and default config object for reuse and better maintainability.
- Merge user-provided config with defaults inside the composable to ensure all options are handled, even if not all are provided.
- For deeply nested config objects, consider using a utility like the `defu` package for deep merging.

**General Example:**

```ts
// Define the config interface
export interface UseExampleConfig {
  fallbackIndex?: number;
  fallbackValue?: any;
}

// Provide default config values
export const useExampleConfigDefaults: UseExampleConfig = {
  fallbackIndex: undefined,
  fallbackValue: undefined,
};

// Merge user config with defaults
export function useExample(list: any[], config?: UseExampleConfig) {
  const _config = { ...useExampleConfigDefaults, ...config };
  // ...use _config.fallbackIndex, _config.fallbackValue as needed
  return {};
}
```

## Lesson 10 - Extend Composable Functionality with a Config Argument 2

## Lesson 11 - Provide Composable TypeSafety with TypeScript
