import sys
sys.stdin = open('input.txt','r')

n = int(input())
cnt = 1
a=1
num = 1

while n > a:
    a += num*6
    cnt+=1
    num+=1
print(cnt)