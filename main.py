print("Введите число в десятичной системе счисления: ")
num = int(input())
bin_num = bin(num)
oct_num = oct(num)
hex_num = hex(num)

print("Число в двоичной системе счисления:", bin_num[2:])
print("Число в восьмеричной системе счисления:", oct_num[2:])
print("Число в шестандцатиричной системе счисления:", hex_num[2:].upper())
