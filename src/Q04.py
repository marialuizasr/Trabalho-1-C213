import numpy as np
import control as cnt
import matplotlib.pyplot as plt
#considerando uma função de transferencia em malha aberta FT=k/(tau*s+1)
k=2
tau=4.995
Theta = 1.975 # atraso de propagação
#parâmetros do controlador kp+kp/(Ti*s)+kp*Td*s
kp=1.082
Ti=4.932
Td=0.824


#escrevendo a função de transferência da planta
num = np. array ([k])
den = np. array ([tau , 1])
H = cnt.tf(num , den)
n_pade = 20
( num_pade , den_pade ) = cnt.pade ( Theta , n_pade )
H_pade = cnt.tf( num_pade , den_pade )
Hs = cnt.series (H , H_pade)

#Fazendo a realimentação
Hcl = cnt.feedback(Hs, 1)

#Plotando em malha aberta
t = np . linspace (0 , 40 , 100)
(t , y ) = cnt.step_response ( Hs, t )
plt.subplot(1,2,1)
plt.plot (t , y )
plt.xlabel ( ' t [ s ] ')
plt.ylabel('Amplitude')
plt.title('Malha aberta')
plt.grid ()

#Plotando em malha fechada
t2 = np . linspace (0 , 40 , 100)
(t2 , y2 ) = cnt.step_response ( Hcl, t2 )
plt.subplot(1,2,2)
plt.plot (t2 , y2 )
plt.xlabel ( ' t [ s ] ')
plt.ylabel('Amplitude')
plt.title('Malha fechada')
plt.grid ()

plt.show()