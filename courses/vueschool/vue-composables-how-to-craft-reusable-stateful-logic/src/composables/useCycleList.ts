import { computed, ref } from "vue";

export const useCycleList = (list: Array<any>) => {
  const activeIndex = ref(0);
  const state = computed(() => list[activeIndex.value]);

  function next() {
    if (activeIndex.value === list.length - 1) {
      activeIndex.value = 0;
    } else {
      activeIndex.value++;
    }
  }

  function prev() {
    if (activeIndex.value === 0) {
      activeIndex.value = list.length - 1;
    } else {
      activeIndex.value--;
    }
  }

  return {
    state,
    prev,
    next,
    go: () => {},
  };
};
