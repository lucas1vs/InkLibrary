#  Sistema de Gerenciamento de biblioteca

 Este projeto é um sistema simples de gerenciamento de biblioteca desenvolvido em Python. Ele funciona via terminal e permite cadastrar, editar e controlar livros disponíveis, simulando um sistema real de controle de acervo.
 
# Objetivo

 O objetivo deste projeto é aplicar conceitos fundamentais de programação em Python, como estruturas de dados, funções e controle de fluxo, criando um sistema capaz de gerenciar livros e suas quantidades.

# Funcionalidades

* Cadastrar livros (título, autor e quantidade)
* Listar todos os livros cadastrados
* Buscar livro pelo título
* Editar informações do livro
* Remover livros do sistema
* Realizar empréstimo de livros (controle de quantidade)
* Dashboard com resumo do sistema

# Conceitos Utilizados

* Listas e dicionários
* Funções para organização do código
* Estruturas condicionais (if/else)
* Laços de repetição (while, for)
* Tratamento de exceções (try/except)
* Manipulação de strings com .lower() e .strip()

# Como Executar

* Certifique-se de ter o Python instalado
* Salve o código em um arquivo .py
* Execute no terminal:
* python nome_do_arquivo.py
* Utilize o menu interativo para navegar pelas opções

# Estrutura dos Dados

Os livros são armazenados em uma lista de dicionários, no seguinte formato:

{
  "titulo": "Dom Casmurro",
  "autor": "Machado de Assis",
  "quantidade": 5
}

# Fluxo do Programa

* O sistema inicia exibindo um menu de opções
* O usuário escolhe uma ação
* O sistema executa a função correspondente
* Os dados são processados e exibidos
* O menu é exibido novamente até o usuário sair

# Observações
* Os dados são armazenados apenas durante a execução do programa
* Não há uso de banco de dados
* O sistema é totalmente baseado em terminal
# Possíveis Melhorias

* Salvar dados em arquivos (JSON ou CSV)
* Criar interface gráfica
* Implementar sistema de devolução de livros
* Adicionar cadastro de usuários

# Conclusão

* Durante o desenvolvimento deste projeto, foi possível compreender melhor o uso de listas, dicionários e funções em Python. Também foi possível praticar a organização do código e a construção de um sistema funcional, enfrentando desafios relacionados à lógica e tratamento de erros.
