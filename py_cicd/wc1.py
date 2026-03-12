__author__ = "Efe Aydin"
__task__ = "SEW4/07/01"
__date__ = "02.03.2026"
__version__ = "1.2.1"
__license__ = "GNU GPLv3"
__status__ = "Released"

import re


def count(text):
    """
    Zählt die Anzahl der Wörter in einem gegebenen Text.

    >>> count(r"")
    0
    >>> count(r" ")
    0
    >>> count(r"  ")
    0

    Normal

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

    Mit HTML

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
    >>> count(r' one<img alt=\\"xxx\\" > two')
    2
    >>> count(r' one<img alt=\\"xxx yyy\\" > two')
    2

    >>> count(r' one \\"two\\" ')
    2
    >>> count(r' one\\"two\\" ')
    2
    >>> count(r' one \\"two\\"')
    2
    >>> count(r' one \\"two\\"three')
    3
    >>> count(r' one \\"two\\" three')
    3

    HTML - trickreich
    Achtung: das ist teilweise nicht ganz legales HTML

    >>> count(r" one<html")
    1
    >>> count(r' one<img alt=\\"<bild>\\" > two')
    2
    >>> count(r' one<img alt=\\"bild>\\" > two')
    2



    """
    sauber = re.sub(r"<[^>]*>?", " ", text)
    words = re.findall(r"[a-zA-Z]+", sauber)
    return len(words)