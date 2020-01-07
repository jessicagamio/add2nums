class Node(object):
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

def add2num(ll1,ll2):
    curr1 = ll1
    curr2 = ll2
    curr3 = None

    carryover=0

    ll3 = LinkedList()

    while curr1 or curr2:

        if curr1 == None and curr2:
            curr1.data = 0

        if curr2 == None and curr1:
            curr2.data = 0

        if curr1 and curr2:
            print('curr1 ===',curr1.data)
            print('curr2 ===', curr2.data)
            node = curr1.data + curr2.data + carryover

            if node >= 10:
                carryover = node//10
                print('carry over =', carryover)
                node = node%10
                print('node over 10 =', node)


        if ll3.head == None:
            ll3.head = Node(node)
            print('ll3 head',ll3.head.data)
            
        elif ll3.head.next == None:
            ll3.head.next = Node(node)
            ll3.tail = ll3.head.next

        else:
            ll3.tail.next = Node(node)
            ll3.tail = ll3.tail.next

            print('ll3 tail',ll3.tail.data)

        print('-------------------------')
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

print('ll3 node =', answer.head.data, answer.head.next.data, answer.tail.data)
