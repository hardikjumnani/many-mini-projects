from typing import List

powers: List[int] = list(map(int, input('Enter space seperated pokemon powers. ').split()))

min: int = 1e10
max: int = -1e10
for i in range(len(powers)):
    if powers[i] < min:
        min = powers[i]
    if powers[i] > max:
        max = powers[i]
    
    print(min, max)
