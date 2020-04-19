# Importing Packages 
import numpy as np # For Mathematical funnctions.
import cv2 # OpenCV.
from tkinter import Tk
from tkinter import ttk

class Encoder_LSB:
    # Decimal to Binary convertor
    def dec2bin(self,dec):
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
    def bin2dec(self,binar):
        binar = int(binar)
        dec = 0
        i = 0
        while binar > 0:
            dec = dec + (int(binar%10)*np.power(2,i))
            i = i+1
            binar = int(binar/10)
        return dec

    # XOR operation
    def XOR(self,data,key):
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

    # Secret Message into ASCII and ASCII into Binary format
    def get_cooked_data(self,secret_message, key):
        binary = ''
        count = 0
        tmp = ''
        if key.isnumeric() and (len(key) == 4):
            sum1 = 0
            for i in range(len(key)):
                sum1 = sum1 + ord(key[i])
            key = str(self.dec2bin(self,sum1))
            print("Converting Message to Binary and encrypting...")
            for pos in range(len(secret_message)):
                if ord(secret_message[pos]) <= 255:
                    if count < 8:
                        tmp = str(self.XOR(self,self.dec2bin(self,ord(secret_message[pos])),key))# coverting Secret code into ASCII and ASCII into Encrypted Binary.
                        binary = binary + tmp
                    else:
                        tmp = count = 0
            print("\nMessage Conversion Successfull.\n")
            len_b = len(binary)
            if (len_b-(int(len_b/64)*64)) != 0:
                extra = len_b-(int(len_b/64)*64)
                for pos in range(64-extra):
                    binary = binary + '0'
                
            return binary
        else:
            exit()
        
# Writing Changes to Cover Image and Generating a Steagnographed Image.
    def encoder_module(self, imagefilename, width , height, textfilename, key):

        progress_window = Tk()
        progress_window.geometry("646x67+685+189")
        progress_window.minsize(148, 1)
        progress_window.maxsize(1924, 1055)
        progress_window.resizable(0, 0)
        progress_window.title("Progress")
        progress_window.configure(background="#d9d9d9")

        TProgressbar1 = ttk.Progressbar(progress_window)
        TProgressbar1.place(relx=0.031, rely=0.194, relwidth=0.944
                , relheight=0.0, height=40)
        TProgressbar1.configure(length="610")

        img = cv2.imread(imagefilename)
        binary = self.get_cooked_data(self,textfilename, key)
        len_binary = len(binary)
        k = 0
        stegano_img = img # Initializing the steagno image with original image.

        hidden = 0

        TProgressbar1['maximum'] = len_binary

        for i in range(height):

            for j in range(width):
                if k < len_binary: 
                    b,g,r = img[i,j] # blue, green , red values in a pixel.
                    #print(np.dtype(b))
                    #print(b,g,r)
                    bin_b = int(self.dec2bin(self,b)) # binary form of blue pixel value.
                    bin_g = int(self.dec2bin(self,g)) # binary form of green pixel value.
                    bin_r = int(self.dec2bin(self,r)) # binary form of red pixel value.
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
                    b = np.uint8(self.bin2dec(self,bin_b))
                    g = np.uint8(self.bin2dec(self,bin_g))
                    r = np.uint8(self.bin2dec(self,bin_r))
                    stegano_img[i,j] = [b,g,r]
                    hidden = hidden + 1 
                    #print(img[i,j],steagno_img[i,j])

                    TProgressbar1['value'] = k
                    TProgressbar1.update()    

                else:
                    break

        steagnoimagefilename = ''
        sub = ''
        for m in range(len(imagefilename)):
            if imagefilename[m] == '.' and imagefilename[m+1:len(imagefilename)] == 'png':
                steagnoimagefilename = sub + "_stegano_LSB.png"
                break
            else:
                sub += imagefilename[m]
        
        cv2.imwrite(steagnoimagefilename,stegano_img)
        progress_window.destroy()
        
        return steagnoimagefilename