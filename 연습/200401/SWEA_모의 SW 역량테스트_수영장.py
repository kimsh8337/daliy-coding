import sys
sys.stdin = open('input.txt', 'r')

def backtrack(i=0,sum=0):
    global min_sum
    if i >= 12:
        if min_sum > sum:
            min_sum = sum
        return
    backtrack(i+1,sum+(price[0]*month[i]))
    backtrack(i+1,sum+price[1])
    backtrack(i+3,sum+price[2])
    backtrack(i+12,sum+price[3])


for tc in range(1, 1+int(input())):
    price = list(map(int, input().split()))
    month = list(map(int, input().split()))
    min_sum = 987654321
    backtrack()
    print("#{} {}".format(tc, min_sum))