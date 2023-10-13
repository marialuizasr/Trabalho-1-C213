import numpy as np
import control as cnt
import matplotlib.pyplot as plt
from scipy.io import loadmat
#considerando uma função de transferencia em malha aberta FT=k/(tau*s+1)
k=2
tau=4.995
Theta = 1.975 # atraso de propagação
#parâmetros do controlador kp+kp/(Ti*s)+kp*Td*s
kp=1.5174
Ti=3.95
Td=0.9875

print(kp)
print(Ti)
print(Td)
#escrevendo a função de transferência da planta
num = np. array ([k])
den = np. array ([tau , 1])
H = cnt.tf(num , den)
n_pade = 20
( num_pade , den_pade ) = cnt.pade ( Theta , n_pade )
H_pade = cnt.tf( num_pade , den_pade )
Hs = cnt.series (H , H_pade)


t = np . linspace (0 , 40 , 100)
(t , y ) = cnt.step_response ( Hs, t )


mat=loadmat('TransferFunction1.mat')
#print(mat)
#Variáveis
degrau = mat.get('degrau')


saida=mat.get('saida')
t1 = mat.get('t')

plt.subplot(1, 3, 1)
plt.plot(t1.T,saida, label='Saída')
plt.grid ()

plt.subplot(1, 3, 2)
plt.plot (t , y )

plt.grid ()

Hmf = cnt.feedback(Hs, 1)
t = np . linspace (0 , 40 , 100)
(t1 , y1 ) = cnt.step_response ( Hmf, t )

plt.subplot(1, 3, 3)
plt.plot(t1,y1, label='Saída')

plt.grid ()
plt.show()


# Erro malha aberta = 0 
# Erro malha fechada = 1.33