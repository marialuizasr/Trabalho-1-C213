import matplotlib.pyplot as plt
from scipy.io import loadmat

# exercício 1

# importando os dados
mat = loadmat('TransferFunction1.mat')

# extraindo as variáveis
degrau = mat.get('degrau')
saida = mat.get('saida')
t = mat.get('t')

# plotando os gráficos
plt.plot(t.T,saida, label='Saída')
plt.plot(t.T,degrau,label='Degrau de entrada')

plt.xlabel (' t [ s ] ')
plt.ylabel('Amplitude')
plt.title('Função de transferência')
plt.legend(loc="upper left")

plt.grid()
plt.show()


# exercício 2

# valores obtidos pelo método de smith
y_max = max(saida) # valor máximo do sinal
d_Y = y_max - min(saida) # delta do sinal
d_u = 1 # valor do degrau

# valor do sinal em 28,3% para determinar t1
y_t1 = y_max * 0.283
t1 = 3.64

# valor do sinal em 63,2% para determinar t2
y_t2 = y_max * 0.632
t2 = 6.97

# encontrando os valores de k, Ɵ e τ
k = d_Y/d_u # k=2
tau = 1.5 * (t2 - t1) # τ=4.995
theta = t2 - tau # Ɵ=1.975

print(k, tau, theta)

