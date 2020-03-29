n = int(input())

ans = 0
for i in range(n):
    s = list(input())
    a = []
    cnt = 0
    for j in range(len(s)):
        if s[j] not in a:
            a.append(s[j])
            cnt += 1
        else:
            if a[-1] ==s[j]:
                continue
            else:
                cnt = 0
                break
    if cnt != 0:
        ans += 1
print(ans)