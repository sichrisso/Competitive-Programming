def totalFruit(self, fruits: List[int]) -> int:
    f1 = f2 = output = 0
    fruit1 = fruit2 = fruits[f1] = fruits[f2]
    while f2 < len(fruits): 
        if fruits[f2] != fruit1 and fruits[f2] != fruit2:
            if fruit1 == fruit2:
                fruit2 = fruits[f2]
            else:
                f1 = f2 - 1
                fruit1 = fruits[f2 - 1]
                while True:
                    f1 -= 1
                    if fruits[f1] != fruit1:
                        f1 += 1
                        break
                    else:
                        continue

                fruit2 = fruits[f2]
        output = max(output, (f2 - f1) + 1) 
        f2 += 1
    return output