class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        new_node = Node('head')
        self.head = new_node
        self.tail = new_node
        self.before = None
        self.current = None
        self.cnt = 0

    def first(self):
        if self.cnt == 0: # 빈 리스트인 경우
            return None
        self.before = self.head
        self.current = self.head.next
        return self.current.data

    def next(self):
        self.before = self.current
        self.current = self.current.next
        if self.current is None:
            return None
        return self.current.data


def append(lst, data):
    new_node = Node(data)
    lst.tail.next = new_node
    lst.tail = new_node
    lst.cnt += 1


def insert_list(lst, new_list):
    insert_num = new_list.first()
    num = lst.first()

    for _ in range(lst.cnt):
        if num > insert_num:
            lst.before.next = new_list.head.next
            new_list.tail.next = lst.current
            lst.cnt += new_list.cnt
            break
        num = lst.next()
    else:
        lst.tail.next = new_list.head.next
        lst.cnt += new_list.cnt


def result(lst):
    ans = []
    num = lst.first()
    for i in range(lst.cnt):
        ans.append(num)
        num = lst.next()
    return ans[::-1][0:10]


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    ans = []
    linked_list = LinkedList()
    s = list(map(int, input().split()))
    for i in range(N):
        append(linked_list, s[i])

    for _ in range(M - 1):
        new_list = LinkedList()

        s = list(map(int, input().split()))
        for i in range(N):
            append(new_list, s[i])

        insert_list(linked_list, new_list)

    ans = result(linked_list)

    print('#{}'.format(tc), end=' ')
    for i in ans:
        print(i, end=' ')
    print()