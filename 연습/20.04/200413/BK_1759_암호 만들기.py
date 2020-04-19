import sys
sys.stdin = open('input.txt','r')

def solve(depth, idx, l, c):
    if depth == l:
        all_out.append(''.join(map(str, out)))
        return
    for i in range(idx, c):
        out.append(alpha[i])
        solve(depth+1, i+1, l, c)
        out.pop()

def password(list_check):
    for i in list_check:
        cons = 0
        vow = 0
        for j in i:
            if j in 'aeiou':
                cons += 1
            else:
                vow += 1
        if cons >= 1 and vow >= 2:
            print(i)
    return

l, c = map(int, input().split())
alpha = list(input().split())
out = []
all_out = []
alpha.sort()

solve(0,0,l,c)
password(all_out)

# 조합 풀이법 - 출력초과
# from itertools import combinations
#
# l,c = map(int,input().split())
# arr = sorted(input().split())
# for s in combinations(arr,l):
#     passwd = ""
#     vowel, consonant = 0, 0
#     for i in range(len(s)):
#         if s[i] in 'aeiou':
#             vowel += 1
#         else:
#             consonant += 1
#         passwd += s[i]
#         if vowel >= 1 and consonant >= 2 and len(passwd) >= 4:
#             print(passwd)