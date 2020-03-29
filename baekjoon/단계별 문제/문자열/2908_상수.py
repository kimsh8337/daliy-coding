num = list(map(str, input()))
change = []
change1 = []
change2 = []
ans = 0
for i in range(0,5,4):
    num[i], num[i+2] = num[i+2], num[i]
    for j in range(i,i+3):
        change.append(num[j])
for i in range(3):
    change1.append(change[i])
for i in range(3,6):
    change2.append(change[i])
if change1 < change2:
    ans = change2
else:
    ans = change1
print(''.join(ans))
