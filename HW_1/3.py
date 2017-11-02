#3. Write a script to sum of the first n positive integers.
n = int(input())
sum = 0
while n:
    sum += n
    n -= 1
print(sum)
