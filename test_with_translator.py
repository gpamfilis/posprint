import requests
import greeklish

__author__ = 'gpamfilis'


def get_order(order_id):
    data = requests.get("http://www.e-orders.org/api/app/order?order_id=" + str(order_id))
    json = data.json()
    return json


def get_orders_to_print():
    data = requests.get("http://www.e-orders.org/api/printer/orders-print?store_id=" + str(1))
    json = data.json()["ids"]
    return json


def create_deltio():
    ids = get_orders_to_print()
    for i in ids:
        print(i, len(ids))
        try:
            json = get_order(i)
        except Exception, e:
            print(e+"dsfsdfsadfsa")

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
