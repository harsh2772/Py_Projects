import pywhatkit
import time

hr=int(time.strftime("%H"))
print(hr)
min=int(time.strftime("%M"))
print(min)

# lst=[]
#
# while True:
#
#     num=(input("Enter the mobile number:"))
#     phone="+91"+num
#
#
#     if(num=="quit"):
#         break
#
#     lst.append(phone)
#
# print(lst)
#
# for i in lst:
#     pywhatkit.sendwhatmsg("+9194748484","Hello Harsh",hr,min+1)

pywhatkit.sendwhatmsg("+91937484848","Hello Harsh",hr,min+1)