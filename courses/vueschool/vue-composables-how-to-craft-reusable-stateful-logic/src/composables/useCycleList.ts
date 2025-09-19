import { ref } from "vue";

export const useCycleList = (list: Array<any>) => {
  return {
    state: ref(""),
    prev: () => {},
    next: () => {},
    go: () => {},
  };
};
