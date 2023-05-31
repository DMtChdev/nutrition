import os
import sqlite3
from flask import Flask, render_template, request, redirect, url_for
import datetime
app = Flask(__name__)
db_path = './nutrition/database/dieta.db'


@app.route('/')
def inicio():
    message = request.args.get('message')  # Obtener el mensaje de la URL
    return render_template('index.html', message=message)

   
import os
import sqlite3
from flask import Flask, render_template, request, redirect, url_for
import datetime
app = Flask(__name__)
db_path = './nutrition/database/dieta.db'


@app.route('/')
def inicio():
    message = request.args.get('message')  # Obtener el mensaje de la URL
    return render_template('index.html', message=message)

# Ruta para agregar desayuno
@app.route('/agregar_desayuno', methods=['GET', 'POST'])
def agregar_desayuno():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Consultar los nombres de las columnas
    cursor.execute("PRAGMA table_info(desayuno)")
    column_names = [column[1] for column in cursor.fetchall()]

    # Consultar los desayunos disponibles desde la base de datos
    cursor.execute('''SELECT d.id, a1.nombre AS lacteo_nombre, a2.nombre AS cereal_nombre, a3.nombre AS acompañamiento_nombre, a4.nombre AS fruta_nombre,
                            (SELECT SUM(calorias) FROM alimento WHERE id IN (d.lacteo, d.cereal, d.acompañamiento, d.fruta)) AS total_calorias,
                            (SELECT SUM(carbohidratos) FROM alimento WHERE id IN (d.lacteo, d.cereal, d.acompañamiento, d.fruta)) AS total_carbohidratos,
                            (SELECT SUM(proteinas) FROM alimento WHERE id IN (d.lacteo, d.cereal, d.acompañamiento, d.fruta)) AS total_proteinas,
                            (SELECT SUM(grasas) FROM alimento WHERE id IN (d.lacteo, d.cereal, d.acompañamiento, d.fruta)) AS total_grasas
                        FROM desayuno d
                        JOIN alimento a1 ON d.lacteo = a1.id
                        JOIN alimento a2 ON d.cereal = a2.id
                        JOIN alimento a3 ON d.acompañamiento = a3.id
                        JOIN alimento a4 ON d.fruta = a4.id
                        GROUP BY d.id''')

    desayunos = cursor.fetchall()
    print('request.method:'+request.method)

    if request.method == 'POST':
        row_data = request.get_json().get('rowData')
        print(row_data)
        # Obtener la fecha de hoy en formato YYYY-MM-DD
        fecha_hoy = datetime.date.today().isoformat()
        # Obtener el ID del desayuno seleccionado desde la solicitud POST
        desayuno_id = row_data[0]
        print('id:'+desayuno_id)

        # Comprobar si existe un registro para la fecha actual
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM dia WHERE fecha = ?", (fecha_hoy,))
        result = cursor.fetchone()
        if result:
            # Si existe, actualizar el registro con el nuevo valor
            cursor.execute("UPDATE dia SET desayuno = ? WHERE fecha = ?", (desayuno_id, fecha_hoy))
            conn.commit()
            print('Registro actualizado en la base de datos')
            message = 'El registro ha sido actualizado correctamente.'
        else:
            # Si no existe, insertar el nuevo registro
            cursor.execute("INSERT INTO dia ( desayuno,fecha) VALUES (?, ?)", (desayuno_id, fecha_hoy))
            conn.commit()
            print('Nuevo registro insertado en la base de datos')
            message = 'El recurso ha sido insertado correctamente.'

        conn.close()

        # Redirigir a la página de ini  cio con el mensaje
        print('DMC RETURN')
        return render_template('index.html', message=message)

        # Redirigir a la página de inicio u otra página según sea necesario

    else:
        # Consultar los desayunos disponibles desde la base de datos (ejemplo con SQLite)
        


        cursor.execute('''SELECT  d.id, a1.nombre AS lacteo_nombre, a2.nombre AS cereal_nombre, a3.nombre AS acompañamiento_nombre, a4.nombre AS fruta_nombre,
                            (SELECT SUM(calorias) FROM alimento WHERE id IN (d.lacteo, d.cereal, d.acompañamiento, d.fruta)) AS total_calorias,
                            (SELECT SUM(carbohidratos) FROM alimento WHERE id IN (d.lacteo, d.cereal, d.acompañamiento, d.fruta)) AS total_carbohidratos,
                            (SELECT SUM(proteinas) FROM alimento WHERE id IN (d.lacteo, d.cereal, d.acompañamiento, d.fruta)) AS total_proteinas,
                            (SELECT SUM(grasas) FROM alimento WHERE id IN (d.lacteo, d.cereal, d.acompañamiento, d.fruta)) AS total_grasas
                        FROM desayuno d
                        JOIN alimento a1 ON d.lacteo = a1.id
                        JOIN alimento a2 ON d.cereal = a2.id
                        JOIN alimento a3 ON d.acompañamiento = a3.id
                        JOIN alimento a4 ON d.fruta = a4.id
                        GROUP BY d.id
                        
                        ''')



        column_names = [description[0].replace('_nombre', '')     for description in cursor.description]  # Obtener los nombres de las columnas sin el sufijo "_nombre"
        column_names = [description.replace('total_', '') for description in column_names]  # Obtener los nombres de las columnas sin el prefijo "total_"

        desayunos = cursor.fetchall()
        conn.close()
    
        return render_template('agregar_desayuno.html', column_names=column_names, desayunos=desayunos)



@app.route('/agregar_media_manana',methods=['GET', 'POST'])
def agregar_media_manana():
    if request.method == 'POST':
        fruta_id = request.form['fruta']
        print(f'Fruta seleccionada: {fruta_id}')
     # Obtener la fecha de hoy en formato YYYY-MM-DD
        fecha_hoy = datetime.date.today().isoformat()
        

        # Comprobar si existe un registro para la fecha actual
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM dia WHERE fecha = ?", (fecha_hoy,))
        result = cursor.fetchone()
        if result:
            # Si existe, actualizar el registro con el nuevo valor
            cursor.execute("UPDATE dia SET media_manana = ? WHERE fecha = ?", (fruta_id, fecha_hoy))
            conn.commit()
            print('Registro actualizado en la base de datos')
            message = 'El registro ha sido actualizado correctamente.'
        else:
            # Si no existe, insertar el nuevo registro
            cursor.execute("INSERT INTO dia (fecha, media_manana) VALUES (?, ?)", (fecha_hoy, fruta_id))
            conn.commit()
            print('Nuevo registro insertado en la base de datos')
            message = 'El recurso ha sido insertado correctamente.'

        conn.close()

        # Redirigir a la página de inicio con el mensaje
        print('DMC RETURN')
        return render_template('index.html', message=message)

    


    else:
        with app.app_context():
            # Crear la conexión a la base de datos
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()

            # Realizar la consulta a la base de datos para obtener los alimentos de tipo "Fruta"
            cursor.execute("SELECT id, nombre FROM alimento WHERE tipo_alimento = 'Fruta'")
            alimentos_fruta = cursor.fetchall()
            print(alimentos_fruta)
            # Cerrar el cursor y la conexión
            cursor.close()
            conn.close()
        
    # Renderizar el template de agregar_media_manana.html y pasar los alimentos_fruta como variable
    return render_template('agregar_media_manana.html', alimentos_fruta=alimentos_fruta)
import datetime
@app.route('/diario', methods=['GET', 'POST'])
def mostrar_diario():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

 

    if request.method == 'POST':
        print(request.form.get('fecha_anterior'))
        print(request.form.get('fecha_siguiente'))
        if 'fecha_anterior' in request.form:
            fecha_hoy = datetime.datetime.strptime(request.form.get('fecha_anterior'), '%Y-%m-%d').date()
        elif 'fecha_siguiente' in request.form:
            fecha_hoy = datetime.datetime.strptime(request.form.get('fecha_siguiente'), '%Y-%m-%d').date()
            print(fecha_hoy)
    else:
        fecha_hoy = datetime.date.today()
    print('FECHA HOY: '+str(fecha_hoy))
    cursor.execute("""
        SELECT d.*, desayuno.tipodesayuno, desayuno_lacteo.nombre AS lacteo_nombre, desayuno_cereal.nombre AS cereal_nombre,
            desayuno_acompañamiento.nombre AS acompañamiento_nombre, desayuno_fruta.nombre AS fruta_nombre,
            media_manana_alimento.nombre AS media_manana_nombre
        FROM dia d
        LEFT JOIN desayuno ON d.desayuno = desayuno.id
        LEFT JOIN alimento desayuno_lacteo ON desayuno.lacteo = desayuno_lacteo.id
        LEFT JOIN alimento desayuno_cereal ON desayuno.cereal = desayuno_cereal.id
        LEFT JOIN alimento desayuno_acompañamiento ON desayuno.acompañamiento = desayuno_acompañamiento.id
        LEFT JOIN alimento desayuno_fruta ON desayuno.fruta = desayuno_fruta.id
        LEFT JOIN alimento media_manana_alimento ON d.media_manana = media_manana_alimento.id
        WHERE d.fecha = ?
        """, (fecha_hoy.isoformat(),))

    dia_info = cursor.fetchone()
    fecha_anterior = fecha_hoy - datetime.timedelta(days=1)
    fecha_siguiente = fecha_hoy + datetime.timedelta(days=1)
    print('fechas:'+ str(fecha_anterior)+' '+str(fecha_siguiente))
    if dia_info is None:
        message = "No existen registros para el día de hoy."
        return render_template("index.html", message=message)
        
    conn.close()

    # Obtener los nombres de las columnas de la tabla "dia"
    column_names = [description[0].replace("_", " ") for description in cursor.description]

    # Combinar los nombres de las columnas con los valores del día en un diccionario
    dia_data = {column_names[i]: dia_info[i] for i in range(len(column_names))}
    

    # Resto del código...

    return render_template('diario.html', dia_info=dia_data, fecha_hoy=fecha_hoy, fecha_anterior=fecha_anterior, fecha_siguiente=fecha_siguiente)

# Crear la base de datos si no existe
if not os.path.exists(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS alimento (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT,
                    calorias INTEGER,
                    carbohidratos INTEGER,
                    proteinas INTEGER,
                    grasas INTEGER)''')

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

    cursor.execute('''CREATE TABLE IF NOT EXISTS dia (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    desayuno INTEGER,
                    media_manana INTEGER,
                    desayuno INTEGER,
                    merienda INTEGER,
                    cena INTEGER,
                    fecha DATE,
                    FOREIGN KEY (desayuno) REFERENCES desayuno(id),
                    FOREIGN KEY (media_manana) REFERENCES desayuno(id),
                    FOREIGN KEY (desayuno) REFERENCES desayuno(id),
                    FOREIGN KEY (merienda) REFERENCES desayuno(id),
                    FOREIGN KEY (cena) REFERENCES desayuno(id))''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    app.run()
