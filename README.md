# Sistema Interativo de Análise de Dados Comerciais em SQLite

## Visão Geral
Projeto prático avaliativo para a disciplina de Banco de Dados 1 (Sistemas de Informação, UFAL).
Sistema em Python que permite consultar, analisar e visualizar informações comerciais (vendas, faturamento, clientes e pedidos) armazenadas em um banco de dados SQLite.

## Objetivos
* Implementar funcionalidades de CRUD e consultas avançadas (JOIN, GROUP BY, agregações).
* Fornecer interface interativa em linha de comando para relatórios de vendas, faturamento, clientes e pedidos.
* Estruturar o código em camadas (models, controllers, views, utils) seguindo boas práticas de organização.

## Tecnologias
* Python 3.13
* SQLite 3
* Biblioteca padrão `sqlite3`
* PyInstaller (opcional, para gerar executável)

## Estrutura do Projeto
```
├── src/                         # Código-fonte organizado por camadas
│   ├── controllers/             # Lógica de negócio e consultas
│   ├── models/                  # Definição das tabelas e mapeamento
│   ├── views/                   # Interface de linha de comando
│   └── utils/                   # Funções utilitárias
├── assets/                      # Arquivos estáticos (imagens, etc.)
├── dist/                        # Build gerado (PyInstaller)
├── Main.py                      # Ponto de entrada da aplicação
├── Projeto_Marianne_SQLITE.db   # Banco de dados de exemplo
├── requirements.txt             # Dependências do projeto
├── .gitignore                   # Arquivos e pastas ignorados pelo Git
└── README.md                    # Este arquivo
```

## Requisitos
Instale as dependências:
   ```pip install -r requirements.txt```

## Estrutura do Banco de Dados
O arquivo `Projeto_Marianne_SQLITE.db` inclui tabelas relacionadas de acordo com o tema comercial:
* `clientes`
* `produtos`
* `pedidos`
* `itens_pedido`
* `faturamento`

## Consultas Principais
* Total de vendas por período
* Faturamento mensal
* Clientes mais ativos
* Produtos mais vendidos

---
