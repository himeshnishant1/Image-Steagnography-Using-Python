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
