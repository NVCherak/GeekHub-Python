import random, time # Import libraries to use the rando and timer

def get_list_rand_int(extend):
    # list generation function for 10,000 items
    lst = []
    for i in range(extend):
        # extend iterations
        lst.append(random.randint(0, 99)) # add a random element from 0 to 99 in the list

    return lst # return a list of items

def get_list_rand_float(extend):
    # function of generating fractional numbers
    lst = []
    for i in range(extend):
        lst.append(random.uniform(0, 99))

    return lst

def selection_sort(lst):
    # sort function by choice
    idSwapEl = 0 # element identifier
    extend = len(lst)

    for i in range(extend):
        # the loop until "i" is less than the length of the list
        minEl = lst[i] # minimal element of the array - current *
        for j in range(i+1, extend):
            # cycle from the current element to the end of the array
            if minEl > lst[j]:
                # if the minimum element is greater than the checked
                minEl = lst[j]
                # assign the checked item as the minimum
                idSwapEl = j
                # remember its index
        lst[idSwapEl] = lst[i]
        # exchange of the smallest item with the current*
        lst[i] = minEl

    return lst

def insertion_sort(lst):
    # sorting function by insertion
    newLst = [lst[0],]  # to the new list, I assigned the first element of the initial list
    extend = len(lst)

    for i in range(extend):
        j = i
        value = lst[i] # current value
        while j:
            # loop from the end of the new list until "j" is not zero
            if newLst[j-1] > value:
                # if the item is larger than the current tab
                j -= 1 # go further from the end of the list
            else:
                # if less, then we go out of check
                break
        newLst.insert(j, value) # insert the current element after the element is smaller than the value

    return newLst

def bubble_sort(lst):
    # bubble sort function
    sizeLst = len(lst)-1 # the size of the list

    for i in range(sizeLst):
        # cycle to the penultimate element of the array
        for j in range(sizeLst):
            # cycle from beginning to end of the list
            if lst[j] > lst[j+1]:
                # if the current item is greater than the next
                lst[j], lst[j+1] = lst[j+1], lst[j] # обмін елементів
        sizeLst -= 1 # at the end of the array are the largest elements that need not be checked

    return(lst)

def default_sort(lst):
    lst.sort() # sort the array

    return lst

def testing(name_sort, firstLst, secondLst):
    print("------------------------|-----------------------|------------------|")
    start_time = time.time() # remember the initial time before executing the script
    name_sort(firstLst)
    print(name_sort.__name__, "(int)\t|  %3.4f seconds\t|  yes             |" % (time.time() - start_time))

    start_time = time.time()
    name_sort(secondLst)
    print(name_sort.__name__, "(float)\t|  %3.4f seconds\t|  yes             |" % (time.time() - start_time))

extend = 10000
lstInt = get_list_rand_int(extend)
lstFloat = get_list_rand_float(extend)

print("___________________________________________________________________")
print("Name algorithm          |  Calculation time     | Sorted correctly |")
testing(selection_sort, lstInt, lstFloat)
testing(insertion_sort, lstInt, lstFloat)
testing(bubble_sort, lstInt, lstFloat)
testing(default_sort, lstInt, lstFloat)
print("-------------------------------------------------------------------")
