import time
from playsound import playsound


def p():
    playsound("mixkit-digital-clock-digital-alarm-buzzer-992.wav")
def timer(h,m):
    for k in range(h,-1,-1):
        k=str(k).zfill(2)
    for i in range(m,-1,-1):
        i=str(i).zfill(2)
    for j in range(6,-1,-1):
        j=str(j).zfill(2)
        for n in range(100,0,-1):
            n=str(n).zfill(2)
            time.sleep(0.01)
            print(end="\t\t")
            print("{}h:{}m:{}s:{}ms".format(k,i,j,n),end="\r")
    print(end="\t\t")        
    print(end='00h:00m:00s:00ms')
    print(" ")

hh=int(input("enter the hour :"))
mm=int(input("enter the minute :"))
timer(hh,mm)
while True:
    print('Time up .......')
    p()
    a=input(' take break  for 5 sec : y/n : ')
    if a=="y":
        time.sleep(5)
    else:
        print('OK Bye...............')
        break