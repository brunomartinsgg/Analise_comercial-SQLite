import sqlite3
import os

# Conecta ao banco de dados
db_path = os.path.join(os.getcwd(), 'arquivo.db')  # Assumindo que o arquivo.db está na mesma pasta
print(f"📁 Tentando acessar: {db_path}")

try:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # 1. Lista todas as tabelas
    print("\n👉 TABELAS EXISTENTES:")
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    for tabela in cursor.fetchall():
        print(f"- {tabela[0]}")
    
    # 2. Verifica a tabela Representante
    print("\n🔍 VERIFICANDO 'Representante':")
    cursor.execute("SELECT sql FROM sqlite_master WHERE name='Representante';")
    resultado = cursor.fetchone()
    
    if resultado:
        print("✅ Tabela encontrada! Estrutura:")
        print(resultado[0])
    else:
        print("❌ Tabela 'Representante' não encontrada!")
    
    conn.close()
    
except Exception as e:
    print(f"\n❌ ERRO: {str(e)}")
    print("Possíveis causas:")
    print("- Arquivo .db não encontrado")
    print("- Permissões insuficientes")
    print("- Banco corrompido")