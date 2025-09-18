# Lessons Learned

## Lesson 1 - Intro to Vue 3 Components

- **Vue 3 Components Introduction**

  - Components are reusable pieces of markup and logic, bundled together.
  - Used to build different parts of websites or web apps (e.g., headers, cards, filters, badges).
  - Components are the building blocks of Vue apps, enabling modular and reusable code.

- **Creating a Component**

  - Create a new `.vue` file in the `components` directory (e.g., `CounterButton.vue`).
  - Add a `<template>` section for markup:
    ```html
    <template>
      <button @click="count++">{{ count }}</button>
    </template>
    ```
  - Add a `<script setup>` section for logic:
    ```html
    <script setup>
      import { ref } from "vue";
      const count = ref(0);
    </script>
    ```

- **Using a Component**

  - Import the component in `App.vue`:
    ```html
    <script setup>
      import CounterButton from "./components/CounterButton.vue";
    </script>
    ```
  - Use the component in the template (multiple possibilities):
    ```html
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
    ```html
    <CounterButton />
    <CounterButton />
    <CounterButton />
    ```

- **Self-Closing Tags**

  - If no slot/content is needed, use self-closing syntax:
    ```html
    <CounterButton />
    ```

## Lesson 2 - Reusable Components with Props

- By extracting repeated markup (like coffee subscription plans) into a component, code becomes cleaner and easier to maintain.

  **Example (before):**

  ```html
  <div class="plan">
    <span class="title">The Hacker</span>
    <div class="description">For those who love to hack on code.</div>
  </div>
  <div class="plan">
    <span class="title">The Addict</span>
    <div class="description">For those who can't get enough coffee.</div>
  </div>
  <!-- ...more repeated markup... -->
  ```

  **Example (after):**

  ```html
  <CoffeePlan
    name="The Hacker"
    description="For those who love to hack on code."
  />
  <CoffeePlan
    name="The Addict"
    description="For those who can't get enough coffee."
  />
  ```

- Props allow components to accept dynamic data, making them flexible and reusable for different content.

  **Example:**

  ```html
  <CoffeePlan
    name="The Hacker"
    description="For those who love to hack on code."
  />
  <CoffeePlan
    name="The Addict"
    description="For those who can't get enough coffee."
  />
  ```

- Props are defined in the `<script setup>` block using the `defineProps` macro (no import needed).

  **Example:**

  ```html
  <script setup>
    defineProps(["name", "description"]);
  </script>
  ```

- Props can be defined as an array (simple) or as an object (for type checking, default values, and required fields).

  **Example (object syntax):**

  ```html
  <script setup>
    defineProps({
      name: { type: String, required: true },
      description: { type: String, default: "No description" },
    });
  </script>
  ```

- Passing props is done using HTML-like attributes, and you can use the `v-for` directive to render multiple component instances with different prop values.

  **Example (v-for):**

  ```html
  <script setup>
    import { ref } from "vue";
    const plans = ref([
      {
        name: "The Hacker",
        description: "For those who love to hack on code.",
      },
      {
        name: "The Addict",
        description: "For those who can't get enough coffee.",
      },
      {
        name: "The Curious",
        description: "For those who want to try something new.",
      },
    ]);
  </script>

  <template>
    <CoffeePlan
      v-for="plan in plans"
      :key="plan.name"
      :name="plan.name"
      :description="plan.description"
    />
  </template>
  ```

- Vue will warn in the console if a prop receives the wrong type or if a required prop is missing.

  **Example (prop validation warning):**

  ```html
  <CoffeePlan :name="true" />
  <!-- Console warning: Invalid prop: type check failed for prop 'name'. Expected String, got Boolean -->
  ```

- Using props and components together reduces code duplication and makes your app more maintainable and scalable.

## Lesson 3 - Nested Components in Vue

- In Vue, components can be composed of other components, allowing you to build complex UIs from smaller, reusable building blocks.
- Nesting components helps organize your code, reduce duplication, and promote separation of concerns.
- Parent components can include child components in their templates and manage their data or behavior.
- Data for nested components can be kept local for encapsulation or passed in as props for flexibility and reuse.
- This pattern enables you to reuse and combine components in different parts of your application, making your codebase more maintainable and scalable.

## Lesson 4 - Global vs Local Vue Components

- In Vue with the Composition API, you can register components either globally or locally.
- Local registration (recommended for most cases) means importing a component directly in the `<script setup>` block of the component where it is used. This keeps your code modular and avoids unnecessary bloat.
- Global registration makes a component available throughout your app, but even if a globally registered component is not used anywhere, it will still be included in the final JavaScript bundle and downloaded by the user. This can negatively impact performance and bundle size.
- Prefer local registration for components only used in specific places, and reserve global registration for components that are truly reused across many parts of your app.

**Example: Local Registration (Composition API)**

```vue
<script setup>
import MyComponent from "./components/MyComponent.vue";
</script>

<template>
  <MyComponent />
</template>
```

**Example: Global Registration**

```js
// In main.js or main.ts
import { createApp } from "vue";
import App from "./App.vue";
import MyComponent from "./components/MyComponent.vue";

const app = createApp(App);
app.component("MyComponent", MyComponent);
app.mount("#app");
```

## Lesson 5 - Communication Between Vue Components with Custom Events

- **Parent-to-Child Communication:** Data is passed from parent to child components using props.
- **Child-to-Parent Communication:** To send data from a child to its parent, use custom events.
- **Defining Custom Events:** Use the `defineEmits` macro in the child component to declare custom events. The returned `emit` function is used to trigger these events, optionally with a payload (data).
- **Emitting Events:** When a user interacts with the child (e.g., clicks a button), call the emit function with the event name and any relevant data.
- **Listening for Events:** In the parent component, listen for the custom event using `v-on:eventName` or the shorthand `@eventName`. The payload is available as `$event` in the handler.
- **General Use Case:** Custom events allow child components to notify their parent components about actions, changes, or data updates, enabling flexible and decoupled communication.
- **Prop-Driven State:** The parent can pass props to children to control their state based on the parent's data, often in response to events emitted by the child.
- **Alternative Approach:** Sometimes, you can use native event listeners directly on the child component’s root element, but custom events are more flexible for complex scenarios.
- **Best Practice:** Use custom events for clear, maintainable communication from child to parent, especially when passing data or signaling actions.

**Example: Child emits a custom event**

```vue
<!-- ChildComponent.vue -->
<script setup>
const props = defineProps({
  label: String,
});
const emit = defineEmits(["customAction"]);
function handleClick() {
  emit("customAction", props.label);
}
</script>

<template>
  <button @click="handleClick">{{ label }}</button>
  <!-- When clicked, emits 'customAction' with the label as payload -->
</template>
```

**Example: Parent listens for the event and updates state**

```vue
<!-- ParentComponent.vue -->
<script setup>
import { ref } from "vue";
import ChildComponent from "./ChildComponent.vue";
const lastAction = ref("");
function handleCustomAction(payload) {
  lastAction.value = payload;
}
</script>

<template>
  <div>
    <div>Last action: {{ lastAction }}</div>
    <ChildComponent label="Click Me" @customAction="handleCustomAction" />
  </div>
</template>
```

**Alternative: Using native event listeners**

```vue
<ChildComponent label="Click Me" @click="doSomething" />
```

## Lesson 6 - Vue Component Prop and Event Validation

- **Prop Validation:** You can add a `validator` function to a prop definition to control what values are considered valid. The function receives the prop value and should return `true` (valid) or `false` (invalid). If invalid, Vue will show a warning in the console.
- **Example (Prop Validator):**
  ```js
  defineProps({
    name: {
      type: String,
      required: true,
      validator: value => value.startsWith("The"),
    }
  });
  ```
- **Event Validation:** To validate the payload of a custom event, define emits as an object with event names as keys and validator functions as values. The validator receives the payload and should return `true` or `false`.
- **Example (Event Validator):**
  ```js
  defineEmits({
    selected: payload => typeof payload === "string",
    hiThere: null // No validation for this event
  });
  ```
- **Multiple Events:** You can validate some events and not others by using `null` for events that don’t need validation.
- **Best Practice:** Use prop and event validation to catch errors early and ensure your components receive and emit the correct data types and formats.

## Lesson 7 - Component Naming Best Practices in Vue

## Lesson 8 - Vue Component Lifecycle Hooks

## Lesson 9 - Vue Component Slots

## Lesson 10 - Build a GitHub User Profile Vue Component

## Lesson 11 - Build an Alert Vue Component
