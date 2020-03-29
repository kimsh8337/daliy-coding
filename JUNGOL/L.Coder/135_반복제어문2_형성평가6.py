a,b = map(int, input().split())
sum = 0
n = 0
if a < b :
    for i in range(a,b+1):
        if i % 3 == 0 or i % 5 ==0:
            sum += i
            n+=1
else:
    for i in range(b,a+1):
        if i % 3 == 0 or i % 5 ==0:
            sum += i
            n+=1
print('sum : {}'.format(sum))
print('avg : {}'.format(round(sum/n,1)))