s = " 3people unFollowed me "

def solution(s):
    answer = ''

    sentences = s.split(' ')
    print(sentences)

    for sentence in sentences:
        answer += ' ' + sentence.capitalize()

    return answer[1:]

print(solution(s))