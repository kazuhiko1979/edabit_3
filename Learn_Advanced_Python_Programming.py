class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.head is None:
            self.head = NewNode
            return

        tail = self.head
        while(tail.next):
            tail = tail.next
        tail.next = NewNode

    def AtStart(self, newdata):
        NewNode = Node(newdata)
        NewNode.next = self.head
        self.head = NewNode

    def Inbetween(self, middle_node, newdata):
        if middle_node is None:
            print('The Mentioned Node does not Exist')
            return

        Newnode = Node(newdata)
        Newnode.next = middle_node.next
        middle_node.next = Newnode



    def listprint(self):
        output = self.head
        while output is not None:
            print(output.data)
            output = output.next

list1 = SLL()
list1.head = Node('Mon')
e2 = Node('Tues')
e3 = Node('Wed')

list1.head.next = e2
e2.next = e3

list1.AtEnd("Thurs")
list1.AtEnd("Fri")
list1.AtStart('Sat')
list1.Inbetween(list1.head,'Sun')
list1.listprint()