#11. Write a script to remove duplicates from Dictionary.
dic = {1: 10, 2: 20, 3: 10, 4: 40, 5: 10, 6: 60}
result = {}

for key,value in dic.items():
    if value not in result.values():
        result[key] = value
