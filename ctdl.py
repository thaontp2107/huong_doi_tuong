class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(10)

new_node = Node(5)
new_node.next = head
head = new_node
 