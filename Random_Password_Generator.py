import random
import string

# My Approach

list=[i for i in string.ascii_letters]
list.extend(i for i in string.digits)
list.extend(i for i in string.punctuation)

# for i in list:
#   print(i)

length=int(input("Enter the length of password: "))

l1=[]

for i in range(length):
  Pass=random.choice(list)
  l1.append(Pass)

print(l1)

random.shuffle(l1)
print(l1)

password="".join(l1)
print(password)


# Another Approach

charValues=string.ascii_letters+string.digits+string.punctuation

length=int(input("\nEnter the length of password: "))

password=""
for i in range(length):
  password+=random.choice(charValues)

print("Random Password: ",password)