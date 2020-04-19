import numpy as np
import cv2

class Decoder_BCPS:
    # XOR operation for our data 
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

    # XOR operation for conjugation
    def XOR1(self,h,w,d1,d2):
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
    def alpha1(self,h,w,b):
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
    def conjugate(self,h,w,b_ex):  
        wc = np.zeros((h,w,1),np.uint8)
        for i in range(8):
            for j in range(8):
                if int(j%2) != 0:
                    wc[i,j] = 1

        b_ex_tmp = self.XOR1(self,h,w,wc,b_ex)
        return b_ex_tmp

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

    # To extract the data from block of binary image to a string format
    def ext_data(self,h,w,d):
        tmp_data = ""
        for a in range(h):
            for b in range(w):
                tmp_data = tmp_data + str(int(d[a,b]))
        return tmp_data

    #decoder module
    def decoder_module(self, imagefilename, width , height, key):
        stegano_image = cv2.imread(imagefilename)

        sub_img = np.zeros((height,width,1),np.uint8)

        bin_data = ''
        data = ''

        for color in range(3):
            for m in range(height):
                for n in range(width):
                    b,g,r = stegano_image[m,n]
                    
                    if color == 0:
                        sub_img[m,n] = b
                        
                    elif color == 1:
                        sub_img[m,n] = g
                        
                    elif color == 2:
                        sub_img[m,n] = r

            meta_loc = 0
            meta_data = ''
            for indic in range(5,8):
                
                patched_loc = ''
                meta_data = ''
                patched_indic = 0

                mean1 = 0.0
                std1 = 0.0
                patched_loc = ''
                patch_loc_len = 0
                
                bt = np.zeros((height,width,1),np.uint8)
                for m in range(height):
                    for n in range(width):
                        shape = str(self.dec2bin(self,sub_img[m,n]))
                        if indic > 4:
                            bt[m,n] = int(shape[indic])
                        else:
                            break
                
                if indic > 4:
                    
                    if (height-(int(height/8)*8)) >= 4:
                        meta_loc = (int(height/8)*8)
                        
                    elif (height-(int(height/8)*8)) < 4:
                        meta_loc = (int(height/8)*8) - 8
                    
                    bt_str = ''
                    for m in range(meta_loc+1,height):
                        for n in range(width):
                            bt_str = bt_str + str(int(bt[m,n]))
                            
                    ct = 0
                    for n in range(0,len(bt_str),8):
                        tmp_bt = ''
                        for a in range(n,n+8):
                            tmp_bt  = tmp_bt + bt_str[a]
                                    
                        if str(chr(int(self.bin2dec(self,int(tmp_bt))))) == ' ':
                            
                            if ct == 0:
                                if meta_data != str(meta_loc):
                                    break
                            
                            elif ct == 1:
                                mean1 = float(meta_data)

                            elif ct == 2:
                                std1 = float(meta_data)
                                
                            elif ct == 3:
                                len_binary = int(meta_data)
                                
                            elif ct == 4:
                                patched_loc = meta_data
                                
                            elif ct == 5:
                                patch_loc_len = int(meta_data)
                                
                            else:
                                break
                            
                            ct = ct + 1
                            meta_data = ""
                            
                        else:
                            meta_data = meta_data + str(chr(int(self.bin2dec(self,int(tmp_bt)))))
                                
                    
                    tmp_patched_loc = ''
                    sub_str = ''   
                    
                    for a in range(len(patched_loc)):
                        
                        if patched_loc[a] == '@':
                            
                            tmp_patched_loc = tmp_patched_loc + str(self.dec2bin(self,int(sub_str)))
                            sub_str = ''
                            
                        else:
                            
                            sub_str = sub_str + patched_loc[a]
                    
                        
                    patched_loc = tmp_patched_loc[0:patch_loc_len]
                    
                    if len(patched_loc) != 0:
                        for m in range(0,meta_loc,8):
                            for n in range(0,int(width/8)*8,8):
                                if patched_indic < patch_loc_len:
                                    
                                    oalpha = self.alpha1(self,8,8,bt[m:m+8,n:n+8])

                                    if oalpha > (mean1-0*std1):
                                        
                                        if patched_loc[patched_indic] == "1":

                                            b_con = self.conjugate(self,8,8,bt[m:m+8,n:n+8]) 
                                            bin_data = bin_data + self.ext_data(self,8,8,b_con)  

                                        elif patched_loc[patched_indic] == "0":

                                            bin_data = bin_data + self.ext_data(self,8,8,bt[m:m+8,n:n+8])

                                        patched_indic = patched_indic + 1
                                    
        data = ''
        sum1 = 0
        for i in range(len(key)):
            sum1 = sum1 + ord(key[i])
        key = str(self.dec2bin(self,sum1))

        for m in range(0,len(bin_data),8):
            data = data + str(chr(int(self.bin2dec(self,self.XOR(self,bin_data[m:m+8],str(key))))))
            
        return data