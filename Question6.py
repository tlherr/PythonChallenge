# Raw data from http://www.pythonchallenge.com/pc/def/banner.p
from urllib.request import urlopen
import pickle

data = pickle.load(urlopen("http://www.pythonchallenge.com/pc/def/banner.p"))

# Now have a list of tuples (list like sequences)
# Tuples are number of characters and character to print
# Example (' ', 5) = print 5 spaces

# Iterate through each element
for line in data:
    for each_item in line:
        print(each_item[0]*each_item[1], end='')
    # After each item in the line has been processed print a newline
    print()
