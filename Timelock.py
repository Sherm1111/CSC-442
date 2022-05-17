#Team: Bastet:  Winkelmann, Andrew Turner, Jacob Roberts, Christopher Johnson, Broady Rivet, Dakota Suire
#Program Timelock
#Date: May 5 2022
import sys
import hashlib
from datetime import *

# get the first two letters
def letters(s):
    only_alpha = ""
    for char in s:
        if ord(char) >= 65 and ord(char) <= 90:
            only_alpha += char
        elif ord(char) >= 97 and ord(char) <= 122:
            only_alpha += char
    return only_alpha[:2]

# get the last two digits from the str
def numbers(s):
    only_numb = ""
    for char in s:
        if char.isdigit():
            only_numb += char
    return only_numb[-2:]

#current time
current = datetime.now()
#current = "2017 04 23 18 02 30"
current1 = current
#current = datetime.strptime(current, "%Y %m %d %H %M %S")

#epoch time
epoch = sys.stdin.readline()
epoch = epoch.strip('\n')       #remove new line
epoch = datetime.strptime(epoch, "%Y %m %d %H %M %S")

#difference
diff = current.timestamp() - epoch.timestamp()
diff = int(diff-(diff%60))

#md5 double hash
hashy = str(diff)
hashy = hashlib.md5((hashlib.md5(hashy.encode())).hexdigest().encode()).hexdigest()
print(hashy)
#print letters/numbers
holder1 = letters(hashy)
holder2 = numbers(hashy)
holder2 = holder2[::-1]

final = holder1 + holder2
len1 = len(hashy)
#middle = len1//2
#print(hashy[middle])
print(final)

print("current system time: {}".format(current1))
