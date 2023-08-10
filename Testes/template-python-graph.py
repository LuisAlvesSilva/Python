# Carrega o dataset
import pandas as pd
dataset = pd.read_csv('Usuarios.csv')

# Cria o Gráfico
import matplotlib.pyplot as plt
import seaborn as sns
sns.violinplot(x = 'salario', data = dataset)
plt.show()