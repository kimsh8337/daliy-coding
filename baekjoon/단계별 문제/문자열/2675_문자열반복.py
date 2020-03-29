T=int(input())

for i in range(T):
    n,s = map(str, input().split())
    n = int(n)
    for j in range(len(s)):
        print(s[j]*n, end = '')
    print()