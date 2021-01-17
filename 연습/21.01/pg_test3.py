board = [[1,1,4,3], [3,2,1,4], [3,1,4,2], [2,1,3,3]]
# board = [[1,2,1,2], [3,4,3,4], [1,2,1,2], [3,4,3,4]]

dr = [1,0,-1,0]
dc = [0,1,0,-1]

def solution(board):
    def check(r,c):
        nonlocal answer

        for a in range(4):
            nr = r + dr[a]
            nc = c + dc[a]
            if 0<=nr<len(board) and 0<=nc<len(board):
                board[r][c], board[nr][nc] = board[nr][nc], board[r][c]
                if 0<=r+2<len(board) and board[r][c] == board[r+1][c] and board[r][c] == board[r+2][c]:
                    answer += 1
                elif 0<=r-2<len(board) and board[r][c] == board[r-1][c] and board[r][c] == board[r-2][c] :
                    answer += 1
                elif 0<=c+2<len(board) and board[r][c] == board[r][c+1] and board[r][c] == board[r][c+2]:
                    answer += 1
                elif 0<=c-2<len(board) and board[r][c] == board[r][c-1] and board[r][c] == board[r][c-2]:
                    answer += 1
                elif 0<=r-1<len(board) and 0<=r+1<len(board) and board[r][c] == board[r-1][c] and board[r][c] == board[r+1][c]:
                    answer += 1
                elif 0<=c-1<len(board) and 0<=c+1<len(board) and board[r][c] == board[r][c-1] and board[r][c] == board[r][c+1]:
                    answer += 1
                board[r][c], board[nr][nc] = board[nr][nc], board[r][c]
        return

    answer = 0

    for i in range(len(board)):
        for j in range(len(board)):
            check(i,j)

    if answer == 0:
        answer = -1
    return answer

print(solution(board))