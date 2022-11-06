def countingSort(arr):
    output = [0]*100
    for i in arr:
        output[i] += 1
    return output