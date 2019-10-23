#import sys
# print "This is the name of the script: ", sys.argv[0]
# print "Number of arguments: ", len(sys.argv)
# print "The arguments are: " , str(sys.argv)
# with open('files/random-names.txt', 'r') as random_names:

import re
import sys
regex = re.compile("^([A-z]+) ([A-z]+)")
with open(sys.argv[1], 'r') as random_names:
    for line in random_names:
        print(regex.search(line).group(2), regex.search(line).group(1))

