# Importing Packages 
import numpy as np # For Mathematical funnctions.
import cv2 # OpenCV.

# Reading an Image through Opencv
img = cv2.imread('original.png')
# img = cv2.resize(img,(500,500))

# Capturing the size of the Cover Image.
height,width,pixels = img.shape
# print("height ",height,"\nwidth",width)

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
    #print("data ",data)
    key = str(key)
    #print("key ",key)
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

t = np.random.randint(2,size=(1999999))
binary = ""
for e in range(len(t)):
    binary = binary + str(t[e])
        
# Writing Changes to Cover Image and Generating a Steagnographed Image.
len_binary = len(binary)
print("text_length = ",len_binary)
k = 0
steagno_img = img # Initializing the steagno image with original image.

hidden = 0

for i in range(height):
    for j in range(width):
        if k < len_binary: 
            b,g,r = img[i,j] # blue, green , red values in a pixel.
            #print(np.dtype(b))
            #print(b,g,r)
            bin_b = int(dec2bin(b)) # binary form of blue pixel value.
            bin_g = int(dec2bin(g)) # binary form of green pixel value.
            bin_r = int(dec2bin(r)) # binary form of red pixel value.
            #print(bin_b,bin_g,bin_r)
            
            if k < len_binary:
                #print('bin_b ',bin_b)
                if int(bin_b % 10) == int(binary[k]):
                    k = k+1
                else:
                    if int(bin_b%10) == 0:
                        bin_b = (int(bin_b/10)*10) + 1
                    else:
                        bin_b = int(bin_b/10)*10
                    k = k+1
                #print('bin_b ',bin_b)
                    
            if k < len_binary:
                #print('bin_g ',bin_g)
                if int(bin_g % 10) == int(binary[k]):
                    k = k+1
                else:
                    if int(bin_g%10) == 0:
                        bin_g = (int(bin_g/10)*10) + 1
                    else:
                        bin_g = int(bin_g/10)*10
                    k = k+1
                #print('bin_g ',bin_g)
                
            if k < len_binary:
                #print('bin_r ',bin_r)
                if int(bin_r % 10) == int(binary[k]):
                    k = k+1
                else:
                    if int(bin_r%10) == 0:
                        bin_r = (int(bin_r/10)*10) + 1
                    else:
                        bin_r = int(bin_r/10)*10
                    k = k+1
                #print('bin_r ',bin_r)
            
            #print(bin_b,bin_g,bin_r)
            # Updating the original Pixel values. 
            b = np.uint8(bin2dec(bin_b))
            g = np.uint8(bin2dec(bin_g))
            r = np.uint8(bin2dec(bin_r))
            steagno_img[i,j] = [b,g,r]
            hidden = hidden + 1 
            #print(img[i,j],steagno_img[i,j])
                
        else:
            break;
     
cv2.imwrite('steagno_image.png',steagno_img)
print("\nWriting Successfull.\n")
print(hidden," bits written")