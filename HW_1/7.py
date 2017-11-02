#7. Write a script to concatenate all elements in a list into a string and print it.
str = input("Enter something through the spacebar: ")
lst = str.split(" ")
concatenateStr = ""
for i in lst:
    concatenateStr += i
print(concatenateStr)
