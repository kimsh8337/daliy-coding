s = '1 2 3 4'

def solution(s):
    nums = s.split()
    ma = -float('inf')
    mi = float('inf')
    for num in nums:
        if float(num) > float(ma):
            ma = num
        if float(num) < float(mi):
            mi = num

    answer = mi + ' ' + ma

    return answer

print(solution(s))