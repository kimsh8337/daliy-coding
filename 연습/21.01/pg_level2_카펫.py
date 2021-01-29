brown = 24
yellow = 24

def solution(brown, yellow):
    for index in range(1, yellow + 1):
        if yellow % index == 0:
            length = yellow//index
            if (((index+2)*(length+2)) - (index * length)) == brown:
                return [max(index+2, length+2), min(index+2,length+2)]

print(solution(brown, yellow))