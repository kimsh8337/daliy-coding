import sys
sys.stdin=open('input.txt','r')

class Node:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:

    def __init__(self):
        self.head = Node("head")
        self.num = 0

    def leftInsert(self, data):
        new = Node(data)
        beforeNext = self.head.next
        self.head.next = new
        new.next = beforeNext
        self.num += 1

    def search(self, num):
        node = self.head
        cnt = 0
        if self.num < num:
            return -1
        while cnt != num:
            node = node.next
            cnt += 1
        return node

    def insert(self, idx, data):
        new = Node(data)
        fNode = self.search(idx)
        fNodeNext = fNode.next
        fNode.next = new
        new.next = fNodeNext
        self.num += 1

    def delete(self, idx):
        fNode = self.search(idx)
        fNode.next = fNode.next.next
        self.num -= 1

    def change(self, idx, data):
        cNode = self.search(idx+1)
        cNode.data = data


T = int(input())

for TC in range(1, T + 1):
    N, M, L = map(int, input().split())
    li = list(map(int, input().split()))
    Li = LinkedList()
    for i in range(N - 1, -1, -1):
        Li.leftInsert(li[i])

    for i in range(M):
        m = list(map(str, input().split()))
        if m[0] == 'I':
            Li.insert(int(m[1]), int(m[2]))
        elif m[0] == 'D':
            Li.delete(int(m[1]))
        elif m[0] == 'C':
            Li.change(int(m[1]), int(m[2]))

    result = Li.search(L + 1)
    if result != -1:
        print("#{} {}".format(TC, result.data))
    else:
        print("#{} {}".format(TC, result))