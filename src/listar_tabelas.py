import sqlite3
import os

# Substitua pelo caminho REAL do seu arquivo.db
caminho_db = r"C:\Users\Bruno\OneDrive\Documentos\UFAL\Banco de Dados\banco_de_dados\arquivo.db"

if not os.path.exists(caminho_db):
    print(f"❌ Arquivo não encontrado: {caminho_db}")
else:
    try:
        conn = sqlite3.connect(caminho_db)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tabelas = cursor.fetchall()
        
        print("👉 TABELAS NO BANCO DE DADOS:")
        for tabela in tabelas:
            print(f"- {tabela[0]}")
        
        conn.close()
    except Exception as e:
        print(f"❌ Erro: {e}")