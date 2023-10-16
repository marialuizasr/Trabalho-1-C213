import numpy as np
import control as cnt
import matplotlib.pyplot as plt
from scipy.io import loadmat

# exercício 4

# importando os dados
mat = loadmat('TransferFunction1.mat')
saida = mat.get('saida')
degrau = mat.get('degrau')
t1 = mat.get('t')

# definindo as variáveis da função de transferência
k = 2
tau = 4.995
theta = 1.975

# construindo a função de transferência da planta
num = np.array([k])
den = np.array([tau, 1])
H = cnt.tf(num, den)
n_pade = 20
(num_pade, den_pade) = cnt.pade(theta, n_pade)
H_pade = cnt.tf(num_pade, den_pade)
Hs = cnt.series(H, H_pade)

# plotando o gráfico de comparação da malha aberta e fechada
t = np.linspace(0, 40, 100)
(t, y) = cnt.step_response(Hs, t)
plt.plot(t, y, label='Malha Aberta')
Hmf = cnt.feedback(Hs, 1)
(t, y1) = cnt.step_response(Hmf, t)
plt.plot(t, y1, label='Malha Fechada')
plot2 = plt.plot(t1.T, degrau, label='Degrau de entrada')
plt.xlabel(' t [ s ] ')
plt.ylabel('Amplitude')
plt.legend(loc='upper left')
plt.title('Malha Aberta x Malha Fechada')

# exibindo o gráfico
plt.grid()
plt.show()

# calculando o erro em malha aberta e fechada
print('')
print('SetPoint = ', degrau[1])
print('Erro da Malha Aberta = ', abs(degrau[1] - max(saida)))
print('Erro da Malha Fechada = ', degrau[1] - 0.66)


