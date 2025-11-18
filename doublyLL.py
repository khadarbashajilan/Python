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

    def add_beg(self,data):
        new_node = Node(data)
        if not self.head:
            self.head=new_node
            self.tail=new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head=new_node

    def delete_node(self,data):
        if not self.head:
            return "Empty DLL"
        
        elif self.head.data == data :
            temp = self.head.next
            self.head.next.prev = None
            self.head.next = None
            self.head = temp
            return

        elif self.tail.data == data:
            temp = self.tail.prev
            self.tail.prev.next = None
            self.tail.prev = None
            self.tail = temp
            return
          
        else:
            dummy = Node()
            curr= self.head
            dummy.next = curr

            while curr:
                if curr.data == data:
                    curr.prev.next = curr.next.next
                curr = curr.next
            dummy.next = self.head





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
print()
li.add_beg(10)
li.printAll()
li.delete_node(2)
li.printAll()