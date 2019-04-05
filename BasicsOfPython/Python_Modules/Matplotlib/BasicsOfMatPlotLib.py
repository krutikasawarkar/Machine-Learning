
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

x = np.linspace(0,10,50)
sinus = np.sin(x)

#plt.plot(x, sinus, "o")
#plt.show()

##Multiplot
cosinus = np.cos(x)
#plt.plot(x, sinus, "-b", x , sinus, "ob" , x , cosinus , "-r" , x,  cosinus, "or")
#plt.xlabel('x')
#plt.ylabel('y')
#plt.title('My first plot')
#plt.show()

##Adding styles
#plt.plot(x, sinus, label='sinus', color='blue', linestyle='--',linewidth=4)
#plt.plot(x, cosinus, label='cosinus', color='red', linestyle='-',linewidth=4)
#plt.legend()
#plt.show()

