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
            paper_status = p.has_paper()
            print("the paper status is:", paper_status)

            while paper_status == False:
                print("Waiting for paper...")
                paper_status = p.has_paper()
                time.sleep(3)
                if paper_status:
                    time.sleep(5)
                    p.linefeed(4)
                    print("reprinting...")
                    p.print_text("REPRINTING")
                    for line in lines:
                        p.print_text(line[:])
                    p.linefeed(5)
                break

        p.linefeed(5)
        printer_status = p.has_printed()
        while printer_status == False:
            printer_status = p.has_printed()
            print("Waiting for the printer to complete...")
            time.sleep(3)
        pnc.post_that_order_was_printed(fil.split("_")[1])
        time.sleep(4)
