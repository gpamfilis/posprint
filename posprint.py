__author__ = 'gpamfilis'

import thermal
import time

if __name__ == '__main__':
    import sys, os
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
        print(status)
        time.sleep(2)