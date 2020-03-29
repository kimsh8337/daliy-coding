def self_number(n):
    num = []
    for i in range(1,n+1):
        num.append(i)
    a = []
    for k in range(1,n+1):
        sum = 0
        str1 = str(k)
        b=0
        for i in range(len(str1)):
            b += int(str1[i])
            sum = k+b
        a.append(sum)
    for x in range(len(num)):
        if num[x] not in a:
            print(num[x])

self_number(10000)