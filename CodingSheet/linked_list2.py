class ListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self,node):
        if self.head is None:
            self.head = node
        else:
            cur = self.head
            while True:
                if cur.next is None:
                    break
                cur = cur.next
            cur.next = node

    def printlist(self):
        cur = self.head
        printval = ''
        while True:
            if cur is not None:
                printval += str(cur.data) + '->'
                cur = cur.next
            else:
                printval += 'None'
                break
        print(printval)


l = LinkedList()

l1 = ListNode(2)
l.head = l1

l2 = ListNode(5)
l1.next = l2

l3 = ListNode(10)
l2.next = l3

l3.next = None

l.printlist()

curr = l1
print_val = ''
while True:
    # print(curr.data,'->',)
    print_val += str(curr.data) + '->'
    if curr.next is None:
        print_val += 'None'
        # print('None')
        break
    curr = curr.next
# print(print_val)