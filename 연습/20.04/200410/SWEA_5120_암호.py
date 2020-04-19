class Node:
    def __init__(self, data=0, link=None):
        self.data = data
        self.next = link


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0


def make_list(linked_list):
    ans = []
    cur = linked_list.head

    for _ in range(linked_list.size):
        ans.append(cur.data)
        cur = cur.next

    return ans


def append(linked_list, new_node):
    if linked_list.head is None:
        linked_list.head = linked_list.tail = new_node
    else:
        linked_list.tail.next = new_node
        linked_list.tail = new_node
    linked_list.size += 1


def insert_first(lst, new):
    if lst.head is None:
        lst.head = lst.tail = new
    else:
        new.next = lst.head
        new.data = lst.tail.data + lst.head.data
        lst.head = new
    lst.size += 1


def insert_last(lst, new):
    if lst.head is None:
        lst.head = lst.tail = new
    else:
        lst.tail.next = new
        new.data = lst.tail.data + lst.head.data
        lst.tail = new
    lst.size += 1


def insert_at(linked_list, idx, new_node):
    if idx == 0:
        insert_first(linked_list, new_node)
    if idx == linked_list.size:
        insert_last(linked_list, new_node)
    else:
        pre, cur = linked_list.tail, linked_list.head

        for _ in range(idx):
            pre = cur
            cur = cur.next

        new_node.next = cur
        new_node.data = pre.data + cur.data
        pre.next = new_node

        linked_list.size += 1


for tc in range(1, int(input()) + 1):
    N, M, K = map(int, input().split())
    p = list(map(int, input().split()))

    my_list = LinkedList()
    for i in range(N):
        append(my_list, Node(p[i]))
    my_list.tail.next = my_list.head

    idx = 0
    for i in range(1, K + 1):
        idx += M
        if idx > my_list.size:
            idx = idx % my_list.size
        insert_at(my_list, idx, Node(0))

    ans = make_list(my_list)
    print('#{}'.format(tc), end=' ')
    for num in ans[::-1][:10]:
        print(num, end=' ')
    print()