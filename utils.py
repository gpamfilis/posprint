# coding=utf-8

from string import maketrans, translate


def greeklishgrtoen(strings):
    try:
        text = strings
        text = text.decode('utf-8')
        text = text.encode('iso-8859-7', 'replace')
        from_chars = u'áâãäåæçèéêëìíîïðñóòôõö÷øùÜÝÞßúÀüýûàþÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÓÔÕÖ×ØÙ¶¸¹ºÚ¼¾Û¿'.encode('latin1')
        to_chars = u'abgdezh8iklmn3oprsstufxywaehiiiouuuwABGDEZH8IKLMNJOPRSTYFXCWAEHIIOUUW'.encode('latin1')
        trantab = maketrans(from_chars, to_chars)
        # trantab = dict((ord(a), b) for a, b in zip(from_chars, to_chars))
        text = translate(text, trantab)
        return text.upper()
    except Exception, e:
        return e


class Create(object):
    def __init__(self):
        pass


    @staticmethod
    def order2(json_object):
        try:
            json = json_object
        except Exception, e:
            print("This is the create_deltio exception", e)

        if json is None:
            return None
        else:
            order = []
            items = json
            # print(items)
            table_name = items['items'][0]["table_name"]
            # print(table_name)
            order_id = items["order_id"]
            # print(table_name, order_id)
            order.append(table_name + "  " + items["datetime"])
            order.append(str(order_id))
            # # print(items)
            for item in items["items"]:
                name = "x" + str(item["quantity"]) + "  " + greeklishgrtoen(item["name"].encode("utf-8"))
                # name = "x" + str(item["quantity"]) + "  " + greeklishgrtoen(item["category"].encode("utf-8"))[:4] + " : " + greeklishgrtoen(item["name"].encode("utf-8"))
                order.append(name)
                if len(item["contents"]) == 0:
                    pass
                else:
                    contents = item["contents"]
                    for content in contents:
                        if (content["changed"] == 1) and (content["default"] == 1):
                            name = content["content_name"].encode("utf-8")
                            greeklish_content = greeklishgrtoen(name)
                            cont = "    NOT  " + greeklish_content
                            order.append(cont)
                        elif (content["changed"] == 1) and (content["default"] == 0):
                            name = content["content_name"].encode("utf-8")
                            greeklish_content = greeklishgrtoen(name)
                            cont = "    YES  " + greeklish_content
                            order.append(cont)
                        elif content['changed'] == 0:
                            pass
                        else:
                            pass
            return order



    @staticmethod
    def order(json_object):
        try:
            json = json_object
        except Exception, e:
            print("This is the create_deltio exception", e)

        if json is None:
            return None
        else:
            order = []
            items = json["items"]
            # print(items)
            table_name = items["items"][0]["table_name"]
            order_id = items["order_id"]
            # print(table_name, order_id)
            order.append(table_name + "  " + items["datetime"])
            order.append(str(order_id))
            # print(items)
            for item in items["items"]:
                name = "x" + str(item["quantity"]) + "  " + greeklishgrtoen(item["name"].encode("utf-8"))
                # name = "x" + str(item["quantity"]) + "  " + greeklishgrtoen(item["category"].encode("utf-8"))[:4] + " : " + greeklishgrtoen(item["name"].encode("utf-8"))
                order.append(name)
                if len(item["contents"]) == 0:
                    pass
                else:
                    contents = item["contents"]
                    for content in contents:
                        if (content["changed"] == 1) and (content["default"] == 1):
                            name = content["content_name"].encode("utf-8")
                            greeklish_content = greeklishgrtoen(name)
                            cont = "    NOT  " + greeklish_content
                            order.append(cont)
                        elif (content["changed"] == 1) and (content["default"] == 0):
                            name = content["content_name"].encode("utf-8")
                            greeklish_content = greeklishgrtoen(name)
                            cont = "    YES  " + greeklish_content
                            order.append(cont)
                        elif content['changed'] == 0:
                            pass
                        else:
                            pass
            return order

    @staticmethod
    def checkout(json_object):
        # print("object")
        # print(json_object)

        checkout_list = []
        order_items = json_object["items"]
        # print("order_items")
        # print(order_items)
        grand_total = 0

        # print("other items")
        # print(order_items["items"])
        # print("the checkout items")
        for order in order_items:
            # print(order)
            for item in order["items"]:
                # print("the item", item)
                name = "x" + str(item["quantity"]) + "  " + greeklishgrtoen(item["category"].encode("utf-8"))[:4] + " : " + greeklishgrtoen(item["name"].encode("utf-8"))
                checkout_list.append(name)
            total = "subtotal  " + str(order["total"])
            grand_total += order["total"]
            checkout_list.append(total)
        checkout_list.append("Total:    "+str(round(grand_total, 2)))
        return checkout_list