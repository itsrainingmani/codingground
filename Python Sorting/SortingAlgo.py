import random
import time

def bubblesort(arr):
    #print (arr)
    start_time = time.time()
    for i in range(0,len(arr)):
        for j in range(0,len(arr)-1):
            if (arr[j] > arr[j+1]):
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    
    print("BS--- %s seconds ---" % (time.time() - start_time))
    return arr
    #print (arr)

def selection_sort(arr):
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
    return arr
    #print (arr)

def insertion_sort(arr):
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
    return arr
    #print (arr)
    
if __name__ == "__main"":
    main()
