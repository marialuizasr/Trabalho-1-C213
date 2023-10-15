import numpy as np
import control as cnt
import matplotlib.pyplot as plt
from scipy.io import loadmat

# exercício 4

# importando os dados
mat = loadmat('TransferFunction1.mat')
saida = mat.get('saida')
degrau = mat.get('degrau')

# definindo as variáveis da função de transferência
k = 2
tau = 4.995
theta = 1.975

# construindo a função de transferência da planta
num = np. array([k])
den = np. array([tau, 1])
H = cnt.tf(num, den)
n_pade = 20
(num_pade, den_pade) = cnt.pade(theta, n_pade)
H_pade = cnt.tf(num_pade, den_pade)
Hs = cnt.series(H, H_pade)

# plotando o sinal da malha aberta e malha fechada
time = np.linspace(0, 40, 100)
(t, y) = cnt.step_response(1 * Hs, time)
plt.plot(time, y, label='Erro (malha aberta)')
Hmf = cnt.feedback(Hs, 1)
(t, y2) = cnt.step_response(1 * Hmf, time)
plt.plot(time, y2, label='Erro (malha fechada)')

# plotando o gráfico para comparação dos sinais
plot2 = plt.plot(time, degrau, label='Degrau de entrada')

plt.xlabel(' t [ s ] ')
plt.ylabel('Amplitude')
plt.title('Comparação de erro entre malha aberta e fechada')
plt.legend(loc="upper left")

# exibindo o gráfico
plt.grid()
plt.show()

# calculando o erro em malha aberta e fechada
erro_malhaaberta = 1 - max(saida) # erro = |1-2| = 1
erro_malhafechada = 1 - 1 # erro = 0
print(f'Erro da malha aberta: {erro_malhaaberta[0]}')
print(f'Erro da malha fechada: {erro_malhafechada}')