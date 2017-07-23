# coding: utf-8
import json

import requests
import sys
import thermal
import time

from get_configs import get_configuration
from network import PrinterNetCalls, InternetConnection
import sys
import os
import greeklish
__author__ = 'gpamfilis'
import os
import shutil
from utils import Create


def create_deltio(id_,pnc):
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


def print_order2(id_, order_list, p):
    pnc = PrinterNetCalls()
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
        p.print_text(line[:]+'\n', chars_per_line=23)
    # p.print_text("-------------END--NEW--ORDER---------------")

    p.linefeed(5)

    check_printer_status(p)

    pnc.post_that_order_was_printed(int(id_))
    print("Sending message to server for order id: ", id_)
    time.sleep(5)


def print_order3(id_, order_list, p):
    pnc = PrinterNetCalls()
    print("Attempting to print ord er_id: ", id_)
    lines = order_list
    print("initial paper check")
    printer_paper_status(p)
    p.print_text("---START--CHECKOUT-----", chars_per_line=27)
    print("printing order_id", id_)
    # p.print_text("---CHECKOUT----!!")
    p.print_text("\n")
    for line in lines:
        printer_paper_status(p)
        print("printing line", line[:])
        p.print_text(line[:]+'\n', chars_per_line=27)

    p.linefeed(5)

    check_printer_status(p)

    pnc.post_that_checkout_was_printed(int(checkout_id))
    print("Sending message to server for checkout id: ", id_)

    time.sleep(5)


if __name__ == '__main__':
    get_configuration()
    with open('values.json') as data_file:
        data = json.load(data_file)

    values = data
    pnc = PrinterNetCalls(**values)
    print(pnc.store_id)
    serial_port = thermal.ThermalPrinter.SERIALPORT
    p = thermal.ThermalPrinter(serialport=serial_port)
    create = Create()
    while True:
        pnc.check_internet()
        print('New Order Section')
        order_ids = pnc.get_orders_to_print()
        print(order_ids)
        for order_id in order_ids:
            order_list = pnc.get_order3(order_id)
            print('Order List: ', order_list)
            if order_list is None:
                pass
            else:
                print_order2(order_id, order_list, p=p)

        pnc.check_internet()
        print('Checkout Section')
        checkout_ids = pnc.get_checkouts_to_print()
        print(checkout_ids)
        for checkout_id in checkout_ids:
            checkout_list = pnc.get_checkout2(checkout_id)
            print('checkout list: ', checkout_list)
            if checkout_list is None:
                pass
            else:
                print_order3(checkout_id, checkout_list, p=p)

        time.sleep(5)
