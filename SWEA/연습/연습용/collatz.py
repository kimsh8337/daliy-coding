def collatz(num):
    cnt = 0
    while num != 1:
        cnt += 1
        if num % 2 == 0:
            num = num / 2
        else:
            num = num*3+1
        if cnt == 500:
            cnt = -1
            break
    return cnt

print(collatz(6))
print(collatz(16))
print(collatz(27))
print(collatz(626331))