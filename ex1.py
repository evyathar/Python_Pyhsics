import numpy as np
#import matplotlib.pyplot as plt
#input
A=float(input("A:"))
B=float(input("B:"))
qn=int(input("qn:"))

# you code
##########
C = abs(A-B)
D = A+B
max_no = 5

#x = np.linspace(0, 10, 10056.4)
#y = np.sin(x + 2) * np.cos(2*x - 3)
#check
#plt.plot(x, y)
#plt.show()




##########
#output
if qn==1: 
    print(f'{C:.5g}')
elif qn==2: 
    print(f'{D:.5g}')
elif qn==3:
    print(max_no)



