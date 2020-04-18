import numpy as np
import cv2
from tkinter import Tk
from tkinter import ttk

class Encoder_bcps:
    # XOR operation for our data 
    def XOR(self, data,key):
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

    # XOR operation
    def XOR1(self, h,w,d1,d2):
        enc_data = np.zeros((h,w,1),np.uint8)
        for ext_data in range(h):
            for ext_dataj in range(w):
                if (int(d1[ext_data,ext_dataj]) == 0) and (int(d2[ext_data,ext_dataj]) == 0):
                    enc_data[ext_data,ext_dataj] =  0
                elif (int(d1[ext_data,ext_dataj]) == 0) and (int(d2[ext_data,ext_dataj]) == 1):
                    enc_data[ext_data,ext_dataj] =  1
                elif (int(d1[ext_data,ext_dataj]) == 1) and (int(d2[ext_data,ext_dataj]) == 0):
                    enc_data[ext_data,ext_dataj] =  1
                elif (int(d1[ext_data,ext_dataj]) == 1) and (int(d2[ext_data,ext_dataj]) == 1):
                    enc_data[ext_data,ext_dataj] =  0
        return enc_data

    # To calculate the complexity of a 8*8 block of binary image
    def alpha1(self, h,w,b):
        x = 0
        count = 0
        change = 0
        for j in range(h):
            for k in range(w):
                if j == 0 and k == 0:
                    count = 0
                    change = int(b[j,k])
                else:
                    if change != int(b[j,k]):
                        count = count + 1
                        change = int(b[j,k])
        x = count/(h*w-1)
        return x      

    # To conjugate a block of binary image
    def conjugate(self, h,w,b_ex):  
        wc = np.zeros((h,w,1),np.uint8)
        for i in range(8):
            for j in range(8):
                if int(j%2) != 0:
                    wc[i,j] = 1

        b_ex_tmp = self.XOR1(self,h,w,wc,b_ex)
        return b_ex_tmp

    # Decimal to Binary convertor
    def dec2bin(self, dec):
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
    def bin2dec(self, binar):
        binar = int(binar)
        dec = 0
        i = 0
        while binar > 0:
            dec = dec + (int(binar%10)*np.power(2,i))
            i = i+1
            binar = int(binar/10)
        return dec

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


    #encoder Module
    def encoder_module(self, imagefilename, width , height, textfilename, key):

        ct_indic = 0
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
        channels = 3

        TProgressbar1['maximum'] = 3*8

        binary = self.get_cooked_data(self, textfilename, key)
        print(len(binary))

        img_b = np.zeros((height,width,1),np.uint8)
        img_g = np.zeros((height,width,1),np.uint8)
        img_r = np.zeros((height,width,1),np.uint8)

        sub_img = np.zeros((height,width,1),np.uint8)

        #tp1.TProgressbar['maximum'] = 8*channels*height

        bit_coded = 0
        for color in range(channels):

            for m in range(height):

                for n in range(width):
                    b,g,r = img[m,n]
                    
                    if color == 0:
                        sub_img[m,n] = b
                        
                    elif color == 1:
                        sub_img[m,n] = g
                        
                    elif color == 2:
                        sub_img[m,n] = r
                        
            img_sub1 = np.zeros((height,width,1),np.uint8)
            img_sub2 = np.zeros((height,width,1),np.uint8)
            img_sub3 = np.zeros((height,width,1),np.uint8)
            img_sub4 = np.zeros((height,width,1),np.uint8)
            img_sub5 = np.zeros((height,width,1),np.uint8)
            img_sub6 = np.zeros((height,width,1),np.uint8)
            img_sub7 = np.zeros((height,width,1),np.uint8)
            img_sub8 = np.zeros((height,width,1),np.uint8)

            meta_loc = 0
            meta_data = ''
            for indic in range(8):

                ct_indic = ct_indic + 1
                TProgressbar1['value'] = ct_indic
                TProgressbar1.update()

                patched_loc = ''
                meta_data = ''
                bt = np.zeros((height,width,1),np.uint8)
                for m in range(height):

                    for n in range(width):
                        shape = str(self.dec2bin(self,sub_img[m,n]))
                        if indic == 0:
                            img_sub1[m,n] = int(shape[indic])
                        elif indic == 1:
                            img_sub2[m,n] = int(shape[indic])
                        elif indic == 2:
                            img_sub3[m,n] = int(shape[indic])
                        elif indic == 3:
                            img_sub4[m,n] = int(shape[indic])
                        elif indic == 4:
                            img_sub5[m,n] = int(shape[indic])
                        else:
                            bt[m,n] = int(shape[indic])
                if indic > 4:
                    mn = []
                    if (height-(int(height/8)*8)) >= 4:
                        meta_loc = (int(height/8)*8)
                        
                    elif (height-(int(height/8)*8)) < 4:
                        meta_loc = (int(height/8)*8) - 8
                    
                    for m in range(0,meta_loc,8):
                        for n in range(0,int(width/8)*8,8):
                            
                            oalpha = self.alpha1(self,8,8,bt[m:m+8,n:n+8])
                            mn.append(oalpha)
                            
                    mean1 = np.mean(mn)
                    std1 = np.std(mn)
                    
                    count1 = bit_coded
                    
                    for m in range(0,meta_loc,8):

                        for n in range(0,int(width/8)*8,8):
                            if bit_coded < len(binary):
                                count1 = bit_coded

                                oalpha = self.alpha1(self,8,8,bt[m:m+8,n:n+8])
                                bi = np.zeros((8,8,1),np.uint8)
                                for i in range(8):
                                    for j in range(8):
                                        if count1 < len(binary):
                                            bi[i,j] = int(binary[count1])
                                            count1 = count1 + 1

                                dalpha = self.alpha1(self,8,8,bi)
                                if oalpha > (mean1-0*std1):

                                    if dalpha <= (mean1-0*std1):

                                        b_con = self.conjugate(self,8,8,bi) 
                                        bt[m:m+8,n:n+8] = b_con
                                        patched_loc = patched_loc + "1"
                                        bit_coded = bit_coded + 64

                                    else:

                                        bt[m:m+8,n:n+8] = bi
                                        patched_loc = patched_loc + "0"
                                        bit_coded = bit_coded + 64


                    len_patch = len(patched_loc)
                        
                    if len(patched_loc)-(int(len(patched_loc)/8)*8) != 0:
                        for a in range(8-len(patched_loc)-(int(len(patched_loc)/8)*8)):
                            patched_loc = patched_loc + "0"
                        
                    tmp_patch_loc = ''
                        
                    for a in range(0,len(patched_loc),8):
                        tmp_patch_loc = tmp_patch_loc + str(self.bin2dec(self,patched_loc[a:a+8]))+"@"
                        
                    patched_loc = tmp_patch_loc
                        
                    if len(patched_loc)-(int(len(patched_loc)/8)*8) != 0:
                        for a in range(8-len(patched_loc)-(int(len(patched_loc)/8)*8)):
                            patched_loc = patched_loc + "0"
                        
                    patched_loc = patched_loc + " " + str(len_patch) + " "
                        
                    meta_data = ''
                    tmp_meta = str(meta_loc)+" "+str(mean1)+" "+str(std1)+" "+str(len(binary))+" "+patched_loc
                    
                    for m in range(len(tmp_meta)):
                        meta_data = meta_data + str(self.dec2bin(self,ord(tmp_meta[m])))

                    meta_ct = 0    
                    for m in range(meta_loc+1,height):
                        for n in range(width):
                            if meta_ct >= len(meta_data):
                                break
                            if bt[m,n] != int(meta_data[meta_ct]):
                                bt[m,n] = int(meta_data[meta_ct])
                            meta_ct = meta_ct + 1
                    
                    n = indic + 1
                    if n == 1:
                        img_sub1 = bt
                    elif n == 2:
                        img_sub2 = bt
                    elif n == 3:
                        img_sub3 = bt
                    elif n == 4:
                        img_sub4 = bt
                    elif n == 5:
                        img_sub5 = bt
                    elif n == 6:
                        img_sub6 = bt
                    elif n == 7:
                        img_sub7 = bt
                    elif n == 8:
                        img_sub8 = bt
                        
            img_channel = np.zeros((height,width,1),np.uint8)
            for m in range(height):
                for n in range(width):
                    stegano = str(int(img_sub1[m,n]))+str(int(img_sub2[m,n]))+str(int(img_sub3[m,n]))+str(int(img_sub4[m,n]))+str(int(img_sub5[m,n]))+str(int(img_sub6[m,n]))+str(int(img_sub7[m,n]))+str(int(img_sub8[m,n]))
                    img_channel[m,n] = np.uint8(self.bin2dec(self,stegano))
                    
            if color == 0:
                img_b = img_channel 
                        
            elif color == 1:
                img_g = img_channel
                        
            elif color == 2:
                img_r = img_channel

        stegano_img = np.zeros((height,width,3),np.uint8)
        for m in range(height):
            for n in range(width):
                stegano_img[m,n] = img_b[m,n],img_g[m,n],img_r[m,n]

        print(bit_coded," were coded")
        #cv2.imshow("cover image",img)
        #cv2.imshow("stegano image",stegano_img)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()
        progress_window.destroy()
        steagnoimagefilename = ''
        sub = ''
        for m in range(len(imagefilename)):
            if imagefilename[m] == '.' and imagefilename[m+1:len(imagefilename)] == 'png':
                steagnoimagefilename = sub + "_steagno.png"
                break
            else:
                sub += imagefilename[m]
        
        cv2.imwrite(steagnoimagefilename,stegano_img)
        return steagnoimagefilename

# Main function
#if __name__ == "__main__":
#    Encoder_bcps.encoder_module(Encoder_bcps,imagefilename = "C:\\Users\\himes\\notebooks\\cover_raw.png",textfilename = "hello world!!",key ="7607")