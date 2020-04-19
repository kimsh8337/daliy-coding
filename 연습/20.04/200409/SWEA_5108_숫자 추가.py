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
        self.num +=1


T = int(input())

for TC in range(1, T + 1):
    N, M, L = map(int, input().split())
    li = list(map(int, input().split()))
    Li = LinkedList()
    for i in range(N-1,-1,-1):
        Li.leftInsert(li[i])

    for i in range(M):
        m_idx, m_value = map(int, input().split())
        Li.insert(m_idx, m_value)

    print("#{} {}".format(TC, (Li.search(L)).next.data))