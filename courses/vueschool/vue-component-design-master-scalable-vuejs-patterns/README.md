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

## Lesson 5 - Smart vs. Dump Components

## Lesson 6 - From Component Pattern

## Lesson 7 - Some Advanced Patterns

### Tightly Coupled Components

### Recursive Components

### Lazy Components
