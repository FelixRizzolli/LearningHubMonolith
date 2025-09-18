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

```html
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

```html
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

```html
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

```html
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
      validator: (value) => value.startsWith("The"),
    },
  });
  ```
- **Event Validation:** To validate the payload of a custom event, define emits as an object with event names as keys and validator functions as values. The validator receives the payload and should return `true` or `false`.
- **Example (Event Validator):**
  ```js
  defineEmits({
    selected: (payload) => typeof payload === "string",
    hiThere: null, // No validation for this event
  });
  ```
- **Multiple Events:** You can validate some events and not others by using `null` for events that don’t need validation.
- **Best Practice:** Use prop and event validation to catch errors early and ensure your components receive and emit the correct data types and formats.

## Lesson 7 - Component Naming Best Practices in Vue

- **Follow the Vue Style Guide:** Use the official Vue style guide to keep your component naming predictable and consistent, making your codebase easier to understand and navigate.
- **Multi-word Component Names:** Always use multi-word names for components (e.g., `BaseButton`, `UserCard`) to avoid conflicts with standard HTML elements, which are single-word.
- **File Name Casing:** Use PascalCase (e.g., `MyComponent.vue`) or kebab-case (e.g., `my-component.vue`) for single file component names. Be consistent throughout your project.
- **Prop Definition Syntax:** Prefer the detailed object syntax for props, specifying at least the type, and ideally also `required`, `default`, and `validator` when needed.
- **Prefix Base Components:** Prefix foundational, reusable components with `Base`, `App`, or `V` (e.g., `BaseButton.vue`, `AppInput.vue`).
- **Consistency:** Stick to one naming convention for your project and avoid mixing styles.
- **Examples:**
  - Good: `BaseButton.vue`, `UserProfileCard.vue`, `app-header.vue`
  - Bad: `button.vue`, `userprofilecard.vue`, `Appheader.vue`
- **Further Reading:** The [Vue style guide](https://vuejs.org/style-guide/) contains more recommendations for naming and organizing components. Refer to the official documentation for advanced best practices.

## Lesson 8 - Vue Component Lifecycle Hooks

- **Best Practice:** Use lifecycle hooks to manage side effects and resource cleanup, ensuring your components behave predictably and efficiently.

- **Further Reading:**

  - [Vue Lifecycle Guide](https://vuejs.org/guide/essentials/lifecycle)
  - [All Vue Lifecycle Hooks (API Reference)](https://vuejs.org/api/composition-api-lifecycle.html#composition-api-lifecycle-hooks)

- **Lifecycle Stages:** Every Vue component goes through a series of stages during its existence: creation, mounting to the DOM, updating, and unmounting (removal from the DOM).
- **Lifecycle Hooks:** Vue provides special functions called lifecycle hooks that let you run code at specific points in a component's lifecycle. These hooks are prefixed with `on` (e.g., `onMounted`, `onUnmounted`).
- **Common Hooks:**
  - `onMounted`: Runs after the component is added to the DOM. Useful for DOM access, API calls, or starting timers.
  - `onUnmounted`: Runs just before the component is removed from the DOM. Useful for cleanup, such as clearing intervals or removing event listeners.
- **Template Refs:** To safely access DOM elements, use template refs in combination with `onMounted`.
- **Memory Management:** Always clean up side effects (like intervals or subscriptions) in `onUnmounted` to prevent memory leaks.
- **Other Hooks:** Vue offers additional hooks like `onBeforeMount`, `onBeforeUpdate`, `onUpdated`, and more for advanced use cases.
- **Example (Basic Usage):**
  ```js
  <script setup>
  import { ref, onMounted, onUnmounted } from 'vue';
  const count = ref(0);
  let intervalId;
  onMounted(() => {
    intervalId = setInterval(() => {
      count.value++;
    }, 1000);
  });
  onUnmounted(() => {
    clearInterval(intervalId);
  });
  </script>
  <template>
    <div>Count: {{ count }}</div>
  </template>
  ```
- **Best Practice:** Use lifecycle hooks to manage side effects and resource cleanup, ensuring your components behave predictably and efficiently.

## Lesson 9 - Vue Component Slots

- **What Are Slots?**  
  Slots allow you to pass content (including HTML and components) from a parent to a child component, giving the parent full control over what appears inside the child.

- **Default Slot:**  
  Place content between the opening and closing tags of a component. In the child, use the `<slot></slot>` element to display this content.

- **Named Slots:**  
  You can define multiple slots in a component by giving them names (e.g., `<slot name="icon"></slot>`). The parent provides content for named slots using the `v-slot:name` directive or its shorthand `#name`.

- **Default Content:**  
  You can provide fallback content inside a slot element, which will be used if the parent does not provide content for that slot.

- **Scoped Slots:**  
  Scoped slots allow the child to expose data (slot props) to the parent, so the parent can use that data when rendering slot content. The parent accesses these props by destructuring them in the `v-slot` directive.

- **Use Cases:**

  - Pass HTML or components from parent to child.
  - Create flexible, reusable components (e.g., buttons, layouts).
  - Share state from child to parent within the slot context.

- **Example (Default and Named Slots):**

  ```html
  <!-- ChildComponent.vue -->
  <template>
    <button>
      <slot name="icon"></slot>
      <slot>Default Button</slot>
    </button>
  </template>
  ```

  ```html
  <!-- ParentComponent.vue -->
  <ChildComponent>
    <template #icon>
      <span>👋</span>
    </template>
    Submit
  </ChildComponent>
  ```

- **Example (Scoped Slot):**

  ```html
  <!-- ChildComponent.vue -->
  <template>
    <slot :hovered="hovered"></slot>
  </template>

  <script setup>
    import { ref } from "vue";
    const hovered = ref(false);
  </script>
  ```

  ```html
  <!-- ParentComponent.vue -->
  <ChildComponent v-slot="{ hovered }">
    <span v-if="hovered">Hovered!</span>
    <span v-else>Not hovered</span>
  </ChildComponent>
  ```

- **Best Practice:**  
  Use slots for maximum flexibility when you want to let the parent control part of a child’s template, especially for reusable UI components. Use scoped slots to share state or data from child to parent within the slot.

## Lesson 10 - Build a GitHub User Profile Vue Component

## Lesson 11 - Build an Alert Vue Component
