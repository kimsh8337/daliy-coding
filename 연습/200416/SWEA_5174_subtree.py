import sys
sys.stdin = open('input.txt','r')

for tc in range(1,int(input())+1):
    E,N = map(int,input().split())
    arr = list(map(int,input().split()))
    L=[0]*(E+2)
    R=[0]*(E+2)
    for i in range(0,len(arr),2):
        p,c=arr[i],arr[i+1]
        if L[p]:R[p]=c
        else: L[p]=c

    def subTree(v):

        if v==0: return 0

        l=subTree(L[v])
        r=subTree(R[v])
        return l+r+1

    print(subTree(N))