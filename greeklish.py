# coding: utf-8
__author__ = 'gpamfilis'

from string import maketrans, translate


def main(strings):
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


if __name__ == "__main__":
    a = main("η ψωλη ενος ανθρωπου λαλαλαλα. ΛΑ.!!!")
    print(a)
