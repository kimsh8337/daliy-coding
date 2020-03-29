# def 함수2():
#     print('함수2 시작')
#     print('함수2 끝')
#
# def 함수1():
#     print('함수1 시작')
#     함수2()
#     print('함수1 끝')
#
# print('메인시작')
# 함수1()
# print('메인끝')


# 재귀 함수
# def crush(size):
#     print(size, '망치로 광석을 뿌시는중... 힘드라')
#     if size == 1:
#         print('다부셔버림')
#         return 1
#
#     return crush(size-1) + size
#
# #메인
# print(crush(5))


# factorial 재귀 함수
# def factorial(num):
#     if num == 1:
#         return 1
#     return num*factorial(num-1)
#
# print(factorial(5))


# factorial 반복문
# num = 5
# fact = 1
# for i in range(num,0,-1):
#     fact *= i
#
# print(fact)


# 피보나치 재귀 함수
# def fibo(i):
#     if i < 2:
#         return i
#     return fibo(i-1)+fibo(i-2)
# print(fibo(5))


# 피보나치 memoization
# n = 20
# memo = [0, 1]
#
# def fibo_mz(n):
#     global memo
#     if n >= 2 and len(memo) <= n:
#         memo.append(fibo_mz(n - 1) + fibo_mz(n - 2))
#     return memo[n]
#
# print(fibo_mz(n))
# print(memo)
#
# memo2 = [-1] * (n + 1)
# memo2[0] = 0
# memo2[1] = 1
#
# def fibo(n):
#     if memo2[n] == -1:
#         memo2[n] = fibo(n - 1) + fibo(n - 2)
#     return memo2[n]
#
# print(fibo(n))
# print(memo2)
#
# 피보나치 DP 적용 알고리즘
def fibo_dp(n):
    f = [0,1]

    for i in range(2,n+1):
        f.append(f[i-1]+f[i-2])

    return f[n]
print(fibo_dp(10))
