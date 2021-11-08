import sys
import time
from extender import *

startTime = time.time()  # время начала замера

if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("Incorrect command line! Waited command -f infile outfile01 outfile02 \n"
              "or \n"
              "command -n number outfile01 outfile02")
        exit()
    elif sys.argv[1] == "-f":
        inputFileName = sys.argv[2]
        outputFileName_01 = sys.argv[3]
        outputFileName_02 = sys.argv[4]
        ifile = open(inputFileName)
        str = ifile.read()
        ifile.close()

        strArray = str.replace("\n", " ").split(" ")

        print('==> Start')

        container = Container()
        plantNum = read_str_array(container, strArray)
        container.print()

        ofile = open(outputFileName_01, 'w')
        ofile_02 = open(outputFileName_02, 'w')
        container.write(ofile)
        container.shell_print()
        container.shell_write(ofile_02)
        ofile.close()
        ofile_02.close()

        print('==> Finish')

    elif sys.argv[1] == "-n":
        if len(sys.argv) != 5:
            print("Incorrect command line! Waited command -f infile outfile01 outfile02 \n"
                  "or \n"
                  "command -n number outfile01 outfile02")
            exit()
        else:
            count = sys.argv[2]
            outputFileName_01 = sys.argv[3]
            outputFileName_02 = sys.argv[4]
            ofile = open(outputFileName_01, 'w')
            ofile_02 = open(outputFileName_02, 'w')
            container = Container()
            container.random_print(count)
            container.random_write(ofile)
            print("\n")
            container.shell_print()
            container.shell_random_write(ofile_02)
            print('==> Finish')
    else:
        print("Incorrect command line! Waited command -f infile outfile01 outfile02 \n"
              "or \n"
              "command -n number outfile01 outfile02")
        exit()

    # Чтение исходного файла, содержащего данные, разделенные пробелами и переводами строки

endTime = time.time()  # время конца замера
totalTime = endTime - startTime  # вычисляем затраченное время
print("Время, затраченное на выполнение данного кода = ", totalTime)
