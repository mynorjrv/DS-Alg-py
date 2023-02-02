import datetime
import random
import time

def main():
    #Write an XML file with the results
    file = open("ListAccessTiming.xml","w")

    file.write('<?xml version="1.0" encoding="UTF-8" standalone="no" ?>\n')
    
    file.write('<Plot title="Average List Element Access Time">\n')
    
    #Test lists of size 1000 to 200000.
    xmin = 1000
    xmax = 2000

    # xList is the length of the tested lists and yList
    # is the test time for 1000 accesses for each length
    xList = []
    yList = []

    for x in range(xmin, xmax+1, 1000):

        xList.append(x)

        prod = 0


         # Creates a list of size x with all 0's
        lst = [0 for i in range(x)]

        # let any garbage collection/memory allocation complete 
        # or at least settle down
        time.sleep(1)

        # Time before the 1000 test retrievals
        starttime = time.perf_counter()

        for v in range(1000):
            # Find a random location within the list
            # and retrieve a value. Do a dummy operation
            # with that value to ensure it is really retrieved.
            index = random.randint(0,x-1)
            val = lst[index]
            prod = prod * val
        # Time after the 1000 test retrievals
        endtime = time.perf_counter()

        # The difference in time between start and end.
        deltaT = endtime - starttime

        # Divide by 1000 for the average access time
        # But also multiply by 1000000 for microseconds.
        accessTime = deltaT * 1000

        yList.append(accessTime)

    file.write(' <Axes>\n')
    file.write(f' <XAxis min="{xmin}" max="{xmax}">List Size</XAxis>\n')
    file.write(f' <YAxis min="{yList}" max="{60}">Microseconds</YAxis>\n')
    file.write(' </Axes>\n')

    file.write(' <Sequence title="Average Access Time vs List Size" color="red">\n')

    for i in range(len(xList)):
        file.write(f' <DataPoint x="{xList[i]}" y="{yList[i]}"/>\n')

    file.write(' </Sequence>\n')

    # This part of the program tests access at 100 random locations within a list
    # of 200,000 elements to see that all the locations can be accessed in
    # about the same amount of time.

    # In fact this is stupid xd random number out of range

    xList = lst
    yList = [0 for i in range(200000)]

    time.sleep(2)

    for i in range(100):
        
        starttime = time.perf_counter()
        index = random.randint(0,200000-1)
        xList[index] = xList[index] + 1
        endtime = time.perf_counter()

        deltaT = endtime - starttime
        yList[index] = yList[index] + deltaT * 1000000

    file.write(' <Sequence title="Access Time Distribution" color="blue">\n')

    for i in range(len(xList)):
        if xList[i] > 0:
            file.write(f' <DataPoint x="{i}" y="{yList[i]/xList[i]}"/>\n')

    file.write(' </Sequence>\n')
    file.write('</Plot>\n')
    file.close()

if __name__ == '__main__':
    main()