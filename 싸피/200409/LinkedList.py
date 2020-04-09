class Node:
    def __init__(self, d=0, n=None):
        self.data = d
        self.next = n
        # print(self.data, 'make')

    # def __del__(self):
        # print(self.data, 'delete')

arr = []
for i in range(5):
    arr.append(Node(i))


class LinkedList:
    def __init__(self):
        self.head = None    # 첫 번째 노드
        self.tail = None    # 마지막 노드
        self.size = 0       # 노드의 수

mylist = LinkedList()

def printList(lst):  # lst : LinkedList객체
    if lst.head is None: return   # 빈 리스트 일 경우

    cur = lst.head
    # print(cur.data)
    #
    # cur = cur.next
    # print(cur.data)
    print(lst.size, '[', end=' ')

    while cur is not None:
        print(cur.data, end=' ')
        cur = cur.next

    print(']')

# n5 = Node(5); n4 = Node(4, n5); n3 = Node(3, n4)
# n2 = Node(2, n3); n1 = Node(1, n2)
# mylist.head = n1; mylist.size = 5

def insertLast(lst, new):   # new : 새로 추가할 노드 객체
    # 빈 리스트일 경우
    if lst.head is None:
        lst.head = lst.tail = new
    else:
        # 마지막 노드 를 찾는다
        # cur = lst.head
        # while cur.next is not None:
        #     cur = cur.next
        # cur.next = new
        lst.tail.next = new
        lst.tail = new

    lst.size += 1

def deleteLast(lst):
    if lst.head is None: return

    pre, cur = None, lst.head
    while cur.next is not None:
        pre = cur
        cur = cur.next

    if pre is None:
        lst.head = lst.tail = None
    else:
        pre.next = None
        lst.tail = pre
    lst.size -= 1

def insertFirst(lst,new):
    if lst.head is None:
        lst.head = lst.tail = new
    else:
        new.next = lst.head
        lst.head = new

    lst.size += 1

def deletFirst(lst):
    if lst.head is None: return

    # 노드가 1개일 경우 주의한다.
    lst.heaad = lst.head.next
    if lst.head is None:
        lst.tail = None

    lst.size -= 1

def insertAt(lst, idx, new):
    # 빈 리스트일 경우, idx == 0
    if lst.head is None or idx == 0:
        insertFirst(lst, new)
    # 마지막 추가하는 경우 idx >= lst.size
    elif idx >= lst.size:
        insertLast(lst, new)
    # 중간에 추가하는 경우
    else:
        pre,cur = None, list.head
        for _ in range(idx):
            pre = cur
            cur = cur.next
        new.next = cur
        pre.next = new
        lst.size += 1

for i in range(5):
    insertLast(mylist, Node(i))
    printList(mylist)

for i in range(3):
    insertAt(mylist, 2 ,Node(i+10))
    printList(mylist)

# while mylist.size:
#     deleteLast(mylist)
#     printList(mylist)