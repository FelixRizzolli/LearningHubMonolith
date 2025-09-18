# Lessons Learned

## Lesson 1 - Introduction to Vue Component Design

This lesson introduces the importance of using proven patterns for Vue component design to create code that is easier to manage, test, and maintain. Key points include:

- Patterns help break down complex components, use branching logic, leverage slots and template props, organize lists, separate concerns (smart vs. dumb components), and manage forms effectively.
- Advanced patterns like recursive and tightly coupled components are also introduced.
- The focus is on understanding the reasoning behind each pattern, not just coding along.
- Benefits of using patterns:
  1.  **Consistency** – predictable, navigable codebase
  2.  **Maintainability** – easier to debug and modify
  3.  **Scalability** – helps apps grow without becoming unwieldy
  4.  **Reusability** – encourages reusable components
  5.  **Collective wisdom** – leverages community experience and proven solutions

These patterns help avoid common pitfalls and enable building scalable, maintainable Vue applications.

## Lesson 2 - Branching Component Pattern

The branching component pattern (also called the extract conditional pattern) involves extracting each branch of a conditional (like `v-if`/`v-else`) into its own component.

- Useful when a component’s template contains large or complex markup inside conditional blocks, such as loading skeletons and loaded content.
- By moving each branch (e.g., loading state and loaded state) into separate components, the main component’s template becomes much clearer and easier to read.
- The logic and data-fetching remain in the parent, but the UI for each state is delegated to dedicated child components.
- This pattern improves maintainability, readability, and makes future edits easier, especially as components grow in complexity.

**Example:**

Suppose you have a component with a conditional in the template:

```vue
<template>
  <div>
    <div v-if="loading">Loading...</div>
    <div v-else>Content loaded!</div>
  </div>
</template>
```

With the branching component pattern, you extract each branch into its own component:

```vue
<template>
  <div>
    <LoadingSkeleton v-if="loading" />
    <LoadedContent v-else />
  </div>
</template>
```

This keeps the main component clean and delegates the UI for each state to dedicated components.

## Lesson 3 - Slots and Template Props Pattern

Props in Vue can serve different purposes:

- **State props**: Pass reactive state (e.g., loading indicators) that changes during the app’s lifetime.
- **Configuration props**: Pass hardcoded options to configure a component (e.g., `outlined: true`).
- **Template props**: Pass values that are only displayed directly in the template, not used in logic or attributes.

When a prop is only used to display a string or content in the template (a template prop), it’s often better to use a slot instead. Slots make components more flexible, allowing parents to pass in not just text, but also HTML or other components.

**Example: Using a template prop**

```vue
<!-- AppButton.vue -->
<template>
  <button :class="{ 'btn-outline': outline }">
    <AppSpinner v-if="loading" />
    {{ label }}
  </button>
</template>

<script setup>
defineProps({
  // state props
  loading: { type: Boolean, default: false },

  // configuration props
  outline: { type: Boolean, default: false },

  // template props
  label: { type: String },
});
</script>
```

Usage:

```vue
<AppButton label="Click me" />
```

**Refactored: Using a slot**

```vue
<!-- AppButton.vue -->
<template>
  <button :class="{ 'btn-outline': outline }">
    <slot></slot>
  </button>
</template>

<script setup>
defineProps({
  loading: { type: Boolean, default: false },
  outline: { type: Boolean, default: false },
});
</script>
```

Usage:

```vue
<AppButton>Click me</AppButton>
<AppButton><strong>Click me</strong></AppButton>
<AppButton><IconStar /> Favorite</AppButton>
```

With slots, the parent can pass in any content, not just plain text, making the component much more flexible and reusable.

## Lesson 4 - List with ListItem Pattern

Lists are everywhere in web apps—courses, users, cards, tables, etc. The List with ListItem pattern helps you encapsulate list logic and markup, making your code cleaner and more reusable.

**Pattern steps:**

- Extract the list markup and logic into a dedicated List component (e.g., `UserList`).
- Pass the list data as a prop to the List component.
- Extract the markup for each item into a ListItem component (e.g., `UserListItem`) if it becomes complex.
- Optionally, extract empty states and content branches into their own components for clarity.

**Example:**

```vue
<!-- UserList.vue -->
<template>
  <div>
    <UserListControls />
    <!-- optional, for filters/search -->
    <UserListContent v-if="filteredUsers.length" :users="filteredUsers" />
    <UserListEmpty v-else />
  </div>
</template>

<script setup>
defineProps({ users: Array });
// ...filter logic, computed filteredUsers, etc.
</script>
```

```vue
<!-- UserListContent.vue -->
<template>
  <table>
    <tbody>
      <UserListItem v-for="user in users" :key="user.id" :user="user" />
    </tbody>
  </table>
</template>

<script setup>
defineProps({ users: Array });
</script>
```

```vue
<!-- UserListItem.vue -->
<template>
  <tr>
    <td>{{ user.name }}</td>
    <!-- more fields as needed -->
  </tr>
</template>

<script setup>
defineProps({ user: Object });
</script>
```

This approach keeps your page components clean, makes lists and list items reusable, and allows you to further break out empty states or controls as needed. The result is a more maintainable and scalable codebase.

## Lesson 5 - Smart vs. Dumb Components

This pattern distinguishes between two main types of components:

- **Dumb (Presentational) Components:**
  - Only receive data via props and display it.
  - Contain little or no logic; focus on rendering and styling.
  - Examples: buttons, cards, or list items.
  - Can be further divided into:
    - **Base components** (generic, reusable, e.g., `AppButton`, `AppCard`)
    - **App-specific dumb components** (specific to your app, e.g., `PostsListItem`)
  - Naming: Prefix base components with `App`, `Base`, or `V` (e.g., `AppButton`).
  - Advantages: Easier to test, understand, and style.

**Example of a dumb component:**

```vue
<!-- AppCard.vue -->
<template>
  <div class="card">
    <slot />
  </div>
</template>
```

```vue
<!-- PostsListItem.vue -->
<template>
  <AppCard>
    <h3>{{ post.title }}</h3>
    <p>{{ post.summary }}</p>
  </AppCard>
</template>

<script setup>
defineProps({ post: Object });
</script>
```

- **Smart (Container) Components:**
  - Manage state, logic, and may handle data fetching.
  - Pass data down to dumb components as props.
  - Examples: list containers, pages, or components that fetch/filter data.
  - Can be further divided into:
    - **Smart components with data fetching:** Responsible for retrieving data from APIs or other sources, managing loading and error states.
    - **Smart components without data fetching:** Manage local state, computed properties, and logic, but receive their data via props or context.

**Example of a smart component (no data fetching):**

```vue
<!-- PostsList.vue -->
<template>
  <div>
    <input v-model="filter" placeholder="Filter posts..." />
    <PostsListItem v-for="post in filteredPosts" :key="post.id" :post="post" />
  </div>
</template>

<script setup>
import { ref, computed } from "vue";
import PostsListItem from "./PostsListItem.vue";

const posts = ref([
  { id: 1, title: "Hello", summary: "..." },
  // ...more posts
]);
const filter = ref("");
const filteredPosts = computed(() =>
  posts.value.filter((p) => p.title.includes(filter.value))
);
</script>
```

**Example of a smart component (with data fetching):**

```vue
<!-- LatestPost.vue -->
<template>
  <div v-if="loading">Loading...</div>
  <div v-else-if="error">Error: {{ error }}</div>
  <div v-else>
    <h2>{{ post.title }}</h2>
    <p>{{ post.summary }}</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
const post = ref(null);
const loading = ref(true);
const error = ref(null);
onMounted(async () => {
  try {
    // Simulate API call
    post.value = await fetchPost();
  } catch (e) {
    error.value = e.message;
  } finally {
    loading.value = false;
  }
});
function fetchPost() {
  // Replace with real API call
  return Promise.resolve({ title: "Latest Post", summary: "..." });
}
</script>
```

**Best practices:**

- Prefer more dumb components than smart components for maintainability.
- Extract logic and state into smart components, and keep presentational components simple.
- When possible, separate data fetching from local state management for clarity.
- This separation makes your codebase easier to test, understand, and scale.
- This separation makes your codebase easier to test, understand, and scale.

## Lesson 6 - From Component Pattern

## Lesson 7 - Some Advanced Patterns

### Tightly Coupled Components

### Recursive Components

### Lazy Components
