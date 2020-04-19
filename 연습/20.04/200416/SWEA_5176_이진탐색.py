for tc in range(1,int(input())+1):
    N=int(input())
    T=[0]*(N+1)
    cnt=1
    def inorder(idx):
        if idx > N: return
        inorder(idx*2)
        global cnt
        T[idx]=cnt;cnt+=1

        inorder(idx*2+1)
    inorder(1)
    print(T[1],T[N//2])