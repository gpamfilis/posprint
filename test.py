# coding: utf-8

__author__ = 'gpamfilis'

from PIL import Image, ImageDraw, ImageFont
import requests


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
    # for i in [22]:
        json = get_order(i)

        items = json["items"]

        n_orders = len(items)
        print(n_orders)
        width = 350
        height = 50 * (n_orders+3)
        h = 50 * n_orders*3
        head = 20
        left = 40
        back_ground_color = (255, 255, 255)
        font_size = 30
        font_color = (0, 0, 0)
        im = Image.new("RGB", (width, height), back_ground_color)
        unicode_font = ImageFont.truetype('./fonts/arial.ttf', font_size)
        date_font = ImageFont.truetype('./fonts/arial.ttf', font_size)

        items = json["items"]
        draw = ImageDraw.Draw(im)

        draw.text((20+left, head), items[0]["table_name"], font=unicode_font, fill=font_color)
        # draw.text((60+left, head), items[0]["datetime"], font=date_font, fill=font_color)
        draw.text((250+left, head), str(i), font=date_font, fill=font_color)
        gap = h/(n_orders*3)
        # draw.text((10, 0+gap), " ", font=unicode_font, fill=font_color)

        d_line = font_size  # +(gap*1)
        for item in items:
            name = item["name"]
            print(name)
            draw.text((20+left, 2*head + d_line), "x" + str(item["quantity"]) + " " + name[:10], font=unicode_font, fill=font_color)
            d_line += gap
        im.save("./orders_pic/id_"+str(i)+"_text.png")


if __name__ == '__main__':
    create_deltio()

