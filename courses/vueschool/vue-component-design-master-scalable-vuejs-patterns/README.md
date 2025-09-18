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

## Lesson 4 - List with ListItem Pattern

## Lesson 5 - Smart vs. Dump Components

## Lesson 6 - From Component Pattern

## Lesson 7 - Some Advanced Patterns

### Tightly Coupled Components

### Recursive Components

### Lazy Components
