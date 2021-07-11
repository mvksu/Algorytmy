class Node:
    def __init__(self, x):
        self.key = x
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None

    def listInsert(self, x):
        x.next = self.head
        if self.head != None:
            self.head.prev = x
        self.head = x
        x.prev = None

    def listPrint(self):
        x = self.head
        while x:
            print(x.key, end=' ')
            x = x.next

    def listSearch(self, k):
        x = self.head
        while x != None and x.key != k:
            x = x.next
        return x

    def listDelete(self, x):
        if x.prev != None:
            x.prev.next = x.next
        else:
            self.head = x.next
        if x.next != None:
            x.next.prev = x.prev

    def copy(self):
        x = self.head
        newList = LinkedList()
        while x:
            a = x
            node = Node(x.key)
            while a.next:
                if node.key == a.next.key:
                    print('1')
                    node.next = node.next.next
                else:
                    print('2')
                    newList.listInsert(node)
                    node = node.next
            x = x.next
        newList.listPrint()

def newList(l):
    newList = LinkedList()
    x = l.head
    while x is not None:
        if newList.listSearch(x.key) == None:
            newList.listInsert(Node(x.key))
        x = x.next
    return newList

def scal(l1, l2):
    l3 = LinkedList()
    x = l1.head
    while x is not None:
        l3.listInsert(Node(x.key))
        x = x.next

    x = l2.head
    while x is not None:
        l3.listInsert(Node(x.key))
        x = x.next
    return l3


# l = LinkedList()
# l.listInsert(Node(1))
# l.listInsert(Node(2))
# l.listInsert(Node(2))
# l.listInsert(Node(3))
# l.listInsert(Node(1))
# l.listInsert(Node(2))
# l.listInsert(Node(2))
# l.listInsert(Node(5))
#
# l.listPrint()
# print("")
# l.listDelete(l.listSearch(5))
# l.listPrint()
# print("")
# newList(l).listPrint()
# print("")
# scal(l, newList(l)).listPrint()

l = LinkedList()
l.listInsert(Node('raz'))
l.listInsert(Node('dwa'))
l.listInsert(Node('trzy'))
l.listInsert(Node('trzy'))
l.listPrint()
print("")
newList(l).listPrint()










