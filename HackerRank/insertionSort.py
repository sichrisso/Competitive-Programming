def insertionSort1(n, arr):
    last = arr[-1]
    while (n-2) >= 0:
        if last < arr[n-2]:
            arr[n-1] = arr[n-2]
            n -= 1  
            print (*arr)  
        else:
            arr[n-1] = last
            print (*arr)  
            break
    if(n-2 < 0 and last not in arr):
        arr[0] = last
        print (*arr) 