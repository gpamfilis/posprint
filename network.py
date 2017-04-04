import requests

__author__ = 'gpamfilis'


class InternetConnection:
    def __init__(self):
        pass

    def check_internet(self):
        status_code = 0
        print("Checking for an internet connection")
        while status_code != 200:
            try:
                req = requests.get("https://www.google.com")
                status_code = req.status_code
                if status_code==200:
                    break
            except Exception, e:
                print(e)
        return None


class PrinterNetCalls(InternetConnection):
    def __init__(self):
        self.base_url = "http://www.e-orders.org"
        self.store_id = 1

    def get_order(self, order_id):
        print("GET request for order_id = ", order_id)

        while True:
            # self.check_internet()

            try:
                data = requests.get(self.base_url + "/api/app/order?order_id=" + str(order_id))
                json = data.json()
                break
            except Exception, e:
                print(e, e.args, e.message)
        return json["items"]

    def get_orders_to_print(self):
        print("GET request for store_id = ", self.store_id)
        while True:
            # self.check_internet()
            try:
                data = requests.get(self.base_url + "/api/printer/orders-print?store_id=" + str(self.store_id))
                json = data.json()["ids"]
                break
            except Exception, e:
                print(e, e.args, e.message)
        return json


    def post_that_order_was_printed(self, order_id):
        print("POST request for order_id = ", order_id)

        status_code = 0
        while status_code != 200:
            # self.check_internet()

            try:
                data = requests.post(self.base_url + "/api/printer/orders-print?order_id=" + str(order_id))
                # json = data.json()["ids"]
                status_code = data.status_code
                print("printed!! ", data.status_code)
                break
            except Exception, e:
                print(e, e.args, e.message)
        return None


if __name__ == '__main__':
    order = PrinterNetCalls().get_order(10)
    print(order)