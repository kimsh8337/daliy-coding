px = [2,3,10,2,4,8,1]

def maxDifference(px):
    ans = 0
    min = px[0]

    for i in range(1,len(px)):
        if min > px[i]:
            min = px[i]
        else:
            if ans < (px[i] - min):
                ans = px[i] - min
        # for j in range(0,i):
        #     if px[i] > px[j] and ans < (px[i] - px[j]):
        #         ans = px[i] - px[j]
    if ans == 0:
        ans = -1

    return ans

print(maxDifference(px))