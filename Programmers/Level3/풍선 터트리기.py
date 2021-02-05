# a = [9, -1, -5]
a = [-16,27,65,-2,58,-92,-71,-68,-61,-33]

def solution(a):
    answer = 1
    l = 0
    r = len(a)-1
    leftMin = a[l]
    rightMin = a[r]

    while l<r:
        if leftMin < rightMin:
            r -= 1
            if rightMin > a[r]:
                answer += 1
            rightMin = min(rightMin, a[r])
        else:
            l += 1
            if leftMin > a[l]:
                answer += 1
            leftMin = min(leftMin, a[l])

    return answer

print(solution(a))