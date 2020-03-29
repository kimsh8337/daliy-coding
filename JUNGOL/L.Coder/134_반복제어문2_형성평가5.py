num = list(map(int, input().split()))
even_cnt = 0
odd_cnt = 0

for i in range(len(num)):
    if num[i] % 2 == 0:
        even_cnt += 1
    else:
        odd_cnt += 1
print('even : {}'.format(even_cnt))
print('odd : {}'.format(odd_cnt))