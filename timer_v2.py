# advanced timer for my interval training app
import time
#import winsound

#60*int(warmUpMins)
#60*intervalMins
#Freq = 2500 # Set Frequency To 2500 Hertz
#Dur = 1000 # Set Duration To 1000 ms == 1 second
#winsound.Beep(2500,500) - this is for windows
#print("\a")


def timing(event,timeLength):
    print(event,"- START")
    time.sleep(int(timeLength))


#intervals
def runIntervals(numIntervals,fastI,slowI):
    for i in range(int(numIntervals)):
        timing("FAST Interval",fastI)
        timing("SLOW Interval",slowI)


#input from user
def userInput():
    x=input("Warm up seconds: ")
    y=input("Number of intervals: ")
    z=input("Length of fast interval: ")
    a=input("Length of slow interval: ")
    b=input("Length of cool down: ")

    print("\n\nWarmup:",x,"seconds\nNumber of intervals:",y,"\nFast Intervals:",z,"seconds\nSlow Intervals:",a,"seconds\nCool down:",b,"seconds")
    jen_continue=input("Y?N?")
    if jen_continue.upper()=="Y":
        timing("Warm up",x)
        runIntervals(y,z,a)
        timing("Cool down",b)
        print("End")

if __name__=="__main__":
    userInput()
