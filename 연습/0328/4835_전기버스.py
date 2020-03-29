import sys
sys.stdin = open('input.txt','r')

for tc in range(1,1+int(input())):
    k,n,m = map(int, input().split())
    charge_stop = list(map(int, input().split()))
    cnt = 0
    nxt = k

    for i in range(m):
        if charge_stop[i]==nxt:
            nxt += k
            cnt += 1
        elif charge_stop[i] > nxt:
            if charge_stop[i-1]+k < charge_stop[i]:
                cnt = 0
                break
            else:
                nxt = charge_stop[i-1]+k
                cnt += 1
        if i == m-1:
            if nxt < n:
                if (charge_stop[i]+k) >= n:
                    cnt += 1
                else:
                    cnt = 0

    print('#{} {}'.format(tc, cnt))