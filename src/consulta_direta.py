import sqlite3
import pandas as pd
import os

def conectar_banco():
    try:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        caminho_db = os.path.join(base_dir, 'database.db')
        conn = sqlite3.connect(caminho_db)
        print("✅ Conexão estabelecida com sucesso!")
        return conn
    except sqlite3.Error as e:
        print(f"❌ Erro ao conectar: {e}")
        return None

def listar_tabelas(conn):
    try:
        tabelas = pd.read_sql("SELECT name FROM sqlite_master WHERE type='table'", conn)
        if tabelas.empty:
            print("⚠️ Nenhuma tabela encontrada!")
            return
        print("\n📋 Tabelas disponíveis:")
        print(tabelas.to_string(index=False))
        print("\n🔍 Estrutura das tabelas:")
        for tabela in tabelas['name']:
            print(f"\nTabela: {tabela}")
            estrutura = pd.read_sql(f"PRAGMA table_info({tabela})", conn)
            print(estrutura.to_string(index=False))
    except Exception as e:
        print(f"❌ Erro ao listar tabelas: {e}")

def consulta_vendas_por_representante(conn):
    try:
        query = """
        SELECT r.nome AS representante, SUM(ip.quantidade * ip.preco_unitario) AS total_vendas
        FROM Representante r
        JOIN Pedido p ON r.id_representante = p.id_representante
        JOIN Item_Pedido ip ON p.id_pedido = ip.id_pedido
        GROUP BY r.nome
        ORDER BY total_vendas DESC
        """
        df = pd.read_sql(query, conn)
        df['total_vendas'] = df['total_vendas'].apply(lambda x: f"R${x:,.2f}".replace(',', 'v').replace('.', ',').replace('v', '.'))
        print("\n📊 Vendas por Representante:")
        print(df.to_string(index=False))
    except Exception as e:
        print(f"❌ Erro na consulta: {e}")

def consulta_vendas_por_produto(conn):
    try:
        query = """
        SELECT pr.nome AS produto, SUM(ip.quantidade * ip.preco_unitario) AS faturamento
        FROM Produto pr
        JOIN Item_Pedido ip ON pr.id_produto = ip.id_produto
        GROUP BY pr.nome
        ORDER BY faturamento DESC
        """
        df = pd.read_sql(query, conn)
        df['faturamento'] = df['faturamento'].apply(lambda x: f"R${x:,.2f}".replace(',', 'v').replace('.', ',').replace('v', '.'))
        print("\n📦 Faturamento por Produto: ")
        print(df.to_string(index=False))
    except Exception as e:
        print(f"❌ Erro na consulta: {e}")

def clientes_que_mais_compraram(conn):
    try:
        query = """
        SELECT c.nome AS cliente, SUM(ip.quantidade * ip.preco_unitario) AS total_gasto
        FROM Cliente c
        JOIN Pedido p ON c.id_cliente = p.id_cliente
        JOIN Item_Pedido ip ON p.id_pedido = ip.id_pedido
        GROUP BY c.nome
        ORDER BY total_gasto DESC
        """
        df = pd.read_sql(query, conn)
        df['total_gasto'] = df['total_gasto'].apply(lambda x: f"R${x:,.2f}".replace(',', 'v').replace('.', ',').replace('v', '.'))
        print("\n👤 Clientes que mais compraram:")
        print(df.to_string(index=False))
    except Exception as e:
        print(f"❌ Erro na consulta: {e}")

def listar_pedidos_completo(conn):
    try:
        query = """
        SELECT p.id_pedido, p.data_pedido, c.nome AS cliente, r.nome AS representante
        FROM Pedido p
        JOIN Cliente c ON p.id_cliente = c.id_cliente
        JOIN Representante r ON p.id_representante = r.id_representante
        """
        df = pd.read_sql(query, conn)
        print("\n📄 Pedidos com cliente e representante:")
        print(df.to_string(index=False))
    except Exception as e:
        print(f"❌ Erro na consulta: {e}")

def listar_itens_do_pedido(conn):
    try:
        id_pedido = input("Digite o ID do pedido: ")
        query = """
        SELECT ip.id_item, pr.nome AS produto, ip.quantidade, ip.preco_unitario
        FROM Item_Pedido ip
        JOIN Produto pr ON ip.id_produto = pr.id_produto
        WHERE ip.id_pedido = ?
        """
        df = pd.read_sql(query, conn, params=(id_pedido,))
        if df.empty:
            print("⚠️ Nenhum item encontrado para esse pedido.")
        else:
            print(f"\n📋 Itens do Pedido {id_pedido}:")
            print(df.to_string(index=False))
    except Exception as e:
        print(f"❌ Erro na consulta: {e}")

def faturamento_total(conn):
    try:
        query = """
        SELECT SUM(ip.quantidade * ip.preco_unitario) AS faturamento_total
        FROM Item_Pedido ip
        """
        df = pd.read_sql(query, conn)
        valor = df.iloc[0, 0]
        print(f"\n💰 Faturamento total: R${valor:,.2f}".replace(',', 'v').replace('.', ',').replace('v', '.'))
    except Exception as e:
        print(f"❌ Erro na consulta: {e}")

def menu():
    conn = conectar_banco()
    if not conn:
        return
        
    try:
        while True:
            print("\n" + "="*60)
            print(" CONSULTA DIRETA AO BANCO DE DADOS ".center(60))
            print("="*60)
            print("1. Vendas por representante")
            print("2. Faturamento por produto")
            print("3. Clientes que mais compraram")
            print("4. Pedidos com cliente e representante")
            print("5. Itens de um pedido específico")
            print("6. Faturamento total do banco")
            print("7. Listar todas as tabelas e estrutura")
            print("0. Sair")
            
            opcao = input("\nEscolha uma opção: ")
            
            if opcao == "1":
                consulta_vendas_por_representante(conn)
            elif opcao == "2":
                consulta_vendas_por_produto(conn)
            elif opcao == "3":
                clientes_que_mais_compraram(conn)
            elif opcao == "4":
                listar_pedidos_completo(conn)
            elif opcao == "5":
                listar_itens_do_pedido(conn)
            elif opcao == "6":
                faturamento_total(conn)
            elif opcao == "7":
                listar_tabelas(conn)
            elif opcao == "0":
                print("Saindo...")
                break
            else:
                print("⚠️ Opção inválida!")
    finally:
        conn.close()

if __name__ == "__main__":
    menu()
