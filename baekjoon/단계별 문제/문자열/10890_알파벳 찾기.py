s = input()
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
cnt =[-3]*26
for i in range(len(s)):
    for j in range(26):
        if alpha[j] in s[i]:
            if cnt[j] == -3:
                cnt[j] = i
            else:
                continue
        if alpha[j] not in s:
            cnt[j] = -1
for i in range(len(cnt)):
    print(cnt[i], end = ' ')

