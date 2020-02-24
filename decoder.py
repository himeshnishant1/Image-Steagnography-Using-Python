import numpy as np
import cv2

# Decimal to Binary convertor
def dec2bin(dec):
    inverse = ''
    binary = ''
    while dec != 0:
        inverse = inverse + str( int(dec % 2) )
        dec = int(dec / 2)
    if len(inverse) <= 8:
        size = len(inverse)
        for i in range(8-size):
            inverse = inverse + '0'
    for i in range(len(inverse)-1,-1,-1):
        binary = binary + str(inverse[i])
    return binary

# Binary to Decimal convertor
def bin2dec(binar):
    binar = int(binar)
    dec = 0
    i = 0
    while binar > 0:
        dec = dec + (int(binar%10)*np.power(2,i))
        i = i+1
        binar = int(binar/10)
    return dec

extracted_code = ''
steagno1_img = cv2.imread('steagno_image.jpeg',)
for i in range(100):
    for j in range(960):
        b,g,r = steagno1_img[i,j] # blue, green , red values in a pixel.
        bin_b = int(dec2bin(b)) # binary form of blue pixel value.
        bin_g = int(dec2bin(g)) # binary form of green pixel value.
        bin_r = int(dec2bin(r)) # binary form of red pixel value.
            
        extracted_code = extracted_code + str(int(bin_b%10)) + str(int(bin_g%10)) + str(int(bin_r%10))
print("Code Extraction Completed.")
#for i in range(len(binary)):
#    print(extracted_code[i],' ',binary[i])
print("Now decoding the message.")
word = ''
for len in range(0,len(extracted_code),8):
    #print(extracted_code[len:(len+8)],'  ',chr(bin2dec(int(extracted_code[len:(len+8)]))))
    word =  word + str(chr(bin2dec(int(extracted_code[len:(len+8)]))))
print(word)