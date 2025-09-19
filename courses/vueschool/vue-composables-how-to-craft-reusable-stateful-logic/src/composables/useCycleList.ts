import { computed, MaybeRefOrGetter, ref, toRef } from "vue";

export const useCycleList = (list: MaybeRefOrGetter<Array<any>>) => {
  const activeIndex = ref(0);
  const _list = toRef(list);
  const state = computed(() => list[activeIndex.value]);

  function next() {
    if (activeIndex.value === _list.value.length - 1) {
      activeIndex.value = 0;
    } else {
      activeIndex.value++;
    }
  }

  function prev() {
    if (activeIndex.value === 0) {
      activeIndex.value = _list.value.length - 1;
    } else {
      activeIndex.value--;
    }
  }

  function go(index: number) {
    if (index >= _list.value.length) {
      throw new Error(
        `Cannot go to index ${index}. The list provided to useCycleList is not that long.`
      );
    } else {
      activeIndex.value = index;
    }
  }

  return {
    state,
    prev,
    next,
    go,
  };
};
