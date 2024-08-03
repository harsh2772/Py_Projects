# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode


val=input("Enter a Word: ")

le=int(len(val))

first=val[0]

star="min"
last="Leo"

if (le)>=3:
    a=val[1:]

    # print(a)

    value=a+first
    # print(value)

    code=star+value+last

elif le==2:
    code=star+val[1]+val[0]+last

else:
    code=star+val+last


print(code)

# Decode

dle=len(code)

if(dle>=9):

    de=code[3:-4]

    # print(de)

    fi=code[-4]

    decode=fi+de
    print(decode)

elif(dle==8):

    de=code[3:-4]
    # print(de)

    fi=code[-4]
    decode=fi+de
    print(decode)

else:
    decode=code[3:-3]
    print(decode)