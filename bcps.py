import numpy as np
import matplotlib.pyplot as plt
x = []
for i in range(4000000):
    b = np.random.randint(2,size=(8,8))
    count = 0
    change = 0
    for j in range(8):
        for k in range(8):
            if j == 0 and k == 0:
                count = 0
                change = b[j,k]
            else:
                if change != b[j,k]:
                    count = count + 1
                    change = b[j,k]
    x.append(count/63)
                
plt.hist(x, density=True, bins=30)
plt.ylabel('Probability')
plt.xlabel('Data')
plt.show()




# Secret Message into ASCII and ASCII into Binary format
file = open('input.txt','r')
secret_message = ''
for line in file.readlines():
    secret_message = secret_message + str(line)
binary = ''
key = ''
key = input("Enter a numeric key of 4 digits.. ")
count = 0
tmp = ''
while True:
    if key.isnumeric() and (len(key) == 4):
        sum1 = 0
        for i in range(len(key)):
            sum1 = sum1+ ord(key[i])
        key = str(dec2bin(sum1))
        print("Converting Message to Binary and encrypting...")
        for pos in range(len(secret_message)):
            if ord(secret_message[pos]) <= 255:
                if count < 8:
                    binary = binary + str(XOR(dec2bin(ord(secret_message[pos])),key)) # coverting Secret code into ASCII and ASCII into Encrypted Binary.
                    count = count + 1
                else:
                    tmp = count = 0
        print("\nMessage Conversion Successfull.\n")
        #print("Binary Code = ",binary)
        break;
    else:
        print("please enter only 4 numeric digits the key")
        key = input("Enter a numeric key of 4 digits..")