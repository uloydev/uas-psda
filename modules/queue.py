class Queue :
    def __init__(self):
        self.queue = []
        self.size = 0
    def empty(self):
        return self.size == 0
    
    def push(self, data):
        self.queue.append(data)
        self.size += 1
    
    def pop(self):
        if self.empty() == True:
            print("queue Empty")
            return
        else:
            self.size -= 1
            return self.queue.pop(0)