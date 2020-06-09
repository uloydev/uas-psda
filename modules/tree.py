from .queue import Queue

class Simpul:
    def __init__(self, value):
        self.children = []
        self.value = value

class Data:
    def __init__(self):
        self.total = 0
        self.aktif = 0
        self.sembuh = 0
        self.meninggal = 0

class Tree:
    def __init__(self, value):
        self.root = Simpul(value)

    def add_children(self, value, node):
        node.children.append(Simpul(value))

    def get_data_by_level(self, level):
        data = []
        if level == 1:
            data.append(self.root.value)
        elif level > 1:
            temp = self.root
            task_queue = Queue()
            new_queue = Queue()
            level_temp = 2
            if temp.children != []:
                for children in temp.children:
                    task_queue.push(children)
            while True:
                while not task_queue.empty():
                    temp = task_queue.pop()
                    if level_temp == level:
                        data.append(temp.value)
                    else:
                        if temp.children != []:
                            for children in temp.children:
                                new_queue.push(children)
                if level_temp == level:
                    break
                level_temp += 1
                # wait until new_queue empty
                while not new_queue.empty():
                    task_queue.push(new_queue.pop())
        return data

    def search_by_value(self, value):
        temp = self.root
        task_queue = Queue()
        new_queue = Queue()
        if temp.value == value:
            return temp
        if temp.children != []:
            for children in temp.children:
                task_queue.push(children)
        else:
            print("data tidak ada di dalam tree")
            return None
        while True:
            while not task_queue.empty():
                temp = task_queue.pop()
                if temp.value == value:
                    return temp
                else:
                    if temp.children != []:
                        for children in temp.children:
                            new_queue.push(children)
            # wait until new_queue empty
            while not new_queue.empty():
                task_queue.push(new_queue.pop())
            if task_queue.empty():
                break
        return None

    def get_leaf(self, node):
        temp = node
        case = []
        task_queue = Queue()
        new_queue = Queue()
        if node.children != []:
            for child in node.children:
                task_queue.push(child)
        while True:
            while not task_queue.empty():
                temp = task_queue.pop()
                if temp.children != []:
                    for child in temp.children:
                        new_queue.push(child)
                else:
                    case.append(temp.value)
            if case != []:
                break
            # wait until new_queue empty
            while not new_queue.empty():
                task_queue.push(new_queue.pop())
        temp_arr = []
        arr = []
        data = []
        for item in case:
            if len(temp_arr) == 2:
                temp_arr.append(item)
                arr.append(temp_arr)
                temp_arr = []
            else:
                temp_arr.append(item)
        for item in arr:
            d = Data()
            d.total = item[0]
            d.sembuh = item[1]
            d.meninggal = item[2]
            d.aktif = d.total - (d.sembuh + d.meninggal)
            data.append(d)
        return data