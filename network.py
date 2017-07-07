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
        return status_code


class PrinterNetCalls(InternetConnection):
    def __init__(self):
        # self.base_url = "http://www.e-orders.org"
        self.base_url = "http://192.168.0.101:5000"
        self.store_id = 1

    def get_order(self, order_id):
        print("GET request for order_id = ", order_id)

        while True:
            # self.check_internet()

            try:
                data = requests.get(self.base_url + "/api/app/order?order_id=" + str(order_id))
                status_code  = data.status_code
                if status_code==200:
                    json = data.json()
                    break
                else:
                    break
            except Exception, e:
                print("This is the get_order exception: ", e, e.args, e.message)

        if status_code == 200:
            return json["items"]
        else:
            return None


    def get_order2(self, order_id):
        print("GET request for order_id = ", order_id)

        while True:
            # self.check_internet()

            try:
                data = requests.get(self.base_url + "/api/app/order?order_id=" + str(order_id))
                status_code  = data.status_code
                if status_code==200:
                    json = data.json()
                    break
                else:
                    break
            except Exception, e:
                print("This is the get_order exception: ", e, e.args, e.message)

        if status_code == 200:
            return json
        else:
            return None


    def get_order3(self, order_id):
        print("GET request for order_id = ", order_id)

        while True:
            # self.check_internet()

            try:
                data = requests.get(self.base_url + "/api/printer/pos-print?store_id=1&item_id="+ str(order_id) +"&type=order")
                status_code  = data.status_code
                if status_code==200:
                    json = data.json()
                    break
                else:
                    break
            except Exception, e:
                print("This is the get_order exception: ", e, e.args, e.message)

        if status_code == 200:
            return json
        else:
            return None



    def get_checkout(self, checkout_id):
        print("GET request for checkout_id = ", checkout_id)

        while True:
            # self.check_internet()

            try:
                data = requests.get(self.base_url + "/api/app/checkout?checkout_id=" + str(checkout_id))
                status_code  = data.status_code
                if status_code==200:
                    json = data.json()
                    break
                else:
                    break
            except Exception, e:
                print("This is the get_checkout exception: ", e, e.args, e.message)

        if status_code == 200:
            return json
        else:
            return None

    def get_checkout2(self, checkout_id):
        print("GET request for checkout_id = ", checkout_id)

        while True:
            # self.check_internet()

            try:
                data = requests.get(self.base_url + "/api/printer/pos-print?store_id=1&item_id="+ str(checkout_id)+"&type=checkout")
                status_code  = data.status_code
                if status_code==200:
                    json = data.json()
                    break
                else:
                    break
            except Exception, e:
                print("This is the get_checkout exception: ", e, e.args, e.message)

        if status_code == 200:
            print('ok', json)
            return json
        else:
            return None



    def get_orders_to_print(self):
        print("GET request for store_id = ", self.store_id)
        while True:
            # self.check_internet()
            try:
                data = requests.get(self.base_url + "/api/printer/orders-print?store_id=" + str(self.store_id))
                json = data.json()["ids"]
                break
            except Exception, e:
                print("The is the get_orders_to_print exception", e, e.args, e.message)
        return json



    def get_checkouts_to_print(self):
        print("GET request for store_id = ", self.store_id)
        while True:
            # self.check_internet()
            try:
                data = requests.get(self.base_url + "/api/printer/checkout-print?store_id=" + str(self.store_id))
                json = data.json()["ids"]
                break
            except Exception, e:
                print("The is the get_checkouts_to_print exception", e, e.args, e.message)
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
                print("this is the post_that_order_was_printed exception: ",e, e.args, e.message)
        return None

    def post_that_checkout_was_printed(self, order_id):
        print("POST request for order_id = ", order_id)

        status_code = 0
        while status_code != 200:
            # self.check_internet()

            try:
                data = requests.post(self.base_url + "/api/printer/checkout-print?checkout_id=" + str(order_id))
                # json = data.json()["ids"]
                status_code = data.status_code
                print("printed!! ", data.status_code)
                break
            except Exception, e:
                print("this is the post_that_order_was_printed exception: ", e, e.args, e.message)
        return None


if __name__ == '__main__':
    order = PrinterNetCalls().get_order(10)
    print(order)