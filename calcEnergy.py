#Assigning default values to variables
prev_dimmerValue=0.0
prev_ts=0.0
dimmerValue=0.0
power=0.0

#read file
f = open("PowerInputTmp.txt", "r")
lines = f.readlines()

#read each line
for x in lines:

    if x=="EOF\n":
        break
    #split each line into 3 fields: Timestamp, Signal, Delta
    l = x.split()

    ts=int(l[0])
    sg=l[1]
    if sg == "Delta":
        delta=l[2]

    #Calculate actual dimmer value from delta
    if sg=="TurnOff":
        dimmerValue=0.0
    else:
        dimmerValue+=float(delta)

    #Error handling: If a message is lost, this step will ensure dimmer value doesn't go beyond range
    if dimmerValue>1:
        dimmerValue=1.0
    elif dimmerValue<0:
        dimmerValue=0.0

    #Actual calulation
    td=ts-prev_ts
    power+=5*(float(td)/3600)*prev_dimmerValue
    #print("Power: "+str(power)+", Time Diff: "+str(td)+", Prev Ratio: "+str(prev_dimmerValue))

    #Getting previous record values
    prev_dimmerValue=dimmerValue
    prev_ts=ts
f.close()
print("Total Power Consumed: %f" % (power))

