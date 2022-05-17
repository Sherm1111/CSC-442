#####TEAM BASTET
#####PROGRAM 2
#####VIGENERE


###imports
import sys

##check for the correct number of parameters
if(len(sys.argv) < 3):
    print("Invalid number of parameters")
    print("Ex. 'python3 vigenere.py [-d or -e] [key] [plaintext or cyphertext]'")
    exit()
    

##assigning some variables

option = sys.argv[1]
key = sys.argv[2]

##defining the encrypt and decrypt functions

def encrypt(key, plaintext):
    
    #make the key's lettercasing irrelevant
    key = key.lower()
    
    #remove all spaces from the key
    key = key.replace(" ", "")

    #create the cyphertext local
    cyphertext = ""

    #ensuring the key is long enough
    key = key * len(plaintext)
    
    #use a separate variable to iterate through the key, trust
    a = 0
    #encrypt
    for i in range(len(plaintext)):
        
        
        ##if lowercase
        ##ranges from 97 to 122
        
        if(ord(plaintext[i]) >= 97 and ord(plaintext[i]) <= 122):
            temp = ((ord(plaintext[i])-97) + (ord(key[a])-97))%26
            cyphertext += chr(temp+97)
            a+=1
            
        
        ##if uppercase
        ##ranges from 65 to 90
        elif(ord(plaintext[i]) >= 65 and ord(plaintext[i]) <= 90):
            temp = ((ord(plaintext[i])-65) + (ord(key[a])-97))%26
            cyphertext += chr(temp+65)
            a+=1
            
        
        ##if not a letter
        ##keep it the same
        ##make sure you don't iterate through the key in this case
        else:
            cyphertext += plaintext[i]
            
    print(cyphertext)
    

def decrypt(key, cyphertext):
    
    #make the key's lettercasing irrelevant
    key = key.lower()
    
    #remove all spaces from the key
    key = key.replace(" ", "")
    
    #create the plaintext local
    plaintext = ""
    
    #ensuring the key is long enough
    key = key * len(cyphertext)
    
    #use a separate variable to iterate through the key, trust
    a = 0
    #decrypt
    for i in range(len(cyphertext)):
        ##if lowercase
        if(ord(cyphertext[i]) >= 97 and ord(cyphertext[i]) <= 122):
            temp = (26 + (ord(cyphertext[i])-97) - (ord(key[a])-97))%26
            plaintext += chr(temp+97)
            a+=1
        
        ##if uppercase
        elif(ord(cyphertext[i]) >= 65 and ord(cyphertext[i]) <= 90):
            temp = (26 + (ord(cyphertext[i])- 65) - (ord(key[a])-97))%26
            plaintext += chr(temp+65)
            a+=1
        
        ##if anything other than a letter
        else:
            plaintext += cyphertext[i]
            
    print(plaintext)
        
    
    

#check to see if we are decrypting or encrypting
##############################################
    
#if -e, encrypting
if(option == "-e"):
    #start the loop
    while(True):
    
        #when you use Control D, it throws an EOF error, so when that error occurs just exit
        try:
    
            plaintext = input()
            
            encrypt(key, plaintext)
        
        except EOFError:
            exit()


#############################################
#if -d, decrypting
elif(option == "-d"): 
    #start the loop
    while(True):
        
        #when you use Control D, it throws an EOF error, so when that error occurs just exit 
        try:
            cyphertext = input()
            
            decrypt(key, cyphertext)
        except EOFError:
            exit()

#############################################
#else, display error message
else:
    print("invalid parameters, type either '-d' to decrypt or '-e' to encrypt")
    print("Ex. 'python3 vigenere.py [-d or -e] [key] [plaintext or cyphertext]'")

##############################################
