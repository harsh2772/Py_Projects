import time

time1=time.strftime("%H:%M:%S")
#print(time1)

check=int(time.strftime("%H"))

# check=int(time2)

if(check>=5 and check<12):
    print("Good Morning")

elif(check>=12 and check<17):
    print("Good Afternoon")

elif(check>=17 and check<21):
    print("Good Evening")

else:
    print("Good Night")

