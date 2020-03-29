def my_abs(num):
    if type(num) == complex:
        return (num.real**2+num.imag**2)**(1/2)
    else:
        if num >= 0:
            return num
        else:
            return -num

print(my_abs(3+4j), my_abs(0.0), my_abs(-5))
