# Enter an element from user and remove it from given array.

import array as arr
a=arr.array('i',[0,9,8,5,3,2,3,4,2])
print(a)                               #6
ele=int(input("enter value to be removed:"))
if ele in a:
    a.remove(ele)
print(a)
