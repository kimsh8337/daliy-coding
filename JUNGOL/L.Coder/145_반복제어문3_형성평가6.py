n = int(input())

for i in range(1,n+1):
    print('  '*(n-i),end='')
    for j in range(1,i+1):
        print(j,end=' ')
    print()

# num = 1
# for i in range(n + 1, -1, -2):
#     print(' ' * i, end='')
#     for j in range(1,num+1):
#         print(j, end=' ')
#     num += 1
#     print()