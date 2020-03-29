def same_diff(n):
    num = []
    cnt = 0
    for i in range(1, n+1):
        num.append(i)
    a=[]
    for k in range(1,n+1):
        str1 = str(k)
        if len(str1) == 3:
            for i in range(len(str1)):
                for j in range(1,len(str1)+1):
                    for z in range(2,len(str1)+2):
                        if str1[i] <= str1[j]:
                            if str1[j] <= str1[z]:
                                a.append(k)
        elif len(str1) == 2:
            for i in range(len(str1)):
                for j in range(1,len(str1)+1):
                    if str1[i] <= str1[j]:
                            a.append(k)
        elif len(str1) == 1:
            a.append(k)
    for i in range(len(a)):
        cnt += 1
    return cnt
n = int(input())
print(same_diff(n))



