import sqlite3

# Conexión a la base de datos
conn = sqlite3.connect('./nutrition/database/dieta.db')
cursor = conn.cursor()

cursor.execute("DELETE FROM desayuno WHERE id = 21")
conn.commit()
conn.close()