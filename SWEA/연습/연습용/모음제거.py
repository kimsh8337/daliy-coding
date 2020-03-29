my_str = 'Life is too short, you need python'
vowels = 'aeiou'

result = ''
for i in my_str:
    if i not in vowels:
        result += i
print(result)