#input an array and append elements at last of array.
import array as arr                             
arr=arr.array('i',[])
n=int(input())

for i in range(n):
    ele=int(input("Enter elements: "))
    arr.append(ele)
for i in arr:   
    print(i,end=" ")
