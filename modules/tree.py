import queue

class Simpul:
    def __init__(self, value):
        self.child = []
        self.value = value

class Tree:
    def __init__(self, value):
        self.root = Simpul(value)

    def add_child(self, value, node):
        node.child.append(value)

    def get_level(self, node):
        task_queue = queue.Queue()
        new_queue = queue.Queue()
        temp = self.root
        level = 0
        if temp != node:
            if temp.child != []:
                for child in temp.child:
                    task_queue.put(child)
            while True:
                while not task_queue.empty():
                    temp = task_queue.get()
                    if temp == node:
                        break
                    if temp.child != []:
                        for child in temp.child:
                            new_queue.put(child)
                level += 1
                if new_queue.empty() and temp != node:
                    level = -1
                    break
                elif temp == node:
                    break
                task_queue = new_queue
                # wait until new_queue empty
                while not new_queue.empty():
                    new_queue.get()
        return level

    def search_node(self, label):
        pass