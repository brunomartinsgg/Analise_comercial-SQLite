import sqlite3
import pandas as pd
import locale
from pathlib import Path
import sys
import os

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def resource_path(relative_path):
    """Resolve caminhos para recursos incluídos no executável"""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def formatar_moeda(valor):
    """Formata valores como moeda brasileira"""
    return locale.currency(valor, grouping=True, symbol=True)

def gerar_relatorio():
    """Gera relatório com formatação profissional"""
    try:
        db_path = resource_path("database.db")
        conn = sqlite3.connect(db_path)
        
        query = """
            SELECT r.nome, SUM(ip.quantidade * ip.preco_unitario) as total_vendas
            FROM Representante r
            JOIN Pedido p ON r.id_representante = p.id_representante
            JOIN Item_Pedido ip ON p.id_pedido = ip.id_pedido
            GROUP BY r.nome
            ORDER BY total_vendas DESC
        """
        
        df = pd.read_sql(query, conn)
        
        df['total_vendas'] = df['total_vendas'].apply(formatar_moeda)
        
        print("\n" + "="*50)
        print("RELATÓRIO DE VENDAS - VALORES EM REAIS")
        print("="*50)
        print(df.to_string(index=False, header=True, justify='left'))
        print("="*50)
        
        return True
        
    except Exception as e:
        print(f"\n❌ ERRO: {str(e)}")
        return False
    finally:
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    if gerar_relatorio():
        print("\n✅ Relatório gerado com sucesso!")
    else:
        print("\n❌ Falha na geração do relatório")
    input("\nPressione Enter para sair...")