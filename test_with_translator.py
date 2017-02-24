import requests
import greeklish
from network import PrinterNetCalls
__author__ = 'gpamfilis'

pnc = PrinterNetCalls()

def create_deltio():
    ids = pnc.get_orders_to_print()
    for i in ids:
        print(i, len(ids))
        try:
            json = pnc.get_order(i)
        except Exception, e:
            print(e)
            continue

        f = open("./order_txt/id_" + str(i) + "text.txt", "w")
        items = json["items"]
        table_name = items[0]["table_name"]
        f.write(table_name + "  " + items[0]["datetime"])
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
