import matplotlib.pyplot as plt
import pandas as pd

# Analise qualidativa 
frutas = [
    "Maça", "Banana","Maça",
    "Laranja","Banana","Banana",
    "Maça","Uva","Laranja",
]

serie = pd.Series(frutas)
frequencia = serie.value_counts ()
print(frequencia)

#criando grafico de barras
frequencia.plot(kind="bar")

plt.title("Frutas preferidas dos alunos")
plt.xlabel("frutas")
plt.ylabel("Frequencia")

plt.show()
plt.savefig("aula06-qualitativo")