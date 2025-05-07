import sqlite3
import pandas as pd
from tkinter import simpledialog, messagebox, Tk
import os


DB_PATH = os.path.join(os.path.dirname(__file__), 'Projeto_Marianne_SQLITE.db')

def exibir_dataframe(df, titulo):
    if df.empty:
        messagebox.showinfo(titulo, "Nenhum dado encontrado.")
    else:
        # Formatação para valores monetários em Real
        df = df.applymap(lambda x: f"R${x:,.2f}" if isinstance(x, (int, float)) else x)
        resultado = df.to_string(index=False)
        messagebox.showinfo(titulo, resultado)

def relatorio_vendas_representantes():
    con = sqlite3.connect(DB_PATH)
    query = '''
    SELECT r.nome AS representante, SUM(ip.quantidade * ip.preco_unitario) AS total_vendas
        FROM Representante r
        JOIN Pedido p ON r.id_representante = p.id_representante
        JOIN Item_Pedido ip ON p.id_pedido = ip.id_pedido
        GROUP BY r.nome
        ORDER BY total_vendas DESC
;
    '''
    df = pd.read_sql_query(query, con)
    con.close()
    exibir_dataframe(df, "Vendas por Representante")

def relatorio_faturamento_produto():
    con = sqlite3.connect(DB_PATH)
    query = '''
    SELECT pr.nome AS produto, SUM(ip.quantidade * ip.preco_unitario) AS faturamento
        FROM Produto pr
        JOIN Item_Pedido ip ON pr.id_produto = ip.id_produto
        GROUP BY pr.nome
        ORDER BY faturamento DESC;
    '''
    df = pd.read_sql_query(query, con)
    con.close()
    exibir_dataframe(df, "Faturamento por Produto")

def clientes_mais_compraram():
    con = sqlite3.connect(DB_PATH)
    query = '''
     SELECT c.nome AS cliente, SUM(ip.quantidade * ip.preco_unitario) AS total_gasto
        FROM Cliente c
        JOIN Pedido p ON c.id_cliente = p.id_cliente
        JOIN Item_Pedido ip ON p.id_pedido = ip.id_pedido
        GROUP BY c.nome
        ORDER BY total_gasto DESC;
    '''
    df = pd.read_sql_query(query, con)
    con.close()
    exibir_dataframe(df, "Clientes que mais Compraram")

def pedidos_cliente_representante():
    con = sqlite3.connect(DB_PATH)
    query = '''
    SELECT p.id_pedido, p.data_pedido, c.nome AS cliente, r.nome AS representante
        FROM Pedido p
        JOIN Cliente c ON p.id_cliente = c.id_cliente
        JOIN Representante r ON p.id_representante = r.id_representante;
    '''
    df = pd.read_sql_query(query, con)
    con.close()
    exibir_dataframe(df, "Pedidos com Cliente e Representante")

def itens_pedido():
    root = Tk()
    root.withdraw()
    pedido_id = simpledialog.askinteger("Itens do Pedido", "Digite o ID do Pedido:")
    root.destroy()

    if pedido_id is None:
        return

    con = sqlite3.connect(DB_PATH)
    query = '''
    SELECT ip.id_item, pr.nome AS produto, ip.quantidade, ip.preco_unitario
        FROM Item_Pedido ip
        JOIN Produto pr ON ip.id_produto = pr.id_produto
        WHERE ip.id_pedido = ?;
    '''
    df = pd.read_sql_query(query, con, params=(pedido_id,))
    con.close()
    exibir_dataframe(df, f"Itens do Pedido {pedido_id}")

def faturamento_total():
    con = sqlite3.connect(DB_PATH)
    query = '''
    SELECT SUM(ip.quantidade * ip.preco_unitario) AS faturamento_total
        FROM Item_Pedido ip;
    '''
    df = pd.read_sql_query(query, con)
    con.close()
    exibir_dataframe(df, "Faturamento Total")

def listar_tabelas():
    con = sqlite3.connect(DB_PATH)
    cursor = con.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tabelas = [linha[0] for linha in cursor.fetchall()]
    con.close()
    messagebox.showinfo("Tabelas no Banco", "\n".join(tabelas))

def menu():
    opcoes = (
    "1. Vendas por representante\n"
    "2. Faturamento por produto\n"
    "3. Clientes que mais compraram\n"
    "4. Pedidos com cliente e representante\n"
    "5. Itens de um pedido específico\n"
    "6. Faturamento total do banco\n"
    "7. Listar todas as tabelas\n"
    "0. Sair"
    )
    root = Tk()
    root.withdraw()
    escolha = simpledialog.askstring("Menu", f"Escolha uma opção:\n\n{opcoes}")
    root.destroy()
    return escolha

def main():
    while True:
        opcao = menu()

        if opcao is None or opcao == '0':
            messagebox.showinfo("Saindo", "Encerrando o programa...")
            break

        elif opcao == '1':
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
        else:
            messagebox.showerror("Erro", "Opção inválida!")

if __name__ == '__main__':
    main()
