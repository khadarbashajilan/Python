class Node:
	def __init__(self, data):
		self.data=data
		self.next=None

class LinkedList:
	def __init__(self):
		self.head = None

	def append(self,data):
		new_node=Node(data)
		if not self.head:
			self.head = new_node
			return
		curr = self.head
		while curr.next :
			curr = curr.next
		curr.next = new_node

	def print_l(self):
		curr = self.head
		while curr:
			print(curr.data, end=" -> ")
			curr = curr.next
		print("None")

li = LinkedList()
li.append(10)
li.append(20)
li.append(30)
li.print_l()
