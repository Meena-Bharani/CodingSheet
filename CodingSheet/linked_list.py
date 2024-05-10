class ListNode:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def list_items(self):
        curr_node = self.head

        while curr_node is not None:
            print(curr_node.data , curr_node.next)
            curr_node = curr_node.next

l = LinkedList()
print(l)

l1 = ListNode(10)
l.head = l1
print(l)

l2 = ListNode(20)
l1.next = l2

l3 = ListNode(30)
l2.next = l3
print(l)

l.list_items()