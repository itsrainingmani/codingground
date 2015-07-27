# Hello World program in Python
import random
import time

def bubblesort(n,m):
    arr = [0 for x in range(n)]
    for num in range(0,n):
        arr[num] = random.randrange(0,m)
    #print (arr)
    start_time = time.time()
    for i in range(0,len(arr)):
        for j in range(0,len(arr)-1):
            if (arr[j] > arr[j+1]):
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    
    print("BS--- %s seconds ---" % (time.time() - start_time))
    #print (arr)

def selection_sort(n,m):
    arr = [0 for x in range(n)]
    for num in range(0,n):
        arr[num] = random.randrange(0,m)
    #print (arr)
    start_time = time.time()
    for i in range(0,len(arr)):
        index_of_min = i
        for j in range(i, len(arr)):
            if(arr[index_of_min] > arr[j]):
                index_of_min = j
        temp = arr[i]
        arr[i] = arr[index_of_min]
        arr[index_of_min] = temp
    print("SS--- %s seconds ---" % (time.time() - start_time))
    #print (arr)

def insertion_sort(n,m):
    arr = [0 for x in range(n)]
    for num in range(0,n):
        arr[num] = random.randrange(0,m)
    #print (arr)
    start_time = time.time()
    for i in range(1,len(arr)):
        x = arr[i]
        j = i
        while ( j > 0 and arr[j-1] > x):
            arr[j] = arr[j-1]
            j = j-1
        arr[j] = x
    #print(arr)
    print("IS--- %s seconds ---" % (time.time() - start_time))
    #print (arr)
    
#bubblesort(10000,10000)
selection_sort(10000,10000)
insertion_sort(10000,10000)