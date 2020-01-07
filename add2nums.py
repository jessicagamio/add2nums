class Node(object):
    def __init__(self,data):
        """create node"""
        self.data = data
        self.next = None

class LinkedList(object):
    """create Linked List"""
    def __init__(self):
        self.head = None
        self.tail = None

def add2num(ll1,ll2):
    """add nodes in linked lists and return sum of each node"""
    curr1 = ll1
    curr2 = ll2

    carryover=0

    ll3 = LinkedList()

    while curr1 or curr2:

        if curr1 == None and curr2:
            curr1.data = 0

        elif curr2 == None and curr1:
            curr2.data = 0

        else:
            node = curr1.data + curr2.data + carryover

            # if node has a value in tens place and additional nodes exist carryoverto following node
            if node >= 10 and curr1.next or curr2.next:
                carryover = node//10
                node = node%10

        # if linked list has no node create head node
        if ll3.head == None:
            ll3.head = Node(node)
            ll3.tail = ll3.head
            
        # if no node follows head of linked list add tail
        elif ll3.head.next == None:
            ll3.head.next = Node(node)
            ll3.tail = ll3.head.next

        # if no node exists after tail add new node to tail.next
        else:
            ll3.tail.next = Node(node)
            ll3.tail = ll3.tail.next

        curr1 = curr1.next
        curr2 = curr2.next

    return ll3

ll1 = Node(2)
ll1.next = Node(4)
ll1.next.next = Node(3)

ll2 = Node(5)
ll2.next = Node(6)
ll2.next.next = Node(4)

answer = add2num(ll1,ll2)
