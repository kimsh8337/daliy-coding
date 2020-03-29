import sys
sys.stdin = open('input.txt','r')

high = []
result = []
for i in range(9):
    a = int(input())
    high.append(a)
N = len(high)
for i in range(0, N-6):
    for j in range(i+1,N-5):
        for k in range(j+1,N-4):
            for q in range(k+1,N-3):
                for w in range(q+1,N-2):
                    for e in range(w+1,N-1):
                        for r in range(e+1,N):
                            if (high[i]+high[j]+high[k]+high[q]+high[w]+high[e]+high[r]) == 100:
                                answer = [high[i],high[j],high[k],high[q],high[w],high[e],high[r]]
result.append(sorted(answer))
for i in range(7):
    print(result[0][i])