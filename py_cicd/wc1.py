__author__ = "Efe Aydin"
__task__ = "SEW4/07/01"
__date__ = "02.03.2026"
__version__ = "1.2.1"
__license__ = "GNU GPLv3"
__status__ = "Released"

import re


def count(text: str) -> int:
    """
    Zählt die Anzahl der Wörter im Text
    HTML Tags werden ignoriert und Wörter bestehen nur aus A-Z bzw. a-z
    >>> count(r"")
    0
    >>> count(r" ")
    0
    >>> count(r"  ")
    0

    >>> count(r"a")
    1
    >>> count(r" a")
    1
    >>> count(r"a ")
    1
    >>> count(r" a ")
    1

    >>> count(r"one")
    1
    >>> count(r" one")
    1
    >>> count(r"one ")
    1
    >>> count(r" one ")
    1
    >>> count(r" one  ")
    1
    >>> count(r"  one ")
    1
    >>> count(r"  one  ")
    1

    >>> count(r"one:")
    1
    >>> count(r":one")
    1
    >>> count(r":one:")
    1
    >>> count(r" one  ")
    1
    >>> count(r" one : ")
    1
    >>> count(r": one :")
    1
    >>> count(r"ein erster Text")
    3
    >>> count(r" ein  erster   Text      ")
    3
    >>> count(r"ein:erster.Text")
    3

    >>> count(r" one  <html> ")
    1
    >>> count(r" one  < html> ")
    1
    >>> count(r" one  <html > ")
    1
    >>> count(r" one  < html > ")
    1
    >>> count(r" one <html> two<html>three <html> four")
    4

    >>> count(r" one <html> two ")
    2
    >>> count(r" one <html>two ")
    2
    >>> count(r" one<html> two ")
    2
    >>> count(r" one<html>two ")
    2
    >>> count(r" one<img alt=\\"xxx\\" > two")
    2
    >>> count(r" one<img alt=\\"xxx yyy\\" > two")
    2

    >>> count(r" one \\"two\\" ")
    2
    >>> count(r" one\\"two\\" ")
    2
    >>> count(r" one \\"two\\"")
    2
    >>> count(r" one \\"two\\"three")
    3
    >>> count(r" one \\"two\\" three")
    3

    >>> count(r" one<html")
    1

    >>> count(r" one<img alt=\\"<bild>\\" > two")
    2
    >>> count(r" one<img alt=\\"bild>\\" > two")
    2
    >>> count(r" one<img alt=\\"<bild>\\" keinwort> two")
    2
    >>> count(r" one<img alt=\\"<bild>\\" src=\\"bild.png\\" >two")
    2
    >>> count(r" one<img alt=\\"<bild\\" keinwort>two")
    2

    >>> count(r" one<img alt=\\"<bild\\" keinwort")
    1
    >>> count(r" one<img alt=\\"<bild\\" keinwort> two")
    2
    >>> count(r" one<img alt=\\"<bild keinwort> keinwort")
    1
    >>> count(r" one<img alt=\\"<bild keinwort keinwort\\">two")
    2
    >>> count(r" one<img alt=\\"<bild keinwort< keinwort\\">two")
    2

    >>> count(r" one<img alt=\\"<bild \\\\\\" keinwort> keinwort\\" keinwort>two")
    2
    >>> count(r" one<img alt=\\"<bild \\\\\\" keinwort<keinwort\\" keinwort>two")
    2
    >>> count(r" one<img alt=\\"<bild \\\\\\" keinwort keinwort\\" keinwort>two")
    2

    >>> count(r" \\\\\\"null\\\\\\" one<img alt=\\"<bild \\\\\\" keinwort keinwort\\" keinwort>two \\"three\\"")
    4
    """
    sauberer_text = []
    position = 0
    ist_im_tag = False
    ist_in_anfuehrung = False

    while position < len(text):
        if not ist_im_tag:
            if text[position] == "<":
                ist_im_tag = True
            else:
                sauberer_text.append(text[position])
            position += 1
        else:
            if text[position] == '"':
                anzahl_backslashes = 0
                pruef_position = position - 1

                while pruef_position >= 0 and text[pruef_position] == "\\":
                    anzahl_backslashes += 1
                    pruef_position -= 1

                if anzahl_backslashes % 4 == 1:
                    ist_in_anfuehrung = not ist_in_anfuehrung

                position += 1
            elif text[position] == ">" and not ist_in_anfuehrung:
                ist_im_tag = False
                sauberer_text.append(" ")
                position += 1
            else:
                position += 1

    return len(re.findall(r"[A-Za-z]+", "".join(sauberer_text)))