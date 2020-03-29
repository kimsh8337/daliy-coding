n = int(input())

for i in range(2*n-1,-1,-2):
    print(' '*((2*n-i)//2),end = '')
    print('*'*i)
for i in range(3,2*n,2):
    print(' '*((2*n-i)//2),end = '')
    print('*'*i)