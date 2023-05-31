import sqlite3

# Conexión a la base de datos
conn = sqlite3.connect('./nutrition/database/dieta.db')
cursor = conn.cursor()

# Creación de la tabla "alimento"
cursor.execute('''CREATE TABLE IF NOT EXISTS alimento (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT,
                    calorias INTEGER,
                    carbohidratos INTEGER,
                    proteinas INTEGER,
                    grasas INTEGER,
                    tipo_alimento TEXT)''')

# Creación de la tabla "desayuno"
cursor.execute('''CREATE TABLE IF NOT EXISTS desayuno (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    lacteo INTEGER,
                    cereal INTEGER,
                    acompañamiento INTEGER,
                    fruta INTEGER,
                    tipodesayuno TEXT,
                    FOREIGN KEY (lacteo) REFERENCES alimento(id),
                    FOREIGN KEY (cereal) REFERENCES alimento(id),
                    FOREIGN KEY (acompañamiento) REFERENCES alimento(id),
                    FOREIGN KEY (fruta) REFERENCES alimento(id))''')

# Creación de la tabla "dia"
cursor.execute('''CREATE TABLE IF NOT EXISTS dia (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    desayuno INTEGER,
                    media_manana INTEGER,
                    comida INTEGER,
                    merienda INTEGER,
                    cena INTEGER,
                    fecha DATE UNIQUE,
                    FOREIGN KEY (desayuno) REFERENCES desayuno(id),
                    FOREIGN KEY (media_manana) REFERENCES alimento(id),
                    FOREIGN KEY (comida) REFERENCES desayuno(id),
                    FOREIGN KEY (merienda) REFERENCES desayuno(id),
                    FOREIGN KEY (cena) REFERENCES desayuno(id))''')


# Conexión a la base de datos
conn = sqlite3.connect('./nutrition/database/dieta.db')
cursor = conn.cursor()
# Lista de alimentos con sus datos
alimentos = [
    ('Vaso de leche desnatada (200 ml)', 68, 9, 6, 0, 'Lácteo'),
    ('Café (200 ml)', 2, 0, 0, 0, 'Lácteo'),
    ('Pan integral (40g)', 90, 18, 4, 1, 'Cereal'),
    ('Tostadas tipo biscottes (2 unidades)', 65, 13, 2, 0, 'Cereal'),
    ('Cereales integrales (30g)', 120, 26, 3, 1, 'Cereal'),
    ('Tomate', 20, 4, 1, 0, 'Acompañamiento'),
    ('Pavo', 92, 1, 21, 1, 'Acompañamiento'),
    ('Jamón serrano (máx. 2 veces/sem)', 224, 0, 29, 11, 'Acompañamiento'),
    ('Jamón york', 120, 2, 16, 5, 'Acompañamiento'),
    ('Queso fresco', 80, 2, 13, 2, 'Acompañamiento'),
    ('Manzana', 52, 14, 0, 0, 'Fruta'),
    ('Plátano', 96, 23, 1, 0, 'Fruta'),
    ('Pera', 60, 15, 0, 0, 'Fruta'),
    ('Mandarina', 53, 13, 1, 0, 'Fruta'),
    ('Fresas', 32, 8, 1, 0, 'Fruta'),
    ('Melocotón', 39, 10, 1, 0, 'Fruta'),
    ('Piña', 50, 13, 0, 0, 'Fruta'),
    ('Melón', 29, 7, 1, 0, 'Fruta'),
    ('Uvas', 69, 18, 1, 0, 'Fruta'),
    ('Ciruelas', 46, 12, 1, 0, 'Fruta'),
    ('Sandía', 30, 8, 0, 0, 'Fruta'),
    ('Nectarina', 44, 11, 1, 0, 'Fruta'),
    ('Mango', 60, 15, 1, 0, 'Fruta'),
    ('Frambuesas', 32, 8, 1, 0, 'Fruta'),
    ('Manzana verde', 52, 14, 0, 0, 'Fruta')
]

# Insertar registros en la tabla
cursor.executemany('INSERT INTO alimento VALUES (NULL, ?, ?, ?, ?, ?,?)', alimentos)
conn.commit()


# Registros de desayuno
desayunos = [
    (1, 1, 2, 3, 4, 'desayuno'),
    (2, 1, 3, 5, 6, 'desayuno'),
    (3, 1, 4, 7, 8, 'desayuno'),
    (4, 1, 2, 9, 10, 'desayuno'),
    (5, 1, 3, 5, 11, 'desayuno'),
    (6, 1, 4, 3, 12, 'desayuno'),
    (7, 1, 2, 5, 13, 'desayuno'),
    (8, 1, 3, 7, 14, 'desayuno'),
    (9, 1, 4, 9, 15, 'desayuno'),
    (10, 1, 3, 5, 16, 'desayuno'),
    (11, 1, 4, 7, 17, 'desayuno'),
    (12, 1, 2, 9, 18, 'desayuno'),
    (13, 1, 3, 5, 19, 'desayuno'),
    (14, 1, 4, 3, 20, 'desayuno'),
    (15, 1, 2, 5, 4, 'desayuno'),
    (16, 1, 3, 7, 6, 'desayuno'),
    (17, 1, 4, 9, 8, 'desayuno'),
    (18, 1, 3, 5, 10, 'desayuno'),
    (19, 1, 4, 7, 11, 'desayuno'),
    (20, 1, 2, 9, 12, 'comida')
]

# Insertar registros en la tabla "desayuno"
cursor.executemany('INSERT INTO desayuno VALUES (?,?,?,?,?,?)', desayunos)

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()
