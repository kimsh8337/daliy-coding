import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
prime_num = [1]

for tc in range(T):
    n = int(input())
    for i in range(2,1000):
        cnt = 0
        for j in range(2,i+1):
            if i%j == 0:
                cnt += 1
                if cnt >1:
                    break
        if cnt == 1:
            prime_num.append(i)

    for i in range(len(prime_num)):
        for j in range(len(prime_num)):
            if prime_num[i]+prime_num[j] == n:
                if prime_num[i] > prime_num[j]:
                    if min(prime_num[i] - prime_num[j]):
                        print(prime_num[j],prime_num[i])
                else:
                    if min(prime_num[j] - prime_num[i]):
                        print(prime_num[i], prime_num[j])