class QueueError(Exception):
    pass


class Queue:
    def __init__(self):
        self.__storage = []

    def put(self, elem):
        self.__storage.insert(0, elem)  # Add to the beginning of the list.

    def get(self):
        if not self.__storage:
            raise QueueError("Queue is empty")
        return self.__storage.pop()  # Remove from the end of the list.


que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")
