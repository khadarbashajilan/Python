class Node:
    def __init__(self,data=0):
        self.data = data
        self.prev = None
        self.next = None

class DoublyL:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node


    def prepend(self,data):
        new_node = Node(data)
        if not self.head:
            self.head=new_node
            self.tail=new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head=new_node


    def append_at(self, idx, data):
        new_node = Node(data)
        curr = self.head
        pt = 0
        while curr:
            if pt == idx:
                # if idx = 0 / head
                if curr == self.head:
                    new_node.next = self.head
                    self.head.prev = new_node
                    self.head = new_node
                    return
                #  if idx = n / tail
                if curr == self.tail:
                    new_node.next = self.tail
                    new_node.prev = self.tail.prev
                    self.tail.prev.next = new_node
                    return

                # if idx is middle on ll
                curr.prev.next = new_node
                new_node.next = curr
                new_node.prev = curr.prev
                curr.prev = new_node
                return
            curr = curr.next
            pt += 1


    def delete_node(self,data):
        if not self.head:
            return "Empty DLL"
        
        curr = self.head

        while curr:
            if curr.data == data:
                # Single node
                if curr == self.head and self.tail == curr:
                    self.tail = self.head = None
                    return
                
                # at head:
                if self.head == curr:
                    self.head = curr.next
                    self.head.prev = None
                    return
                # at tail
                if self.tail == curr:
                    self.tail = curr.prev
                    self.tail.next = None
                    return
                
                #at middle:
                curr.prev.next = curr.next
                curr.next.prev = curr.prev
                return
            curr = curr.next


    def delete_at(self,idx):
        if not self.head:
            return "Empty DLL"
        curr = self.head
        count = 0
        while curr:
            if count == idx:
                if curr == self.head and curr == self.tail:
                    self.tail = self.head = None
                    return

                if curr == self.head:
                    self.head = curr.next
                    self.head.prev = None
                    return
                if curr == self.tail:
                    self.tail = curr.prev
                    self.tail.next = None
                    return
                
                curr.prev.next = curr.next
                # curr.next = curr.prev = None
            curr = curr.next
            count += 1

                
    def reverse(self):
        if not self.head:
            return "Empty DLL"
        curr = self.head
        prev_node = None

        while curr:
            curr.prev, curr.next = curr.next, curr.prev
            prev_node = curr
            curr  = curr.prev
        self.head, self.tail = self.tail, self.head


    def printAll(self):
        curr = self.head
        while curr:
            print(curr.data, end=" <=> ")
            curr=curr.next
        print(None)

        
li = DoublyL()
li.append(1)
li.append(2)
li.append(3)
li.append(4)
li.printAll()
li.reverse()
li.printAll()