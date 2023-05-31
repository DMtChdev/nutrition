import sqlite3

# Conexión a la base de datos
conn = sqlite3.connect('./nutrition/database/dieta.db')
cursor = conn.cursor()

# Modificar la tabla "alimento" para agregar la columna "tipo_alimento"
cursor.execute('ALTER TABLE alimento ADD COLUMN tipo_alimento TEXT')

# Actualizar los valores de la columna "tipo_alimento" para cada alimento
cursor.execute("UPDATE alimento SET tipo_alimento = 'Lácteo' WHERE id = 1")
cursor.execute("UPDATE alimento SET tipo_alimento = 'Cereal' WHERE id IN (2, 3, 4)")
cursor.execute("UPDATE alimento SET tipo_alimento = 'Acompañamiento' WHERE id IN (5, 6, 7, 8, 9, 10)")
cursor.execute("UPDATE alimento SET tipo_alimento = 'Fruta' WHERE id IN (11, 12, 13, 14, 15, 16, 17, 18, 19, 20)")

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()
