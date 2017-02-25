__author__ = 'gpamfilis'

import thermal
import time
from network import PrinterNetCalls


if __name__ == '__main__':
    import sys, os
    pnc = PrinterNetCalls()
    if len(sys.argv) == 2:
        serial_port = sys.argv[1]
    else:
        serial_port = thermal.ThermalPrinter.SERIALPORT
    p = thermal.ThermalPrinter(serialport=serial_port)
    for fil in os.listdir("./order_txt"):
        print(fil)
        f = open("./order_txt/"+fil)
        lines = f.readlines()
        f.close()
        for line in lines:
            p.print_text(line[:])
        status = p.has_printed()
        # p.linefeed(3)
        pnc.post_that_order_was_printed(fil.split("_")[1])
        print(status)
        while status==False:
            print("Waiting...")
            time.sleep(1)
        time.sleep(4)