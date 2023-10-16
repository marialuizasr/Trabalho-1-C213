import matplotlib.pyplot as plt
import numpy as np
import control as cnt

# ajuste método CC

# definindo as variáveis da função de transferência
k = 2
tau = 4.995
theta = 1.975

# ajustando parâmetro do controlador PID - CC
ke = 1.5
ti = 4.2
td = 0.67

# construindo a função de transferência da planta
num = np.array([k])
den = np.array([tau, 1])
H_cc = cnt.tf(num, den)
n_pade = 20
(num_pade, den_pade) = cnt.pade( theta, n_pade)
H_pade = cnt.tf(num_pade, den_pade)
Hs = cnt.series(H_cc, H_pade)

# controlador proporcional
numke = np.array([ke])
denke = np.array([1])

# controlador integrativo
numki = np.array([ke])
denki = np.array([ti, 0])

# controlador derivativo
numkd = np.array([ke*td, 0])
denkd = np.array([1])

# construindo o controlador PID
Hke = cnt.tf(numke, denke)
Hki = cnt.tf(numki, denki)
Hkd = cnt.tf(numkd, denkd)
Hctrl1 = cnt.parallel(Hke, Hki)
Hctrl = cnt.parallel(Hctrl1, Hkd)
Hdel = cnt.series(Hs, Hctrl)

# fazendo a realimentação
Hcl = cnt.feedback(Hdel, 1)

# plotando o gráfico
t = np.linspace(0, 40, 100)
(t, y) = cnt.step_response(1*Hcl, t)
plt.plot(t, y)
plt.xlabel(' t [ s ]')
plt.ylabel('Amplitude')
plt.legend(loc='upper right')
plt.title('Controle PID - CC')

plt.grid()
plt.show()