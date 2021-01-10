begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]

def solution(begin, target, words):
    answer = 0
    visited = [0] * len(words)

    def dfs(now, cnt):
        nonlocal answer

        if now == target:
            if answer > cnt or answer == 0:
                answer = cnt
            return

        for i in range(len(words)):
            check = 0
            if visited[i] == 1:
                continue
            for j in range(len(now)):
                if now[j] == words[i][j] and visited[i] == 0:
                    check += 1
            if check == len(now)-1:
                visited[i] = 1
                dfs(words[i],cnt+1)
                visited[i] = 0

    if target not in words:
        return answer
    else:
        dfs(begin,0)

    return answer

print(solution(begin, target, words))