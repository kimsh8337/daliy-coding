import sys
sys.stdin = open('input.txt', 'r')

nums = list(map(int, input().split()))

if nums[0] == 1:
    num = 1
    for i in range(1,8):
        if nums[i] == num + 1:
            num += 1
            continue
        else:
            print('mixed')
            break
    if num == 8:
        print('ascending')

elif nums[0] == 8:
    num = 8
    for i in range(1,8):
        if nums[i] == num -1:
            num -= 1
            continue
        else:
            print('mixed')
            break
    if num == 1:
        print('descending')

else:
    print('mixed')