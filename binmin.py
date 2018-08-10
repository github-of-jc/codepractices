# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 15:10:32 2018

@author: jc57220
"""

# Returns index of x in arr if present, else -1
def binMin (arr, l, r):
    print('binary search')
    print(arr)
    print('left')
    print(l)
    print('right')
    print(r)
    # Check base case
    if l<=r:
        mid = l + (r-l)//2
        print('middle is at ' + str(mid) + ' value ' + str(arr[mid]))
        
        if arr[mid] < arr[r]: #turn is on the left, binMin left side
            return binMin(arr, l, mid)
        else:
            return binMin(arr, mid + 1, r)
    else:
        print('l > r')
        print('r: ' + str(r))
        return r
        
# Test array
arr = [ 40, 50, 60, 2, 3, 4, 10, 20 ]

 
# Function call
result = binMin(arr, 0, len(arr)-1)
 
print('smallest is at ' + str(result))
