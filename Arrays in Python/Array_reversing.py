import array as arr
arr=arr.array('i',[])
n=int(input())

for i in range(n):
    ele=int(input("Enter elements: "))
    arr.append(ele)
print("Reversed array.....")
arr.reverse()              
print(arr)
