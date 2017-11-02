"""9. Write a script to replace last value of tuples in a list.
		Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
		Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']"""
lst = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
print(lst)

i = 0
while i < len(lst):
    if(not len(lst[i])):
        lst.remove(lst[i])
    else:
        i += 1

print(lst)
