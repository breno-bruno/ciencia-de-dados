import pandas as pd

# criação do dataframe

df = pd.DataFrame({
#cria uma coluna com definição de valores
"idade": [20, 22, 20, 23, 24]
})

print(df['idade'].describe())

print('media: '+str(df['idade'].mean()))
print('mediana: '+str(df['idade'].median()))
print('moda: '+str(df['idade'].mode().iloc[0]))