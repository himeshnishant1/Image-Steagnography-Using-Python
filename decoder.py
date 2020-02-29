# Importing Packages 
import numpy as np # For Mathematical funnctions.
import cv2 # OpenCV.

# Reading an Image through Opencv
img = cv2.imread('original.jpeg')
# img = cv2.resize(img,(500,500))

# Capturing the size of the Cover Image.
height,width,pixels = img.shape
print("height ",height,"\nwidth",width)

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

# XOR operation
def XOR(data,key):
    data = str(data)
    print("data ",data)
    key = str(key)
    print("key ",key)
    enc_data = ''
    for ext_data in range(len(data)):
        if data[ext_data] == '0' and key[ext_data] == '0':
            enc_data = enc_data + '0'
        elif data[ext_data] == '0' and key[ext_data] == '1':
            enc_data = enc_data + '1'
        elif data[ext_data] == '1' and key[ext_data] == '0':
            enc_data = enc_data + '1'
        elif data[ext_data] == '1' and key[ext_data] == '1':
            enc_data = enc_data + '0'
    return enc_data

# Extracting the Secret Message for the Image.
steagno1_img = cv2.imread('steagno_image.png') # Reading an Steagnographed Image.
#print(steagno_img[0,0],img[0,0])
sum1 = 0
key = input("Enter your key..")
for i in range(len(key)):
        sum1 = sum1 + ord(key[i])
key = str(dec2bin(sum1))
print(key)
extracted_code = ''
print("Extracting Code...")
for i in range(100):
    for j in range(960):
        b,g,r = steagno1_img[i,j] # blue, green , red values in a pixel.
        bin_b = int(dec2bin(b)) # binary form of blue pixel value.
        bin_g = int(dec2bin(g)) # binary form of green pixel value.
        bin_r = int(dec2bin(r)) # binary form of red pixel value.
        extracted_code = extracted_code + str(int(bin_b%10)) + str(int(bin_g%10)) + str(int(bin_r%10))
print("Code Extraction Completed.")
print("Now Coverting message to Readable format...")
word = ''
for len in range(0,len(extracted_code),8):
    word =  word + str(chr(bin2dec(XOR(extracted_code[len:(len+8)],key))))
print(word)