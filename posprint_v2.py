import requests
import sys
import thermal
import time
from network import PrinterNetCalls
import sys
import os
import greeklish
__author__ = 'gpamfilis'
import os
import shutil


pnc = PrinterNetCalls()

ids = pnc.get_orders_to_print()


def create_deltio(id_):
    try:
        json = pnc.get_order(id_)
    except Exception, e:
        print(e)
        order = []

        items = json["items"]
        table_name = items[0]["table_name"]

        order.append(table_name + "  " + items[0]["datetime"])
        order.append(str(id_))
        for item in items:
            name = "x" + str(item["quantity"]) + " " + greeklish.main(item["name"].encode("utf-8"))[:28]
            order.append(name)
            if len(item["contents"]) == 0:
                pass
            else:
                contents = item["contents"]
                for content in contents:
                    # find a way to range them on a line.
                    cont = "    " + greeklish.main(content)
                    order.append(cont)
    return order


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


def print_order(id_, order):
    pnc = PrinterNetCalls()
    if len(sys.argv) == 2:
        serial_port = sys.argv[1]
    else:
        serial_port = thermal.ThermalPrinter.SERIALPORT
    p = thermal.ThermalPrinter(serialport=serial_port)

    print("Attempting to print ord er_id: ", id_)
    lines = order
    print("initial paper check")
    printer_paper_status(p)
    print("---NEW--ORDER----!!")
    print("printing order_id", id_)
    p.print_text("---NEW--ORDER----!!")
    p.print_text("\n")
    for line in lines:
        printer_paper_status(p)
        print("printing line", line[:])
        p.print_text(line[:]+'\n')

    p.linefeed(3)

    check_printer_status(p)

    pnc.post_that_order_was_printed(int(id_))
    print("Sending message to server for order id: ", id_)
    time.sleep(5)


if __name__ == '__main__':
    pnc = PrinterNetCalls()
    ids = pnc.get_orders_to_print()
    for id_ in ids:
        order = create_deltio(id_)
        print_order(id_, order)
