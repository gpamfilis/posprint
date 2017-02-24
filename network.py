__author__ = 'gpamfilis'

import requests


class PrinterNetCalls:
    def __init__(self):
        self.base_url = "http://www.e-orders.org"
        self.store_id = 1

    def get_order(self, order_id):
        data = requests.get(self.base_url + "/api/app/order?order_id=" + str(order_id))
        json = data.json()
        return json

    def get_orders_to_print(self):
        try:
            data = requests.get(self.base_url + "/api/printer/orders-print?store_id=" + str(self.store_id))
            json = data.json()["ids"]
        except Exception, e:
            print(e, e.args, e.message)
            json=None
        return json


if __name__ == '__main__':
    pass
