#Input an array from user and delete a index.

import array as arr      

arr=arr.array('i',[])
n=int(input())

for i in range(n):
    ele=int(input("Enter elements: "))
    arr.append(ele)
for i in arr:   
    print(i,end=" ")
ind=int(input("Enter index u want to delete: "))
arr.pop(ind)                 
for i in arr:   
    print(i,end=" ")
