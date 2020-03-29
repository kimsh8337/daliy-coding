# T = int(input())
# for i in range(T):
#     cnt = 0
#     K, N, M = map(int, input().split())
#     nxt = K
#     charge = list(map(int, input().split()))
#     for j in range(M):
#         if charge[j] == nxt:
#             nxt += K
#             cnt += 1
#         elif charge[j] > nxt:
#             if charge[j-1]+K < charge[j]:
#                 cnt = 0
#                 break
#             else:
#                 nxt = charge[j-1]+K
#                 cnt += 1
#         if j == M-1:
#             if nxt < N:
#                 if (charge[j] + K) >= N:
#                     cnt += 1
#                 else:
#                     cnt = 0
#     print("#{0} {1}".format(i+1, cnt))

'''
1. 전체 버스정류장 수만큼 리스트 만들기
2. 충전소가 있는 위치 표시해두기(ex:1로)

3. 몇번 반복을 해야되는지 횟수를 모르니 while으로 돌기
4. 현재 나의 위치에서 k만큼 이동(최소 충전횟수를 구하므로 일단 연료 다써서 이동)
4.1 만약 내 위치가 정류장 끝과 같거나 넘겨버리면 통과 정답출력
5. 충전소가 있으면(땡큐) 없으면 이동한 연료만큼 뒤로 이동하면서 충전소 찾기
6. 충전소가 없으면 답이 없음. 0출력
7. 있으면 그자리로 내위치 변경 후 충전회수도 증가
'''
T = int(input())

for tc in range(1,T+1):
    K,N,M = map(int, input().split())

    tmp = list(map(int, input().split()))
    charge =[0]*(N+1)

    for i in range(len(tmp)):
        charge[tmp[i]] = 1

    pos = 0
    cnt = 0

    while 1:
        flag = False
        pos += K
        if pos >= N:
            break

        for i in range(pos, pos-K, -1):
            if charge[i] == 1:
                cnt += 1
                pos = i
                flag = True
                break
        if not flag:
            cnt = 0
            break

    print('#{} {}'.format(tc, cnt))





