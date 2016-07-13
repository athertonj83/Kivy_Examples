# advanced timer for my interval training app
import time
#import winsound

#60*int(warmUpMins)
#60*intervalMins
#Freq = 2500 # Set Frequency To 2500 Hertz
#Dur = 1000 # Set Duration To 1000 ms == 1 second


# warmup start of mins*60 for number of seconds
def warmupdown(timeLength, msg):
    print(msg)
    t0 = time.time()
    time.sleep(int(timeLength))
    #winsound.Beep(2500,500) - this is for windows
    #print("\a")
    #Beep

#intervals
def runIntervals(numIntervals,fastIntervalSecs,slowIntervalSecs):
    for i in range(int(numIntervals)):
        print("Fast interval - START")
        t0 = time.time()
        time.sleep(int(fastIntervalSecs))

        print("Slow interval - START")
        t0 = time.time()
        time.sleep(int(slowIntervalSecs))


#input from user
def userInput():
    x=input("Warm up seconds: ")
    y=input("Number of intervals: ")
    z=input("Length of fast interval: ")
    a=input("Length of slow interval: ")
    b=input("Length of cool down: ")

    print("\n\nWarmup:",x,"seconds\nNumber of intervals:",y,"\nFast Intervals:",z,"seconds\nSlow Intervals:",a,"seconds\nCool down:",b,"seconds")
    jen_continue=input("Y/N?")
    if jen_continue.upper()=="Y":
        warmupdown(x,"Warm up - START")
        runIntervals(y,z,a)
        warmupdown(b,"Cool down - START")
        print("End")

if __name__=="__main__":
    userInput()
