import requests
import greeklish
from network import PrinterNetCalls
__author__ = 'gpamfilis'
import os
pnc = PrinterNetCalls()
import shutil

def create_deltio():
    ids = pnc.get_orders_to_print()
    if os.path.exists("/order_txt/"):
        print("not")
        os.mkdir("order_txt")
        shutil.rmtree('order_txt')
    else:
        print("yes")
        shutil.rmtree('order_txt')
        os.mkdir("order_txt")
        #


    for i in ids:
        print(i, len(ids))
        try:
            json = pnc.get_order(i)
        except Exception, e:
            print(e)
            continue

        f = open("./order_txt/id_" + str(i) + "_text.txt", "w")
        items = json["items"]
        table_name = items[0]["table_name"]
        f.write(table_name + "  " + items[0]["datetime"])
        f.write("\n")
        f.write(str(i))
        f.write("\n")
        for item in items:
            name = "x" + str(item["quantity"]) + " " + greeklish.main(item["name"].encode("utf-8"))[:28]
            f.write(name)
            f.write("\n")
            if len(item["contents"]) == 0:
                pass
            else:
                contents = item["contents"]
                for content in contents:
                    # find a way to range them on a line.
                    f.write("    " + greeklish.main(content))
                    f.write("\n")
        f.close()

if __name__ == '__main__':
    create_deltio()
