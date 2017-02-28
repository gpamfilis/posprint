import requests

__author__ = 'gpamfilis'


class PrinterNetCalls:
    def __init__(self):
        self.base_url = "http://www.e-orders.org"
        self.store_id = 1

    def get_order(self, order_id):
        while True:
            try:
                data = requests.get(self.base_url + "/api/app/order?order_id=" + str(order_id))
                json = data.json()
                break
            except Exception, e:
                print(e, e.args, e.message)
        return json

    def get_orders_to_print(self):
        while True:
            try:
                data = requests.get(self.base_url + "/api/printer/orders-print?store_id=" + str(self.store_id))
                json = data.json()["ids"]
                break
            except Exception, e:
                print(e, e.args, e.message)
        return json


    def post_that_order_was_printed(self, order_id):
        while True:
            try:
                data = requests.post(self.base_url + "/api/printer/orders-print?order_id=" + str(order_id))
                json = data.json()["ids"]
                print("printed!! ", order_id)
                break
            except Exception, e:
                print(e, e.args, e.message)
        return json


if __name__ == '__main__':
    pass
