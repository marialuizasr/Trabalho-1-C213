import numpy as np
import control as cnt
import matplotlib.pyplot as plt

# definindo as variáveis da função de transferencia
k=2
tau=4.995
Theta = 1.975

# parâmetros do controlador kp+kp/(Ti*s)+kp*Td*s
kp=1.082
ti=4.932
td=0.824

# construindo a função de transferência da planta
num = np. array ([k])
den = np. array ([tau , 1])
H = cnt.tf(num , den)
n_pade = 20
( num_pade , den_pade ) = cnt.pade ( Theta , n_pade )
H_pade = cnt.tf( num_pade , den_pade )
Hs = cnt.series (H , H_pade)

# Controlador proporcional
numkp = np. array ([kp])
denkp = np. array ([1])
#integral
numki = np. array ([kp])
denki = np. array ([Ti,0])
#derivativo
numkd = np. array ([kp*Td,0])
denkd = np. array ([1])
#Construindo o controlador PID
Hkp = cnt.tf(numkp , denkp)
Hki=cnt.tf(numki , denki)
Hkd=cnt.tf(numkd , denkd)
Hctrl1 = cnt.parallel (Hkp , Hki)
Hctrl = cnt.parallel (Hctrl1 , Hkd)
Hdel = cnt.series (Hs , Hctrl)
#Fazendo a realimentação
Hcl = cnt.feedback(Hdel, 1)

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