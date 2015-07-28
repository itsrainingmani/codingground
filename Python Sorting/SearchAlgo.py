def binary_search(arr, val):
    if len(arr) == 0:
        return False
    else:
        mid = len(arr)//2
        if(arr[mid] == val):
            return True
        else:
            if(val < arr[mid]):
                return binary_search(arr[:mid], val)
            else:
                return binary_search(arr[mid + 1:], val)
    