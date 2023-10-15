import matplotlib.pyplot as plt
import numpy as np
import control as cnt

# exercício 5 - método CC

# definindo as variáveis da função de transferência
k = 2
tau = 4.995
theta = 1.975

# controlador PID - CC
ke = (1/k)*(tau/theta)*((4/3+(1/4*(theta/tau))))
ti = theta*((32+6*(theta/tau))/(13+(8*(theta/tau))))
td = theta*((4/(11+(2*(theta/tau)))))

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
t = np.linspace(50, 90, 100)
(t, y) = cnt.step_response(1*Hcl, t)
plt.plot(t, y)
plt.xlabel('Tempo[s] ')
plt.ylabel('Amplitude')
plt.legend(loc='upper right')
plt.title('Controle PID - CC')

# exibindo o gráfico
plt.grid()
plt.show()
