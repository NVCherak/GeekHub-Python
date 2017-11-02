"""5. Write a script to convert decimal to hexadecimal
		Sample decimal number: 30, 4
		Expected output: 1e, 04"""
numbers = input()
lst = numbers.split(", ")
str = ""
for i in lst:
    str = hex(int(i))
    print(str[2:], end = ", ")
print()
