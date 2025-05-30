﻿# Analise Comercial SQLite

## Visão Geral
Este projeto prático avaliativo da disciplina de Banco de Dados 1 (Sistemas de Informação, UFAL) consiste em um sistema em Python que permite consultar, analisar e visualizar informações comerciais (vendas, faturamento, clientes e pedidos) armazenadas em um banco de dados SQLite.

## Objetivos
* Implementar funcionalidades de CRUD e consultas avançadas (JOIN, GROUP BY, agregações).
* Fornecer interface interativa em linha de comando e GUI básica (Tkinter) para geração de relatórios.
* Organizar o código em camadas (models, controllers, views, utils) seguindo boas práticas.

## Requirements
Ative o ambiente virtual e instale dependências:
   python -m venv .venv
   source .venv/bin/activate  # Linux/macOS
   .\.venv\Scripts\activate   # Windows
   pip install -r requirements.txt

### Dependências
* Python 3.13
* SQLite 3
* pandas
* Tkinter
* PyInstaller (para empacotamento em executável)


## Estrutura do Repositório
```
banco_de_dados/
├── .venv/                        # Ambiente virtual Python
├── assets/                       # Recursos visuais (imagens, ícones) para GUI
├── build.spec                    # Especificação do PyInstaller
├── dist/                         # Output do PyInstaller (executável + banco)
├── src/                          # Código-fonte em Python
│   ├── Main.py                   # Script principal (conexão, consultas, Tkinter, menu)
│   ├── consulta_direta.py        # Versão em terminal para executar consultas via pandas
│   └── debug.db                  # Banco de testes
├── Projeto_Marianne_SQLITE.db    # Banco principal com tabelas: Cliente, Produto, Pedido, Item_Pedido, Representante
├── requirements.txt              # Dependências do projeto
├── .gitignore                    # Arquivos/ pastas ignorados pelo Git
└── README.md                     # Documentação deste projeto
```

## Uso
* **GUI (Tkinter):** execute `python src/Main.py` para abrir janelas de diálogo e navegar pelo menu gráfico.
* **Terminal:** execute `python src/consulta_direta.py` para operar via linha de comando.

## Estrutura do Banco de Dados
O arquivo `Projeto_Marianne_SQLITE.db` contém as tabelas relacionadas:
* `Cliente`
* `Produto`
* `Pedido`
* `Item_Pedido`
* `Representante`

## Consultas Principais
* Total de vendas por representante e período
* Faturamento agregado (mensal/anual)
* Listagem de itens de um pedido específico
* Clientes e produtos mais ativos/vendidos

---
