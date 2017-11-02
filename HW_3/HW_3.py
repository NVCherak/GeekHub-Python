import random

def get_list_rand_int():
    lst = []
    for i in range(10):
        lst.append(random.randint(0, 99))
    print(lst)
    return lst

def get_list_rand_float():
    lst = []
    for i in range(10):
        lst.append(random.uniform(0, 99))
    print(lst)
    return lst

def selection_sort(lst):
    idSwapEl = 0

    for i in range(0, len(lst)):
        minEl = lst[i]
        for j in range(i+1, len(lst)):
            if minEl > lst[j]:
                minEl = lst[j]
                idSwapEl = j
        lst[idSwapEl] = lst[i]
        lst[i] = minEl

    return lst

def insertion_sort(lst):
    newLst = [lst[0],]
    for i in range(1, len(lst)):
        j = i
        value = lst[i]
        while j:
            if newLst[j-1] > value:
                j -= 1
            else:
                break
        newLst.insert(j, value)

    print(newLst)

insertion_sort(get_list_rand_int())
