import numpy as np
import control as cnt
import matplotlib.pyplot as plt
from scipy.io import loadmat

# exercício 3

# importando os dados
mat = loadmat('TransferFunction1.mat')

# simulação da função de transferência
degrau = mat.get('degrau')
saida = mat.get('saida')
t1 = mat.get('t')

# definindo as variáveis da função de transferência
k = 2
tau = 4.995
theta = 1.975

# construindo a função de transferência
num = np.array([k])
den = np.array([tau, 1])
H = cnt.tf(num, den)
n_pade = 20
(num_pade, den_pade) = cnt.pade(theta, n_pade)
H_pade = cnt.tf(num_pade, den_pade)
Hs = cnt.series(H, H_pade)

# simulação da função de transferência estimada
time, y = cnt.step_response(1*Hs, T=t1)

# plotando os gráficos
plt.plot(time, y, label='Saída estimada')
plt.plot(time, saida, label='Saída fornecida', linestyle='dashed')
plt.plot(time, degrau, label='Degrau de entrada')

plt.xlabel(' t [ s ] ')
plt.ylabel('Amplitude')
plt.legend(loc="upper left")
plt.title('Funções de transferência')

# exibindo o gráfico
plt.grid()
plt.show()
