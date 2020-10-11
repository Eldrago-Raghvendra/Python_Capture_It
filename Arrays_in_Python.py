import array as arr                             #1
arr=arr.array('i',[])
n=int(input())

for i in range(n):
    ele=int(input("Enter elements: "))
    arr.append(ele)
for i in arr:   
    print(i,end=" ")
