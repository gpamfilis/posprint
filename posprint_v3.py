# coding: utf-8
import requests
import sys
import thermal
import time
from network import PrinterNetCalls, InternetConnection
import sys
import os
import greeklish
__author__ = 'gpamfilis'
import os
import shutil
from utils import Create


pnc = PrinterNetCalls()

ids = pnc.get_orders_to_print()


def create_deltio(id_):
    try:
        # int.check_internet()
        json = pnc.get_order(id_)
    except Exception, e:
        print("This is the create_deltio exception", e)

    if json is None:
        return None
    else:    
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
                    name = content["content_name"].encode("utf-8")
                    greeklish_content = greeklish.main(name)
                    cont = "    " + greeklish_content
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
        # print("not done printing")
        printer_status = [p.has_printed() for i in range(10)][-1]
        time.sleep(2)
        if printer_status:
            # print("printer free")
            time.sleep(5)
            break



def print_order2(id_, order_list):
    pnc = PrinterNetCalls()
    if len(sys.argv) == 2:
        serial_port = sys.argv[1]
    else:
        serial_port = thermal.ThermalPrinter.SERIALPORT
    p = thermal.ThermalPrinter(serialport=serial_port)

    # print("Attempting to print ord er_id: ", id_)
    lines = order_list
    print("initial paper check")
    printer_paper_status(p)
    print("---NEW--ORDER----!!")
    print("printing order_id", id_)
    p.print_text("-------START--NEW--ORDER-------")
    p.print_text("\n")
    for line in lines:
        printer_paper_status(p)
        print("printing line", line[:])
        p.print_text(line[:]+'\n')
    # p.print_text("-------------END--NEW--ORDER---------------")

    p.linefeed(5)

    check_printer_status(p)

    pnc.post_that_order_was_printed(int(id_))
    print("Sending message to server for order id: ", id_)
    time.sleep(5)

def print_order3(id_, order_list):
    pnc = PrinterNetCalls()
    if len(sys.argv) == 2:
        serial_port = sys.argv[1]
    else:
        serial_port = thermal.ThermalPrinter.SERIALPORT
    p = thermal.ThermalPrinter(serialport=serial_port)

    print("Attempting to print ord er_id: ", id_)
    lines = order_list
    print("initial paper check")
    printer_paper_status(p)
    p.print_text("------START--CHECKOUT---------")
    print("printing order_id", id_)
    p.print_text("---CHECKOUT----!!")
    p.print_text("\n")
    for line in lines:
        printer_paper_status(p)
        print("printing line", line[:])
        p.print_text(line[:]+'\n')
    # p.print_text("-----------END--CHECKOUT--------")

    p.linefeed(5)

    check_printer_status(p)

    pnc.post_that_checkout_was_printed(int(checkout_id))
    print("Sending message to server for checkout id: ", id_)
    time.sleep(5)


if __name__ == '__main__':
    # int = InternetConnection()
    pnc = PrinterNetCalls()
    create = Create()
    while True:
        pnc.check_internet()
        order_ids = pnc.get_orders_to_print()
        for order_id in order_ids:
            order = pnc.get_order2(order_id)
            print(order)
            order_list = create.order(order)
            if order_list is None:
                pass
            else:
                print_order2(order_id, order_list)

        checkout_ids = pnc.get_checkouts_to_print()
        print(checkout_ids)
        for checkout_id in checkout_ids:
            checkout = pnc.get_checkout(checkout_id)
            print(checkout)
            checkout_list = create.checkout(checkout)
            if checkout_list is None:
                pass
            else:
                print_order3(checkout_id, checkout_list)
        # time.sleep(5)
