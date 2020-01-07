class Node(object):
    def __init__(self,data):
        self.data = data
        self.next = None

def add2num(ll1,ll2):
    curr1 = ll1
    curr2 = ll2

    carryover=0

    ll3 = None

    while curr1 or curr2:

        if curr1 == None and curr2:
            curr1.data = 0

        if curr2 == None and curr1:
            curr2.data = 0

        if curr1 and curr2:
            node = curr1.data + curr2.data + carryover

            if node >= 10:
                carryover = node%10
                node = abs(node/10)

        if ll3 == None:
            ll3 = Node(node)
        else:
            ll3.next = Node(node)
            ll3 = ll3.next

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
print(answer)