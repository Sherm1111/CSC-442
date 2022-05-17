#Team: Bastet:  Winkelmann, Andrew Turner, Jacob Roberts, Christopher Johnson, Broady Rivet, Dakota Suire
#Program: XOR
#Date: May 5 2022
import sys

# Reads in the key as a byte array from the file named  "key"
key = open("key.bmp","rb").read()

# Reads in text as a bytearray from stdin
input_text = bytearray(sys.stdin.buffer.read())

i_len = len(input_text) # Length of input
k_len = len(key)    # Length of key

output = [] # Stores the XORd text as a list of bytes
for i in range(i_len): output.append(input_text[i]^key[i%k_len]) # Bitwise XORs the key and cipher

# Outputs the XORd text as binary data
sys.stdout.buffer.write(bytearray(output))
