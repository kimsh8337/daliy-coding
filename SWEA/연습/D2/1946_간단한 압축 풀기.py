import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 1+int(input())):
    n = int(input())
    x = ''
    li = []
    ans = []
    for _ in range(n):
        a,b = input().split()
        b = int(b)
        li.append(a)
        li.append(b)

    for i in range(0,len(li),2):
        ans.append(li[i]*li[i+1])

    for i in range(len(ans)):
        x += ans[i]

    print('#{}'.format(tc))
    for i in range(0,len(x),10):
        if i+10 <= len(x):
            for j in range(i,i+10):
                print(x[j], end ='')
            print()
        else:
            for j in range(i,len(x)):
                print(x[j], end='')
            print()