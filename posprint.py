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

        print("initial paper check")

        paper_status = p.has_paper()

        while paper_status is False:
            paper_status = p.has_paper()
            print("no paper in printer!")
            time.sleep(2)
            if paper_status:
                print("paper in printer")
                time.sleep(5)
                break

        print("going on to print paper")
        print("printing order_id", fil.split("_")[1])

        print("---NEW--ORDER----!!")
        p.print_text("---NEW--ORDER----!!")
        p.print_text("\n")
        for line in lines:
            paper_status = p.has_paper()

            if paper_status is False:
                while paper_status is False:
                    paper_status = p.has_paper()
                    print("no paper in printer!")
                    time.sleep(2)

                    if paper_status:
                        print("paper in printer")
                        time.sleep(5)

                        p.print_text("--REPRINTING--")
                        for line in lines:
                            print("reprinting", line[:])
                            # p.print_text(line[:])
                        p.linefeed(3)
                        # p.print_text("---IGNORE---") # todo correct this fucking shit. after ignore it always print s some items
                        print("--ignore--")
                        break
                    break

            else:
                print("actual printing: ", line[:])
                # p.print_text(line[:])

        p.linefeed(3)
        printer_status = p.has_printed()
        if printer_status is False:
            while printer_status is False:
                print("not done printing")
                printer_status = p.has_printed()
                if printer_status:
                    print("printing completed")
                    print("sending messaged to server that id {0} is printed!".format(fil.split("_")[1]))
                    time.sleep(5)

        else:
            print("printing completed")
            print("sending messaged to server that id {0} is printed!".format(fil.split("_")[1]))
            time.sleep(5)
