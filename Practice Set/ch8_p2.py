def Fahrenheit (n):
    convert = (n * 1.8)+32
    return convert
n = float(input("Enter temperature in celsius: "))
print(Fahrenheit(n))
