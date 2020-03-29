s = input()
sum = 0
for i in range(len(s)):
    if s[i] == 'A' or s[i] == 'B' or s[i] == 'C':
        sum += 3
    elif s[i] == 'D' or s[i] == 'E' or s[i] == 'F':
        sum += 4
    elif s[i] == 'G' or s[i] == 'H' or s[i] == 'I':
        sum += 5
    elif s[i] == 'J' or s[i] == 'K' or s[i] == 'L':
        sum += 6
    elif s[i] == 'M' or s[i] == 'N' or s[i] == 'O':
        sum += 7
    elif s[i] == 'P' or s[i] == 'Q' or s[i] == 'R' or s[i] == 'S':
        sum += 8
    elif s[i] == 'T' or s[i] == 'U' or s[i] == 'V':
        sum += 9
    elif s[i] == 'W' or s[i] == 'X' or s[i] == 'Y' or s[i] == 'Z':
        sum += 10
print(sum)
