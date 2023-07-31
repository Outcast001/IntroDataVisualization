""" 
Notas da primeira à terceira etapa - Análise - Curso Técnico em informática (TI)
IFNMG Campus Pirapora
"""
# - Atualizado ás 16:51. 30 de julho de 2023

## IMPORTS
import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns
import pygal
print("Setup Complete")

# Passo 1:  Importando base de dados
file_path = "Datasets\grade_notas.csv"
tabela_dados = pd.read_csv(file_path)
    
# Passo 2:  Visualizando informações gerais da fonte de dados
print(tabela_dados.head())

# Passo 3:  Tratamento de dados

""" 
Somando cada uma das notas da primeira à terceira etapa do curso
(n1, n2 e n3 - por disciplina).
"""

notas = list(zip(tabela_dados.n1, tabela_dados.n2))
Nota_final = [float(sum(num)) for num in notas] # list comprehension

disciplin_notas = pd.DataFrame({
    'Disciplina':tabela_dados.Disciplina,
        'modulo':tabela_dados['Módulo'],
            'n1': tabela_dados.n1, 
                'n2': tabela_dados.n2,
                    'Total':Nota_final})

# Passo 4:  Análise inicial
carga_horaria = sum(tabela_dados.CH) # CH: Carga horária total (até o 3° módulo)
frequencia = sum(tabela_dados['Freq.']) # Quantas horas de aula o aluno tem no curso

nota_mod1 = disciplin_notas[(disciplin_notas['modulo'] == 1)]
nota_mod2 = disciplin_notas[(disciplin_notas['modulo'] == 2)]
nota_mod3 = disciplin_notas[(disciplin_notas['modulo'] == 3)]

"""  
Calcula a variação e subtrai por cem (100), obtendo assim o
percentual de horas que o aluno tem, no curso.
"""
freq_percent = (100 - (((carga_horaria - frequencia) / frequencia)*100 ))

media_modulo_1 = nota_mod1.Total.mean()
media_modulo_2 = nota_mod2.Total.mean()
media_modulo_3 = nota_mod3.Total.mean()
media_global = disciplin_notas.Total.mean()

""" Ao longo do primeiro ao terceiro módulo... """
print('\nO aluno(a) tem {} horas de curso, o que representa {}% '.format(frequencia, round(freq_percent,2)),end='\b')
print(' de um total de {} horas\n'.format(carga_horaria))

print("Média das notas do 1° módulo: ", round(media_modulo_1,2), 'de 100pts')
print("Média das notas do 2° módulo: ", round(media_modulo_2,2), 'de 100pts')
print("Média das notas do 3° módulo: ", round(media_modulo_3,2), 'de 100pts')
print("Média global das notas: ", round(media_global,2), 'de 100 pontos')

"""
As informações sobre as médias das notas acima podem ser encontradas
de uma forma mais simples, utilizando o método 'describe()',
abaixo:
"""
print(disciplin_notas.describe())

#5  Análise completa (Criar e exibir gráfico)

## Visualizando resultados:
### - Criando Histograma/Gráfico de barras

""" Gráfico de barras interativo da biblioteca 'pygal' """
# histograma = pygal.Bar()

# histograma._title = ["Notas das disciplinas do primeiro ao terceiro módulo do Curso de TI."]
# histograma.x_labels = disciplin_notas.Disciplina
# histograma._x_title = "Resultado"
# histograma._y_title = "Frequência dos resultados"

### - Exibindo e Salvando gráfico.

# histograma.add("Notas", disciplin_notas['Total'])

""" Faz o download do gráfico """
# histograma.render_to_file("gráfico-notas-curso-TI.svg")

""" Gráficos da biblioteca 'Seaborn' - Gráfio de barras"""

# Não puderam ser plotados no meu editor de código.
# Gráficos plotados no Google Colab.

plt.figure(figsize=(10,6))
plt.title("Notas das disciplinas do primeiro e segundo módulo do Curso de TI.")
plt.xlabel("Disciplinas")
plt.ylabel("Notas")
plt.xticks(rotation=50, ha='right')
sns.set_style('whitegrid')
sns.barplot(data=disciplin_notas, x="Disciplina", y="Total", hue="modulo")

""" Mapa de calor (Heatmap) - Seaborn """
data = disciplin_notas.drop(columns=['Disciplina', "modulo"]) # 
plt.figure(figsize=(10,7))
sns.heatmap(data=data, yticklabels=disciplin_notas['Disciplina'], annot=True)

#Final - Conclusões
