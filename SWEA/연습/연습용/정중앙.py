char = input()

a = len(char)//2
if len(char)%2 != 0:
    print(char[a])
else:
    print(char[a-1],char[a])
