
class QueueError(Exception):
    pass


class Queue:
    def __init__(self):
        self.__storage = []

    def put(self, elem):
        self.__storage.insert(0, elem)

    def get(self):
        if not self.__storage:
            raise QueueError("Queue is empty")
        return self.__storage.pop()


class SuperQueue(Queue):
    def isempty(self):
        return len(self._Queue__storage) == 0


que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")
