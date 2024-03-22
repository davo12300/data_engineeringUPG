import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
import matplotlib.pyplot as plt
import seaborn as sns
# Crear un DataFrame de ejemplo (sustitúyelo con la carga de tus datos reales)
df = pd.read_excel("data_source.xlsx")

# Convertir los datos al formato esperado por mlxtend
te = TransactionEncoder()
te_ary = te.fit(df.iloc[:, 1:].astype(str).values).transform(df.iloc[:, 1:].astype(str).values)
transactions = pd.DataFrame(te_ary, columns=te.columns_)

#fc = float(input("SOPORTE MINIMO:\t"))

frequent_itemsets = apriori(transactions, min_support=0.10, use_colnames=True, max_len=3)

mapeo_redes = {1: 'Facebook', 2: 'Twitter', 3: 'Instagram', 4: 'LinkedIn', 5: 'Snapchat',6:'Pinterest',7:'TikTok',8:'Reddit'}
frequent_itemsets['itemsets'] = frequent_itemsets['itemsets'].apply(lambda x: {mapeo_redes[int(i)] for i in x})



# Filtrar el DataFrame por longitud de itemsets
df_k1 = frequent_itemsets[frequent_itemsets['itemsets'].apply(lambda x: len(x)) == 1]
df_k2 = frequent_itemsets[frequent_itemsets['itemsets'].apply(lambda x: len(x)) == 2]
df_k3 = frequent_itemsets[frequent_itemsets['itemsets'].apply(lambda x: len(x)) == 3]
df_k1['itemsets'] = df_k1['itemsets'].apply(lambda x: ', '.join(x))
df_k2['itemsets'] = df_k2['itemsets'].apply(lambda x: ', '.join(x))
df_k3['itemsets'] = df_k3['itemsets'].apply(lambda x: ', '.join(x))

print("PARA K=1 \n ", df_k1, "\n","PARA K=2 \n", df_k2, "\n","PARA K=3 \n", df_k3, "\n")



import matplotlib.pyplot as plt
import seaborn as sns

# Suponiendo que ya tienes los DataFrames df_k1, df_k2 y df_k3

def plot_bar_chart(df, k):
    plt.figure(figsize=(10, 6))
    plt.rcParams['font.family'] = 'Arial'
    ax = sns.barplot(x='itemsets', y='support', data=df, palette='mako')
    ax.set(title=f'Frecuencia de combinaciones para k={k}', xlabel='Itemsets', ylabel='Soporte')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=30, ha='right', fontsize=10)  # Ajustar tamaño del texto del eje x
    for p in ax.patches:
        height_percentage = p.get_height() * 100  # Multiplicar por 100 el valor del DataFrame para obtener el porcentaje
        ax.annotate(f'{height_percentage:.2f}%', (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='center', xytext=(0, 10), textcoords='offset points', fontsize=8)

    plt.show()

# Gráficos para k=1
plot_bar_chart(df_k1, 1)

# Gráficos para k=2
plot_bar_chart(df_k2, 2)

# Gráficos para k=3
plot_bar_chart(df_k3, 3)
