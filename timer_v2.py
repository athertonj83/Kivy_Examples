# advanced timer for my interval training app
import time
#import winsound

#60*int(warmUpMins)
#60*intervalMins
#Freq = 2500 # Set Frequency To 2500 Hertz
#Dur = 1000 # Set Duration To 1000 ms == 1 second


# warmup start of mins*60 for number of seconds
def warmup(warmUpSecs):
    t0 = time.time()
    time.sleep(int(warmUpSecs))
    print("End of warm up!")
    print(time.time() - t0, "time elapsed")
    #winsound.Beep(2500,500) - this is for windows
    #print(chr(7))

#intervals
def intervalTime(numIntervals,intervalSecs):
    for i in range(int(numIntervals)):
        t0 = time.time()
        time.sleep(int(intervalSecs))
        print("End of interval",i+1)
        print(time.time() - t0, "time elapsed")




#input from user
def userInput():
    x=input("Enter number of warm up seconds: ")
    y=input("Enter number of intervals: ")
    z=input("Enter length of each interval: ")

    print("You have chosen a warmup of",x,"seconds, and",y,"intervals, of",z, "seconds each.")
    jen_continue=input("Y/N?")
    if jen_continue.upper()=="Y":
        warmup(x)
        intervalTime(y,z)

if __name__=="__main__":
    userInput()
