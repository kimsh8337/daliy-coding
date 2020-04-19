def push(item):
    global hsize
    hsize += 1
    H[hsize] = item
    c, p = hsize, hsize // 2
    while p and H[p] > H[c]:
        H[p], H[c] = H[c], H[p]
        c = p
        p = c // 2


for tc in range(1, int(input()) + 1):
    N = int(input())
    node = list(map(int, input().split()))
    hsize = 0  # 힙에 저장된 자료의 수, 마지막 노드의 인덱스
    H = [0] * (N + 1)  # 완전 이진 트리로 저장
    for i in node:
        push(i)
    ans = 0
    while N:
        ans += H[N // 2]
        N //= 2
    print('#{} {}'.format(tc, ans))