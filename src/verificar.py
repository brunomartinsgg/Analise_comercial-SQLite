import sqlite3
conn = sqlite3.connect('Projeto_Marianne_SQLITE.db')
print(conn.execute('SELECT name FROM sqlite_master WHERE type="table"').fetchall())
conn.close()