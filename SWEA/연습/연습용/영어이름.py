name = input()
names = name.split()

for i in range(1, len(names)-1):
    print(names[i])
    names[i]=names[i][0]+'.'

print(names)
print(' '.join(names))