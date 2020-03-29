def my_all(arg):
    if len(arg) == 0:
        return True
    for item in arg:
        if not item:
            return False
    return True
    
print(my_all([]))
print(my_all([1, 2, 5, '6']))
print(my_all([[], 2, 5, '6']))