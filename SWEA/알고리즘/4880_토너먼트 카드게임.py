import sys
sys.stdin=open('input.txt','r')

def game(x,y):
    if (num[x]==1 and num[y]==3) or (num[x]==2 and num[y]==1) or (num[x]==3 and num[y]==2):
        return x
    elif (num[x]==3 and num[y]==1) or (num[x]==1 and num[y]==2) or (num[x]==2 and num[y]==3):
        return y
    elif (num[x]==1 and num[y]==1) or (num[x]==2 and num[y]==2) or (num[x]==3 and num[y]==3):
        return x

def getmin(x,y):
    if x == y:
        return x
    mid = (x+y)>>1
    l = getmin(x,mid)
    r = getmin(mid+1,y)
    return game(l,r)

for tc in range(1,1+int(input())):
    n = int(input())
    num = list(map(int, input().split()))
    ans = getmin(0,n-1)
    print('#{} {}'.format(tc, ans+1))