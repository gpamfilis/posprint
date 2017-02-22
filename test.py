# coding: utf-8

__author__ = 'gpamfilis'

from PIL import Image, ImageDraw, ImageFont
import requests


def get_order(order_id):
    data = requests.get("http://www.e-orders.org/api/app/order?order_id="+str(order_id))
    json = data.json()
    print(json)
    return json


def create_deltio(order_id):
    json = get_order(order_id)
    items = json["items"]

    n_orders = len(items)
    print(n_orders)
    width = 350
    height = 50 * (n_orders+1)
    h = 50 * n_orders*3

    back_ground_color = (255, 255, 255)
    font_size = 30
    font_color = (0, 0, 0)
    im = Image.new("RGB", (width, height), back_ground_color)
    unicode_font = ImageFont.truetype('./fonts/arial.ttf', font_size)

    items = json["items"]
    draw = ImageDraw.Draw(im)
    d_line = font_size
    draw.text((10, 0), "Table Name", font=unicode_font, fill=font_color)
    for item in items:
        name = item["name"]
        print(name)
        # unicode_text = unicode(name, "utf-8")
        draw.text((10, d_line), "x" + str(item["quantity"]) + " "+name, font=unicode_font, fill=font_color)
        d_line += h/(n_orders*4)
    im.save("text.png")


if __name__ == '__main__':
    create_deltio(10)

