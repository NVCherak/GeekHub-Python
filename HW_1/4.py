#4. Write a script to concatenate N strings.
num = int(input("Number of strings: "))
lst = []
str = ""
for i in range(num):
    lst.append(input("String: "))
    str += lst[i]
print("Concatenate string is:", str)
