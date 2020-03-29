# import sys

# sys.stdin = open('input.txt', 'r')

# for T in range(10):
#     Dumps = int(input())
#     Boxes = list(map(int, input().split()))

#     while max(Boxes) -1 > min(Boxes):
#         Boxes[Boxes.index(max(Boxes))] -= 1
#         Boxes[Boxes.index(min(Boxes))] += 1
#         Dumps -= 1
#         if Dumps == 0:
#             break
#     print("#{} {}".format(T+1, max(Boxes)-min(Boxes)))

def min_search():
    minValue = 987654321
    minIdx = -1
    for i in range(len(box)):
        if box[i] < minValue:
            minValue = box[i]
            minIdx = i
        return minIdx

def max_search():
    maxValue = -1
    maxIdx = 0
    for i in range(len(box)):
        if box[i] < maxValue:
            maxValue = box[i]
            maxIdx = i
        return maxIdx

for tc in range(1,11):
    N = int(input())

    box = list(map(int, input().split()))

    for i in range(N):
        box[max_search()] -= 1
        box[min_search()] += 1

    print('#{} {}'.format(tc, box[max_search()]-box[min_search()]))

