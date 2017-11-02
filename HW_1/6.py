"""6. Write a script to check whether a specified value is contained in a group of values.
		Test Data :
		3 -> [1, 5, 8, 3] : True
		-1 -> (1, 5, 8, 3) : False"""
inp = input()
lst = inp.split(" -> ")
st = set(lst[1])
print(lst[0] in st)
