friends =["Ram", "Shyam", "Jon", "Tom"]
friends[0] = "Mary"
print(friends)

print(friends[0])
print(friends[2])
print(friends[-1])
print("learning print the rest of the list\n")

print(friends[1:3])
print(friends[1:])

print("lets discuss function of list\n")

lucky_no =[4, 8, 6, 2, 3]
print("append list")
friends.extend(lucky_no)
print(friends)
lucky_no.sort()
print(lucky_no)


friends.append("preplay")
print(friends)
print(friends.index("Tom"))
print(friends)
friends.insert(1, "Singh")
print(friends)
print(friends.count("Jon"))
friends.remove("Tom")
print(friends)


friends.pop()
print(friends)

friends.reverse()
print(friends)

friends2 =friends.copy()
print(friends2)
friends.clear()
print(friends) 






