#####TEAM BASTET
#####PROGRAM 2
#####VIGENERE

###imports
import sys

##assigning some variables
option = sys.argv[1]
key = sys.argv[2]

##defining the encrypt and decrypt functions
def encrypt(key, plaintext):
    
    #make the key's lettercasing irrelevant
    key = key.lower()

    #create the cyphertext local
    cyphertext = ""

    #ensuring the key is long enough
    key = key * len(plaintext)
    
    
    #encrypt
    for i in range(len(plaintext)):
        ##if lowercase
        ##ranges from 97 to 122
        
        if(ord(plaintext[i]) >= 97 and ord(plaintext[i]) <= 122):
            temp = ((ord(plaintext[i])-97) + (ord(key[i])-97))%26
            cyphertext += chr(temp+97)
            
        
        ##if uppercase
        ##ranges from 65 to 90
        elif(ord(plaintext[i]) >= 65 and ord(plaintext[i]) <= 90):
            temp = ((ord(plaintext[i])-65) + (ord(key[i])-97))%26
            cyphertext += chr(temp+65)
            
        
        ##if not a letter
        ##keep it the same 
        else:
            cyphertext += plaintext[i]
            
    print(cyphertext)
    

def decrypt(key, cyphertext):
    
    #make the key's lettercasing irrelevant
    key = key.lower()
    
    #create the plaintext local
    plaintext = ""
    
    #ensuring the key is long enough
    key = key * len(cyphertext)
    
    #decrypt
    for i in range(len(cyphertext)):
        ##if lowercase
        if(ord(cyphertext[i]) >= 97 and ord(cyphertext[i]) <= 122):
            temp = (26 + (ord(cyphertext[i])-97) - (ord(key[i])-97))%26
            plaintext += chr(temp+97)
        
        ##if uppercase
        elif(ord(cyphertext[i]) >= 65 and ord(cyphertext[i]) <= 90):
            temp = (26 + (ord(cyphertext[i])- 65) - (ord(key[i])-97))%26
            plaintext += chr(temp+65)
        
        ##if anything other than a letter
        else:
            plaintext += cyphertext[i]
            
    print(plaintext)
#check to see if we are decrypting or encrypting
##############################################
    
#if -e, encrypting
if(option == "-e"):
    print("encrypting")
    
    #start the loop
    while(True):
        plaintext = input()
        
        encrypt(key, plaintext)


#############################################
#if -d, decrypting
elif(option == "-d"):
    print("decrypting")
    
    #start the loop
    while(True):
        cyphertext = input()
        
        decrypt(key, cyphertext)

#############################################
#else, display error message
else:
    print("invalid parameters, type either '-d' to decrypt or '-e' to encrypt")  

#############################################
