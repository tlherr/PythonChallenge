from urllib.request import urlopen
import url
import re

uri = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s"

nothing = 12345
nothing_again = str(16044/2);
pattern = re.compile("and the next nothing is (\d+)")


while True:
    content = urlopen(uri % nothing).read().decode('utf-8')
    print(content)
    match = pattern.search(content)
    if match == None:
        break
    nothing = match.group(1)
    print(nothing)

while True:
    content = urlopen(uri % nothing_again).read().decode('utf-8')
    print(content)
    match = pattern.search(content)
    if match == None:
        break
    nothing_again = match.group(1)
    print(nothing_again)
