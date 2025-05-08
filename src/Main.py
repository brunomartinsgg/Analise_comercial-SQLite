import sqlite3
import os
import pandas as pd
from pathlib import Path
from PIL import Imagepip
import locale
import tkinter as tk
from tkinter import simpledialog
import sys

BASE_DIR = Path(__file__).parent
ASSETS_DIR = BASE_DIR / "assets"
IMAGES_DIR = ASSETS_DIR / "images"
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def get_resource_path(relative_path):
    """Resolve caminhos para recursos incluídos no executável"""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def menu():
    """Exibe o menu de opções"""
    print("=" * 60)
    print("             CONSULTA DIRETA AO BANCO DE DADOS".center(60))
    print("=" * 60)
    print("1. Vendas por representante")
    print("2. Faturamento por produto")
    print("3. Clientes que mais compraram")
    print("4. Pedidos com cliente e representante")
    print("5. Itens de um pedido específico")
    print("6. Faturamento total do banco")
    print("7. Listar todas as tabelas e estrutura")
    print("0. Sair")
    print("=" * 60)

def obter_entrada():
    """Exibe uma janela para capturar a entrada do usuário"""
    root = tk.Tk()
    root.withdraw()
    usuario_input = simpledialog.askstring("Entrada", "Escolha uma opção:")
    return usuario_input

def relatorio_vendas_representantes():
    """Gera relatório de vendas por representante"""
    print("Relatório de vendas por representante gerado...")
    pass

def relatorio_faturamento_produto():
    """Gera relatório de faturamento por produto"""
    print("Relatório de faturamento por produto gerado...")
    pass

def clientes_mais_compraram():
    """Exibe os clientes que mais compraram"""
    print("Clientes que mais compraram...")
    pass

def pedidos_cliente_representante():
    """Exibe pedidos com cliente e representante"""
    print("Pedidos com cliente e representante...")
    pass

def itens_pedido():
    """Exibe itens de um pedido específico"""
    print("Itens do pedido específico...")
    pass

def faturamento_total():
    """Exibe faturamento total do banco"""
    print("Faturamento total do banco...")
    pass

def listar_tabelas():
    """Exibe todas as tabelas e estrutura"""
    print("Listando tabelas...")
    pass

def main():
    """Função principal do programa"""
    while True:
        menu()
        opcao = obter_entrada()  # Usa o tkinter para pegar a entrada do usuário
        if opcao == '1':
            relatorio_vendas_representantes()
        elif opcao == '2':
            relatorio_faturamento_produto()
        elif opcao == '3':
            clientes_mais_compraram()
        elif opcao == '4':
            pedidos_cliente_representante()
        elif opcao == '5':
            itens_pedido()
        elif opcao == '6':
            faturamento_total()
        elif opcao == '7':  
            listar_tabelas()
        elif opcao == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
