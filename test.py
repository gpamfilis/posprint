# coding: utf-8

__author__ = 'gpamfilis'

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import requests



def get_order(order_id):
    data = requests.get("http://www.e-orders.org/api/app/order?order_id="+str(order_id))
    json = data.json()
    return json





def create_deltio():
    json = get_order(1)

    width = 500
    height = 100
    back_ground_color = (255, 255, 255)
    font_size = 36
    font_color = (0, 0, 0)
    im = Image.new("RGB", (width, height), back_ground_color)
    unicode_font = ImageFont.truetype('/Library/Fonts/Arial.ttf', font_size)

    items = json["items"]
    for item in items:
        name = item["name"]
        # unicode_text = unicode(name, "utf-8")
        draw = ImageDraw.Draw(im)
        draw.text((10, 10), name, font=unicode_font, fill=font_color)
    im.save("text.jpg")



def test1():
    # configuration
    width = 500
    height = 100
    back_ground_color = (255, 255, 255)
    font_size = 36
    font_color = (0, 0, 0)
    unicode_text = u = unicode("τεσ΄κα'δς΄φκασδ", "utf-8")
    im = Image.new("RGB", (width, height), back_ground_color)
    draw = ImageDraw.Draw(im)
    unicode_font = ImageFont.truetype('/Library/Fonts/Arial.ttf', font_size)
    draw.text((10, 10), unicode_text, font=unicode_font, fill=font_color)
    im.save("text.jpg")


if __name__ == '__main__':
    create_deltio()
    # img = Image.new('RGB', (200, 100))
    # d = ImageDraw.Draw(img)
    # d.text((20, 20), 'Hello', fill=(255, 0, 0))
    #
    # text_width, text_height = d.textsize('Hello')
    #
    # img = Image.new('RGB', (200, 100), (255, 255, 255))
    #
    # import cStringIO
    #
    # s = cStringIO.StringIO()
    # # img.save(s, 'png')
    # img.show()
    # in_memory_file = s.getvalue()
    #
    # raw_img_data = img.tobytes()
    #

    # font = ImageFont.truetype("sans-serif.ttf", 16)

    # img = Image.open("sample_in.jpg")
    # img = Image.new('RGB', (640, 480), (255, 255, 255))
    #
    # img.save('test.png')
    #
    #
    # img = Image.open("test.png")
    #
    # draw = ImageDraw.Draw(img)
    # # # font = ImageFont.truetype(<font-file>, <font-size>)
    # font = ImageFont.truetype('/Library/Fonts/Arial.ttf', 20, encoding="utf-8")
    # # draw.text((x, y),"Sample Text",(r,g,b))
    # draw.text((20, 20), "ψδκλξ", (0, 0, 0), font=font)
    # img.save('sample-out.jpg')