import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import statsmodels.api as sm
import matplotlib.image as mpimg
from bcb import sgs
#nessa questão usaremos também a parte visual da biblioteca matplotlib


#aqui estamos puxando as séries da API do Banco Central (biblioteca: bcb import sgs) das taxas que foram solicitadas na questão
selic = sgs.get({'selic':432}, start = '2019-01-01',end = '2024-01-01')
pib = sgs.get({'PIB':1207}, start = '2019-01-01', end = '2024-01-01')
inflacao = sgs.get({'inflacao': 13521}, start = '2019-01-01', end = '2024-01-01')
desemprego = sgs.get({'desemprego':24369}, start = '2019-01-01', end = '2024-01-01')


#irá criar uma figura com dois subgráficos dispostos em linha única. O primeiro número irá indicar uma linha e o segundo número que haverá duas colunas
fig, axs = plt.subplots (1, 2, figsize =(15,10))

#colocando nossos dados no subgráfico, axs[0] será o primeiro gráfico e axs[1] o segundo gráfico
selic.plot(ax=axs[0], label = "Taxa Selic", color = 'blue')
inflacao.plot(ax=axs[0], label = "Inflação", color = 'red')
desemprego.plot(ax=axs[0], label = "Desemprego", color = 'orange')

axs[0].set_title("Taxa selic, Inflação e Desemprego (2019-2023)")
axs[0].set_xlabel("Data")
axs[0].set_ylabel("Valores")
axs[0].legend()

pib.plot(ax=axs[1], label="GDP", color ='green')

axs[1].set_title("GDP ((2019-2023)")
axs[1].set_xlabel("Data")
axs[1].set_ylabel("GDP Valores")
axs[1].legend()

#Vamos ler a imagem do arquivo docs/ceicdata.jpeg e armazenar em uma variável img.
img = mpimg.imread('docs/ceicdata.jpeg')

#Aqui definimos o eixo, largura e altura da imagem
ax_img = fig.add_axes([0.0, 0.0, 1.0, 0.5])
ax_img.imshow(img)
#exibe a imagem
ax_img.axis('off')

plt.tight_layout(rect=[0, 0.5, 1,1 ])
plt.savefig("docs/gráficoquestao2.png")

plt.show()


