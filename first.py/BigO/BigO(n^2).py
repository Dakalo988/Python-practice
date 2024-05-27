#quadratic complexity

from functools import total_ordering


num_list = [1,2,3,4,5,6,7]
num_list2 = [5,6,7,8,9]

def rondomFuction(num_list):
    total = 0

for num1 in num_list2: # type: ignore
    for num2 in num_list:
        print(num1,num2)
        total += 1 # type: ignore
    
    return total # type: ignore
print(rondomFuction(num_list))
