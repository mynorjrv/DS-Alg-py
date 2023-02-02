import time
import io

# time.perf_counter()
# time.sleep(1)
# time.perf_counter()

def preamble(file: io.TextIOWrapper) -> None:
    file.write('<?xml version="1.0" encoding="UTF-8" '
        'standalone="no" ?>\n')

    file.write('<Plot title="Average List Element '
        'Access Time">\n')
    
    pass


def main():

    xmin = 1000
    xmax = 20000

    xList = list()
    yList = list()

    with open("ListAccessTiming.xml", 'w') as MyFile:

        preamble(MyFile)

        for x in range(xmin, xmax+1, 1000):
            xList.append(x)

            



        


    pass

if __name__ == '__main__':
    main()