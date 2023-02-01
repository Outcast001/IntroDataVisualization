"""
Análise relativa dos projetos com maior número de estrelas no Github, por linguagem de programação
- Projetos analisados por linguagem: Python e JavaScript

OBS: Múltiplos gráficos foram feitos devido à atualização constante
da API - os resultados das chamadas de api do github estão incompletos

Fontes: 
    - JavaScript: https://api.github.com/search/repositories?q=language:javascript&sort=stars
    - Python: https://api.github.com/search/repositories?q=language:python&sort=stars
"""

# Imports
import requests as rq
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
import pygal

# Faz uma chamada de API e armazena a resposta numa variável
url = 'https://api.github.com/search/repositories?q=language:javascript&sort=stars'
r = rq.get(url)

print("Status code: ", r.status_code)# Se 200 -> Ok!

# Armazena a resposta da API numa variável
respost_dict = r.json()

# Processa o resultado
print('\n',respost_dict.keys())

""" 
O valor em 'total_count' obtido através da chamada de API do github 
é atualizado a cada poucos segundos, o que altera os dados de entrada
sempre que o script é executado
"""

print("\nTotal repositories: ",respost_dict['total_count'], "Incomplete results?", respost_dict['incomplete_results'])

# Explora informações sobre os repositórios
repo_dicts = respost_dict['items']
print("Repositóries returned: ", len((repo_dicts)))

# Dados presentes nos gráfico interativo:
## - Nome do repositório ('name');e
## - Quantidade de estrelas ('stargazers_count')

names, stars = [], []
""" 
Armazena dados do dicionário de repositórios
nas variáveis 'name' e 'stars'
"""
for repo_dict in repo_dicts:
  names.append(repo_dict['name'])
  stars.append(repo_dict['stargazers_count'])

# Criando visualização com a biblioteca pygal

#style = LS('#333366',base_style=LCS)
style = LS('#EA4335',base_style=LCS)

grafico = pygal.Bar(style=style, x_label_rotation=45, show_legend=False)
grafico.title = "Projetos javascript com maior número de estrelas no Github"
# grafico.title = "Projetos python com maior número de estrelas no Github"
grafico.x_title = "Projetos"
grafico.y_title = "Número de estrelas"
grafico.x_labels = names

grafico.add('',stars)

# Faz o download dos gráfico interativos
# grafico.render_to_file('Most-Starred-Python-Projects-on-Github_2023-01-31.svg') # 'Most-Starred-Python-Projects-on-Github_2023-01-31 - V1.svg')
grafico.render_to_file('Imagens - plots/Most-Starred-JavaScript-Projects-on-Github_2023-02-01.svg') # 'Most-Starred-Python-Projects-on-Github_2023-01-31 - V1.svg')

"""
Observação 2: Algumas linhas foram comentadas, pois não podem ser executados ao mesmo tempo
- O que é possível, más requer algumas modificações no código.

Observação 3: Os gráficos e outputs obtidos devem ser diferentes, a depender de quando você executar este script.
"""