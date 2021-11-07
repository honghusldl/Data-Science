# from math import ceil
import time

def find_divisible(x,y):
    start = time.time()

    if not y > x:
        return []
    # else:
    #     div = []
    #     for a in range(1, int((y)/x) + 1):
    #         b = x * a
    #         div.append(b)

    #     return div
    div = []
    num = 1
    while num < int(y/x) + 1:
        div.append(x*num)
        num += 1
    
    time_elasped = time.time() - start
    print(time_elasped)
    return div
    
    
print(find_divisible(5, 50))
# print( find_divisible(7, 62) )
#print(find_divisible(3, 11) )
#print(find_divisible(13, 102) )
# print(find_divisible(11, 78) )
# print(find_divisible(65,5))




