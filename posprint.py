import thermal
import time
from network import PrinterNetCalls
import sys
import os

__author__ = 'gpamfilis'



def read_items(fil):
    print(fil)
    f = open("./order_txt/" + fil)
    lines = f.readlines()
    f.close()
    return lines


def printer_paper_status(p):
    paper_status = [p.has_paper() for i in range(10)][-1]
    while paper_status is False:
        paper_status = p.has_paper()
        print("no paper in printer!")
        time.sleep(2)
        if paper_status:
            print("paper in printer")
            time.sleep(5)
            break


def check_printer_status(p):
    printer_status = p.has_printed()
    while printer_status is False:
        print("not done printing")
        printer_status = [p.has_printed() for i in range(10)][-1]
        time.sleep(2)
        if printer_status:
            print("printer free")
            time.sleep(5)
            break

if __name__ == '__main__':
    pnc = PrinterNetCalls()
    if len(sys.argv) == 2:
        serial_port = sys.argv[1]
    else:
        serial_port = thermal.ThermalPrinter.SERIALPORT
    p = thermal.ThermalPrinter(serialport=serial_port)

    for fil in os.listdir("./order_txt"):
        print("Attempting to print ord er_id: ", fil.split("_")[1])
        lines = read_items(fil)
        print("initial paper check")
        printer_paper_status(p)
        print("---NEW--ORDER----!!")
        print("printing order_id", fil.split("_")[1])
        p.print_text("---NEW--ORDER----!!")
        p.print_text("\n")
        for line in lines:
            printer_paper_status(p)
            print("printing line", line[:])
            p.print_text(line[:])

        p.linefeed(3)

        check_printer_status(p)

        print("Sending message to server for order id: ", fil.split("_")[1])
