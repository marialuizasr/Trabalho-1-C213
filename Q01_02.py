import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat

mat = loadmat('./TransferFunction1.mat')

degrau = mat.get('degrau')
saida = mat.get('saida')
t1 = mat.get('t')

plt.plot(t1.T, saida, label='Saída')
plt.plot(t1.T, degrau, label='degrau de entrada')
plt.xlabel(' t [ s ] ')
plt.ylabel('Amplitude')
plt.legend(loc="upper left")

plt.grid()
plt.show()
    
    
    
