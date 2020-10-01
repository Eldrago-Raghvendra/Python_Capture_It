
#Enter a no. if print if negative, positive or zero 

num = int(input("Enter a number: ")) 
if num > 0:
  print("Positive")
elif num < 0:
  print("Negative")
else:
  print("equal to zero")'''
  
  
  
#Enter a letter print if vowel or not  
  
  
x = input("Input a letter of the alphabet: ")

if x in ('a', 'e', 'i', 'o', 'u'):
  print("%s is a vowel." % x)

else:
  print("%s is a consonant." % x)
