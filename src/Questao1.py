import numpy as np
import statsmodels.api as sm
import pandas as pd
import matplotlib.pyplot as plt
# Chamando bibliotecas para ajudar na confecção de um gráfico de exemplo do que é uma OLS
# numpy realiza cálculos numéricos , "as np" aqui estamos dando um apelido para a biblioteca. O mesmo se repetirá nas demais 
# statsmodels é uma biblio para análise estatística, .api para interagir com as ferramentas
# pandas = biblio para manipulaçao de dados
# matplotlib.pyplot = bilioteca que também irá interagir com pandas e numpy, tbm irá realizar o gráfico



np.random.seed(42)  #aqui definimos uma seed para criar números aleatórios
num_estudantes = 200
horas_estudadas = np.random.uniform(0, 10, num_estudantes) #gera nmrs aleatórios de horas de estudos de 0 a 10
intercept = 50  # nota tirada sem estudar
slope = 10      # Aumento da nota por hora estudada
noise = np.random.normal(0, 5, num_estudantes)  # Ruído aleatório = simula fatores que influenciam, a fim de tornar mais realista
notas = intercept + slope * horas_estudadas + noise 
# relação linear entre horas estudadas e notas, com adição do ruido aleatorio


data = pd.DataFrame({'horas': horas_estudadas, 'notas': notas})

X = data['horas']  # Variável independente (horas estudadas)
y = data['notas']  # Variável dependente (notas)
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()

#configurando o nosso gráfico
plt.scatter(X['horas'], y, label='Dados')
plt.plot(X['horas'], model.fittedvalues, color='red', label='Reta de Regressão')
plt.xlabel('Horas estudadas')
plt.ylabel('Notas Obtidas')
plt.title('Exemplo de OLS: horas estudadas por alunos vs notas obtidas')
plt.legend()
plt.savefig("docs/gráficoquestao1.png")
plt.show()




#OLS é uma técnica de regressão linear para encontrar relação entre variáveis numéricas através de uma reta.