def countSwaps(a):
    swap = 0
    for i in range(n):
        for j in range(i+1, n):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
                swap += 1
            else:
                pass
    print("Array is sorted in",swap, "swaps.")
    print("First Element:", a[0])
    print("Last Element:", a[-1])