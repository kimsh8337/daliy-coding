import sys
sys.stdin = open('input.txt','r')

s = input()
# print(s)
check = []
cnt = 0

for i in range(len(s)):
    if s not in check:
        for j in range(i+1,i+2):
            if 'c=' in s[i]:
                check.append(s[i])
                check.append(s[j])
                cnt += 1
            elif 'c-' in s[i]:
                check.append(s[i])
                check.append(s[j])
                cnt += 1
            elif 'dz=' in s[i]:
                check.append(s[i])
                check.append(s[j])
                cnt += 1
            elif 'd-' in s[i]:
                check.append(s[i])
                check.append(s[j])
                cnt += 1
            elif 'lj' in s[i]:
                check.append(s[i])
                check.append(s[j])
                cnt += 1
            elif 'nj' in s[i]:
                check.append(s[i])
                check.append(s[j])
                cnt += 1
            elif 's=' in s[i]:
                check.append(s[i])
                check.append(s[j])
                cnt += 1
            elif 'z=' in s[i]:
                check.append(s[i])
                check.append(s[j])
                cnt += 1
    else:
        continue
print(cnt)

