# Group 3, BASTET, Nicholas Winkelmann, Andrew Turner, Jacob Roberts, Dakota Suire, Christopher Johnson, and Broady Rivet
# script for ftp stuff
from ftplib import FTP
import re

IP = "138.47.99.64"
PORT = 21
USER = "anonymous"
PASSWORD = ""
FOLDER = "7"
USE_PASSIVE = True

#---change METHOD here!!!!-------
METHOD = 7
#--------------------------------

ftp = FTP()
ftp.connect(IP, PORT)
ftp.login(USER, PASSWORD)
ftp.set_pasv(USE_PASSIVE)

ftp.cwd(FOLDER)
files = []
ftp.dir(files.append)

ftp.quit()

# holder variable for string 
holder = ""
bin = ""
#blank array 
array = []

# iterate through files and separate the "bits" based on the the METHOD
for f in files :
    if METHOD == 7 :
        if f[0] == '-' and f[1] == '-' and f[2] == '-' :
            holder += f[3:10]
    else :
        holder += f[:10]
# loop converting every r, w, x, and d into a 1 and 0 otherwise
for i in holder :
    if i == 'r' or i == 'w' or i == 'x' or i == 'd':
        bin += "1"
    else :
        bin += "0"
# putting groups of 7 into an array, for binary conversion
array = re.findall('.......', bin)
result = ""
# iterate through array, and convert to characters
for j in range(len(array)) :
    result += chr(int(array[j], 2))
# print
print(result)