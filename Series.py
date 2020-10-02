a=int(input("Enter the terms"))
f=int(input("Enter the first no:"))                                         #first element of series
s=int(input("Enter the second:"))                                         #second element of series
if a<=0:
    print("The requested series is",f)

else:
    print(f,s,end=" ")
    for x in range(2,a):
        next=f+s                           
        print(next,end=" ")
        f=s
        s=next
