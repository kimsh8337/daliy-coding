import sys
sys.stdin = open('input.txt', 'r')

a = list(input())
b = list(input())
c = 0
ans = []
ans_sum = []
for i in range(-1,-len(b)-1,-1):
    num = 1
    for j in range(-1,-len(a)-1,-1):
        if j == -1:
            c = (int(b[i])*int(a[j]))
        else:
            c += (int(b[i]) * int(a[j])) * (10 ** num)
            num += 1
    ans.append(c)
for i in range(len(ans)):
    print(ans[i])
    c = ans[i]*(10**i)
    ans_sum.append(c)
print(sum(ans_sum))