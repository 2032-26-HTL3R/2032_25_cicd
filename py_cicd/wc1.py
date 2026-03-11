__author__ = "Efe Aydin"
__task__ = "SEW4/07/01"
__date__ = "02.03.2026"
__version__ = "1.2.1"
__license__ = "GNU GPLv3"
__status__ = "Released"

import re

def count(text):
    """
    Zählt die Anzahl der Wörter in einem gegebenen Text
    :param text:
    :return:

    >>> count("eins")
    1
    >>> count("eins")
    1
    >>> count("ein erster Text")
    3
    >>> count("ein <html>eins</html> zwei")
    3
    """
    sauber = re.sub(r'<[^>]*>', '', text)
    words = re.findAll(r'[a-zA-Z]+', sauber)
    return len(words)


