#13. Write a script to get the maximum and minimum value in a dictionary.
dic = {1: 10, 2: 20, 3: 10, 4: 40, 5: 10, 6: 60}

def maxValue(d):
    return d.get(max(d, key=d.get))

def minValue(d):
    return d.get(min(d, key=d.get))
