class CircularQueue:
    def __init__(self, capacity):
        if type(capacity) != int or capacity<=0:
            raise Exception ('Capacity Error')

        self.__items = []
        self.list = self.__items
        self.__capacity = capacity
        self.__count=0
        self.count = self.__count=0
        self.__head=0
        self.__tail=0

    def enqueue(self, item):
        if self.__count == self.__capacity:
            raise Exception('Error: Queue is full')
        if len(self.__items) < self.__capacity:
            self.__items.append(item)
        #?
        else:
            self.__items[self.__tail]=item
        self.__count +=1
        self.__tail=(self.__tail +1) % self.__capacity

    def dequeue(self):
        if self.__count == 0:
            raise Exception('Error: Queue is empty')
        item= self.__items[self.__head]
        self.__items[self.__head]=None
        self.__count -=1
        self.__head=(self.__head+1) % self.__capacity
        return item

    def peek(self):
        if self.__count == 0:
            raise Exception('Error: Queue is empty')
        return self.__items[self.__head]

    def isEmpty(self):
        return self.__count == 0
    # Returns True if the queue is full, and False otherwise:
    def isFull(self):
        return self.__count == self.__capacity

    def size(self):
        return self.__count
    # Returns the capacity of the queue:
    def capacity(self):
        return self.__capacity

    def clear(self):
        self.__items = []
        self.__count=0
        self.__head=0
        self.__tail=0

    def __str__(self):
        #print self.__items
        str_exp = "]"

        i=self.__head
        for j in range(self.__count):
            if j == 0:
                str_exp += str(self.__items[i])
            else:
                str_exp += ','+str(self.__items[i])
            i=(i+1) % self.__capacity
        return str_exp + "]"


    def __repr__(self):
        a = str(self.__items) + ' H=' + str(self.__head) + " T="+str(self.__tail) + " ("
        return a + str(self.__count)+"/"+str(self.__capacity)+")"