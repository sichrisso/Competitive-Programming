class Solution: 
    def select(self, arr, i):
        self.arr = arr
        self.i = i
    
    def selectionSort(self, arr,n):
       
        for i in range(n):
            for j in range(i+1, n):
                if arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
                else:
                    pass
                    
    
          
