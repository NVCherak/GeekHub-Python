import random, time # імпортуємо бібліотеки для використання рандому та таймера часу

start_time = time.time() # запам'ятовуємо початковий час до виконання скрипта

def get_list_rand_int():
    # функція генерування списку на 10000 елементів
    lst = []
    for i in range(10000):
        # 10000 итерацій
        lst.append(random.randint(0, 99)) # додаємо в список випадковий елемент від 0 до 99

    return lst # повертаємо список елементів

def get_list_rand_float():
    # така жсама функція лише з дробовими числами
    lst = []
    for i in range(10000):
        lst.append(random.uniform(0, 99))

    return lst

def selection_sort(lst):
    # функція сортування вибором
    idSwapEl = 0 # ідентифікатор елемента

    for i in range(len(lst)):
        # цикл поки "i" менше довжини списку
        minEl = lst[i] # мінімальний елемент масиву, поточний*
        for j in range(i+1, len(lst)):
            # цикл від поточного елементу до кінця масиву
            if minEl > lst[j]:
                # якщо мінімальний елемент більший за перевіряємий
                minEl = lst[j]
                # присвоюємо перевіряємий елемент як мінімальний
                idSwapEl = j
                # запам'ятовуємо його індекс
        lst[idSwapEl] = lst[i]
        # обмін найменшого елемента з поточним*
        lst[i] = minEl

    return lst

def insertion_sort(lst):
    # функція сортування вставкою
    newLst = [lst[0],]  # новому списку присвоюєм перший елемент початкового списку

    for i in range(len(lst)):
        j = i
        value = lst[i] # поточне значення
        while j:
            # цикл з кінця нового списку поки j не дорівнює нулю
            if newLst[j-1] > value:
                # якщо елемент більше поточного начення
                j -= 1 # йдем далі від кінця списку
            else:
                # якщо менше, то виходимо з перевірки
                break
        newLst.insert(j, value) # вставляємо поточний елемент після елемена меншого за значенням

    return newLst

def bubble_sort(lst):
    # функція сортування бульбашкою
    sizeLst = len(lst)-1 # розмір списку

    for i in range(len(lst)-1):
        # цикл до передостаннього елементу масиву
        for j in range(sizeLst):
            # цикл від початку до кінця списку
            if lst[j] > lst[j+1]:
                # якщо поточний елемент більше наступного
                lst[j], lst[j+1] = lst[j+1], lst[j] # обмін елементів
        sizeLst -= 1 # в кінці масиву залишаються найбільші елементи, яких не потрібно перевіряти

    return(lst)

def default_sort(lst):
    lst.sort() # відсортувати масив

    return lst

#default_sort(get_list_rand_int())
#default_sort(get_list_rand_float())

print("default_sort (float) --- %s seconds ---" % (time.time() - start_time)) # виводимо час виконання
