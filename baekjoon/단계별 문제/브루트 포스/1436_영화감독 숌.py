import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
a = 666

while n:
    if '666' in str(a):
        n -= 1
    a += 1
print(a-1)
