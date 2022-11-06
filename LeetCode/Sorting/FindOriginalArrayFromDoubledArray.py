def findOriginalArray(self, changed: List[int]) -> List[int]:
    n = len(changed)
    original = []
    double =  []
    changed.sort()
    count = changed.count(0)
    if n %2 != 0:
        return []
    else:
        for num in changed:
            if num == 0:
                if count == 0:
                    continue
                elif count %2 == 0: 
                    original.append(num)
                    count -= 2
                else:
                    break
            elif num>0:
                if len(double) == 0 or double[0] != num:
                    double.append(num*2)
                    original.append(num)
                elif double[0] == num:
                    double.pop(0)
                else:
                    break    
            else:
                break 
        if len(original) == n/2: 
            return original
        else:
            return []