import sys
sys.stdin = open('input.txt', 'r')

dic = {'0':0,'1':1, '2':2, '3':3, '4':4,'5':5,'6':6,'7':7,'8':8, '9':9, 'A':10,'B':11,'C':12, 'D':13,'E':14,'F':15}

def binary(num):
    global tmp
    x,y = 0, 0
    for i in range(4):
        x = num//2
        y = num % 2
        tmp = str(y) + tmp
        num = x
    return tmp


for tc in range(1,int(input())+1):
    n,num = input().split()
    ans = ''
    for i in num:
        tmp=''
        binary(dic[i])
        ans += tmp
    print('#{} {}'.format(tc,ans))