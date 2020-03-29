import sys
sys.stdin = open('input.txt', 'r')

while 1:
    a,b,c = map(int,input().split())
    if a == 0 and b==0 and c==0:
        break
    if a<=c and b<=c:
        if c**2 == a**2 + b**2:
            print('right')
        else:
            print('wrong')
    elif a<=b and c<=b:
        if b**2 == a**2 + c**2:
            print('right')
        else:
            print('wrong')
    elif b<=a and c<=a:
        if a**2 == c**2 + b**2:
            print('right')
        else:
            print('wrong')
