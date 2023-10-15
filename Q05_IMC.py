import matplotlib.pyplot as plt
import numpy as np
import control as cnt

# exercício 5 - método IMC

# definindo as variáveis da função de transferência
k = 2
tau = 4.995
theta = 1.975

# controlador PID - IMC
lambida = 1.6 # lambda > 1.58
kp = ((2 * tau + theta) / (k * (2 * lambida + theta)))
ti = tau + (theta / 2)
td = (tau * theta) / (2 * tau + theta)

# construindo a função de transferência da planta
num = np.array([k])
den = np.array([tau , 1])
H = cnt.tf(num , den)
n_pade = 20
( num_pade , den_pade ) = cnt.pade ( theta , n_pade )
H_pade = cnt.tf( num_pade , den_pade )
Hs = cnt.series (H , H_pade)

# controlador proporcional
numkp = np.array([kp])
denkp = np.array([1])

# controlador integrativo
numki = np.array([kp])
denki = np.array([ti,0])

# controlador derivativo
numkd = np.array([kp*td,0])
denkd = np.array([1])

# construindo o controlador PID
Hkp = cnt.tf(numkp , denkp)
Hki = cnt.tf(numki , denki)
Hkd = cnt.tf(numkd , denkd)
Hctrl1 = cnt.parallel (Hkp , Hki)
Hctrl = cnt.parallel (Hctrl1 , Hkd)
Hdel = cnt.series (Hs , Hctrl)

# fazendo a realimentação
Hcl = cnt.feedback(Hdel, 1)

# plotando o gráfico
t = np.linspace(0 , 40 , 100)
( t , y ) = cnt.step_response (1 * Hcl, t )
plt.plot (t , y)
plt.xlabel (' t [ s ]')
plt.ylabel('Amplitude')
plt.title('Controle PID - IMC')

# exibindo o gráfico
plt.grid()
plt.show()

