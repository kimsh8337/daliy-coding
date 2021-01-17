board = [[1,1,4,3], [3,2,1,4], [3,1,4,2], [2,1,3,3]]

var dr = [1,0,-1,0]
var dc = [0,1,0,-1]

function solution(board) {
    function check(r,c){
        var len = board.length
        var a = 0;
        var nr, nc = 0;
        var temp = 0;

        for (a=0;a<4;a++){
            nr = r + dr[a]
            nc = c + dc[a]
            if(0<=nr<len && 0<=nc<len){
                temp = board[r][c]
                board[r][c] = board[nr][nc]
                board[nr][nc] = temp
                if((0<=r+2<len) && (board[r][c] == board[r+1][c]) && (board[r][c] == board[r+2][c])){
                    answer += 1
                }else if((0<=r-2<len) && (board[r][c] == board[r-1][c]) && (board[r][c] == board[r-2][c])){
                    answer += 1
                }else if((0<=c+2<len) && (board[r][c] == board[r][c+1]) && (board[r][c] == board[r][c+2])){
                    answer += 1
                }else if((0<=c-2<len) && (board[r][c] == board[r][c-1]) && (board[r][c] == board[r][c-2])){
                    answer += 1
                }else if((0<=r-1<len) && (0<=r+1<len) && (board[r][c] == board[r-1][c]) && (board[r][c] == board[r+1][c])){
                    answer += 1
                }else if((0<=c-1<len) && (0<=c+1<len) && (board[r][c] == board[r][c-1]) && (board[r][c] == board[r][c+1])){
                    answer += 1
                }
                temp = board[r][c]
                board[r][c] = board[nr][nc]
                board[nr][nc] = temp
            }
        }
        return

    }

    var answer = 0;
    var i,j = 0;

    for (i=0;i<board.length;i++){
        for (j=0;j<board.length;j++){
            check(i,j)
        }
    }

    if (answer == 0){
        answer = -1
    }
    
    return answer;
}

console.log(solution(board))