""" Notas da segunda etapa - Análise """
## - Atualizado ás 18:44. 19 de Janeiro 2023

import pandas as pd
import pygal

# Passo 1:  Importar base de dados

tabela = pd.read_csv("documents\Datasets\grade_notas.csv")
    
# Passo 2:  Exibir base de dados
# Passo 3:  Tratamento de dados
##  - Corrigindo problema com espaços nas colunas da tabela
##  - Apagando linha 1 - 2° nota vazia

tabela.columns = [str(value).strip() for value in ('Id', 'Professor', 'Disciplina', 'n1', 'n2') ]# Inútil.
tabela = tabela.drop([0])

# Passo 4:  Análise inicial

""" O que mais interessa são as notas da 1° e 2° etapa """

materias = list(zip(tabela.Professor, tabela.Disciplina))
notas = list(zip(tabela.n1, tabela.n2))

""" 
Tendo decidido por analisar as notas da primeira e segunda etapa, separei ambas
as notas em duas variáveis, 'Etp1' e 'Etp2' e as transformei num 'DataFrame'
para que pudesse usar o método 'describe()'.
"""

''' List Comprehensions '''

Etp1 = [str(item[1]) for item in materias] 
Etp2 = [int(sum(num)) for num in notas]

notaPorDisciplina = pd.DataFrame(tuple(zip(Etp1,Etp2)), columns=['Disciplina','Nota'])

print(round(notaPorDisciplina.describe(),2))
print(notaPorDisciplina)

#5  Análise completa (Criar e exibir gráfico)

## Visualizar resultados:
### - Criar Gráfico

histograma = pygal.Bar()

histograma._title = "Resultado final do 2° módulo do Curso de TI."
histograma.x_labels = ['Análise S.','Dev. Web','Admin.','L. Programação','Redes']
histograma._x_title = "Resultado"
histograma._y_title = "Frequência dos resultados"

### - Exibindo e Salvando gráfico.

histograma.add("Notas", notaPorDisciplina['Nota'])
histograma.render_to_file("gráfico-notas-segundo-módulo.svg")

#Final - Conclusões

## Qual a menor nota?
## Qual a maior nota?
'''
Maior nota (Etapa 1): 50 pts;
Menor nota (Etapa 1): 30 pts;

Maior nota (Etapa 2): 44 pts;
Menor nota (Etapa 2): 15 pts;
'''

## Notas da primeira e segunda etapa: 
'''
Maior nota total: 89
Menor nota total: 60
'''
