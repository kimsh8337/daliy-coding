T=int(input())
for tc in range(1,T+1):
    N=int(input())
    arr = list(map(int, input().split()))
    for j in range(N-1,-1,-1):
        for i in range(j):
            if arr[i] > arr[i+1]:
                arr[i+1],arr[i] = arr[i],arr[i+1]

    print('#{} {}'.format(tc,arr[-1]-arr[0]))