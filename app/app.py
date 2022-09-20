from flask import Flask, render_template, redirect, request, flash, url_for
from datetime import datetime
from flask_mysqldb import MySQL
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'hospital'

mysql = MySQL(app)


app.secret_key = 'secreto'

#### Manegadores Medicos ####
def especialidades():
    cursor = mysql.connection.cursor()
    sql = "SELECT * FROM especialidades"
    cursor.execute(sql)
    especialidad = cursor.fetchall()
    return especialidad

def consultas():
    cursor = mysql.connection.cursor()
    sql = "SELECT * FROM consultas"
    cursor.execute(sql)
    consultas = cursor.fetchall()
    return consultas

def pacientes():
    cursor = mysql.connection.cursor()
    sql = "SELECT * FROM pacientes"
    cursor.execute(sql)
    pacientes = cursor.fetchall()
    return pacientes

@app.route('/medicos')
def lista_medicos():
    cursor = mysql.connection.cursor()
    sql = "SELECT * FROM medicos"
    cursor.execute(sql)
    medico = cursor.fetchall()
    return render_template('medicos.html',medicos=medico, especialidades=especialidades())

def medicos():
    cursor = mysql.connection.cursor()
    sql = "SELECT * FROM medicos"
    cursor.execute(sql)
    medicos = cursor.fetchall()
    return medicos

@app.route('/guardar-medico', methods=['POST'])
def agregar_medico():
    if request.method == 'POST':
        run = request.form['run']
        nombre = request.form['nombre']
        paterno = request.form['paterno']
        materno = request.form['materno']
        especialidad = request.form['especialidad']
        fecha = datetime.now().strftime('%Y-%m-%d')
        activo = 1

        cursor = mysql.connection.cursor()
        sql = "INSERT INTO medicos (rut_medico, nombre_medico, paterno_medico, materno_medico, fecha_registro_medico, activo, id_especialidad) VALUES (%s, %s, %s,  %s, %s,%s, %s)"
        cursor.execute(sql,(run, nombre, paterno, materno, fecha, activo, especialidad))
        mysql.connection.commit()
        flash("Medico agregado con exito.")
        return redirect('medicos')

@app.route('/actualizar-medico',methods=['POST'])
def actualizar_medico():
    if request.method == 'POST':
        rut  = request.form['run']
        nombre  = request.form['nombre']
        paterno  = request.form['paterno']
        materno  = request.form['materno']
        especialidad  = request.form['especialidad']

        cursor = mysql.connection.cursor()
        sql = 'UPDATE  medicos SET nombre_medico=%s, paterno_medico=%s, materno_medico=%s, id_especialidad=%s WHERE rut_medico = %s'
        cursor.execute(sql,(nombre, paterno, materno, especialidad, rut))
        mysql.connection.commit()
        flash("Medico actualizado con exito.")
        return redirect('medicos')

@app.route('/editar-medico/<rut>')
def editar_medico(rut):
    cursor = mysql.connection.cursor()
    sql = 'SELECT * FROM medicos WHERE rut_medico = %s'
    cursor.execute(sql,[rut])
    dato = cursor.fetchall()
    return render_template('editar_medico.html',datos=dato, especialidades=especialidades())

@app.route('/eliminar-medico/<rut>')
def eliminar_medico(rut):
    cursor = mysql.connection.cursor()
    sql = 'UPDATE  medicos SET activo = 0 WHERE rut_medico = %s'
    cursor.execute(sql,[rut])
    mysql.connection.commit()
    flash("Medico eliminado con exito.")
    return redirect('/medicos')
    
#### FIN ####

#### Manegadores Pacientes ####
@app.route('/pacientes')
def lista_pacientes():
    cursor = mysql.connection.cursor()
    sql = "SELECT * FROM pacientes"
    cursor.execute(sql)
    paciente = cursor.fetchall()
    return render_template('pacientes.html',pacientes=paciente)

@app.route('/guardar-paciente', methods=['POST'])
def agregar_paciente():
    if request.method == 'POST':
        rut = request.form['run']
        nombre = request.form['nombre']
        paterno = request.form['paterno']
        materno = request.form['materno']
        edad = request.form['edad']
        peso = request.form['peso']
        estatura = request.form['estatura']
        fumador = request.form.get('fumador')
        tiempo = request.form.get('tiempo')
        dieta = request.form.get('dieta')
        fecha = datetime.now().strftime('%Y-%m-%d')
        activo = 1

        if tiempo is None:
            tiempo = 0

        cursor = mysql.connection.cursor()
        sql = "INSERT INTO pacientes (rut_paciente, nombre_paciente, paterno_paciente, materno_paciente, edad_paciente, peso_paciente, estatura_paciente,fumador_paciente, tiempo_fumador, dieta_paciente, fecha_registro_paciente, activo) VALUES (%s, %s, %s,  %s, %s, %s, %s,%s, %s, %s,%s, %s)"
        cursor.execute(sql,(rut, nombre, paterno, materno, edad, peso, estatura, fumador, tiempo, dieta, fecha, activo))
        mysql.connection.commit()
        flash("Paciente agregado con exito.")
        return redirect('pacientes')

@app.route('/actualizar-paciente',methods=['POST'])
def actualizar_paciente():
    rut  = request.form['run']
    nombre  = request.form['nombre']
    paterno  = request.form['paterno']
    materno  = request.form['materno']
    edad  = request.form['edad']
    peso  = request.form['peso']
    estatura  = request.form['estatura']
    fumador  = request.form['fumador']
    tiempo  = request.form['tiempo']
    dieta  = request.form['dieta']

    cursor = mysql.connection.cursor()
    sql = 'UPDATE  pacientes SET nombre_paciente=%s, paterno_paciente=%s, materno_paciente=%s, edad_paciente=%s , peso_paciente=%s, estatura_paciente=%s, fumador_paciente=%s, tiempo_fumador=%s, dieta_paciente=%s WHERE rut_paciente = %s'
    cursor.execute(sql,(nombre, paterno, materno, edad, peso, estatura, fumador, tiempo, dieta, rut))
    mysql.connection.commit()
    flash("Paciente actualizado con exito.")
    return redirect('pacientes')

@app.route('/editar-paciente/<rut>')
def editar_paciente(rut):
    cursor = mysql.connection.cursor()
    sql = 'SELECT * FROM pacientes WHERE rut_paciente = %s'
    cursor.execute(sql,[rut])
    dato = cursor.fetchall()
    return render_template('editar_paciente.html',datos=dato)

@app.route('/eliminar-paciente/<rut>')
def eliminar_paciente(rut):
    cursor = mysql.connection.cursor()
    sql = 'UPDATE  pacientes SET activo = 0 WHERE rut_paciente = %s'
    cursor.execute(sql,[rut])
    mysql.connection.commit()
    flash("Paciente eliminado con exito.")
    return redirect('/pacientes')

#### FIN ####

#### Manegadores Atenciones ####
@app.route('/atenciones')
def atencion():
    cursor = mysql.connection.cursor()
    sql = 'SELECT * FROM pacientes'
    cursor.execute(sql)
    dato = cursor.fetchall()
    return render_template('atenciones.html',datos=dato, consultas=consultas(), medicos=medicos(), pacientes=pacientes())


@app.route('/lista_atenciones')
def lista_atenciones():
    cursor = mysql.connection.cursor()
    sql = 'SELECT * FROM atenciones ORDER BY prioridad DESC'
    cursor.execute(sql)
    atenciones = cursor.fetchall()


    return render_template('lista_atenciones.html',atenciones=atenciones, consultas=consultas(), medicos=medicos(), pacientes=pacientes())

@app.route('/nueva_atencion', methods=['POST'])
def nueva_atencion():
    if request.method == 'POST': 
        run = request.form['run']
        cursor = mysql.connection.cursor()
        sql = 'SELECT * FROM pacientes WHERE rut_paciente = %s'
        cursor.execute(sql,[run])
        paciente = cursor.fetchall()
        consulta = consultas()
        if paciente[0][4] >= 1 and paciente[0][4] <= 5:
            prioridad = int(round(paciente[0][5]/(paciente[0][6])**2))+3
            prioridad = int(round((paciente[0][4]*prioridad)/100))
        elif paciente[0][4] >= 6 and paciente[0][4] <= 12:
            prioridad = int(round(paciente[0][5]/(paciente[0][6])**2))+2
            prioridad = int(round((paciente[0][4]*prioridad)/100))
        elif paciente[0][4] >= 13 and paciente[0][4] <= 15:
            prioridad = int(round(paciente[0][5]/(paciente[0][6])**2))+1
            prioridad = int(round((paciente[0][4]*prioridad)/100))
        elif paciente[0][4] >= 16 and paciente[0][4] <= 40:
            if paciente[0][7] == 1: 
                prioridad = int(round(paciente[0][8]/4))+2
                prioridad = int(round((paciente[0][4]*prioridad)/100))
            elif paciente[0][7] == 0: 
                prioridad = 2
                prioridad = int(round((paciente[0][4]*prioridad)/100))
        elif paciente[0][4] >= 41 and paciente[0][4] <= 100:
            if paciente[0][9] == 1 and paciente[0][4] >= 60 and paciente[0][4] <= 100: 
                prioridad = int(round(paciente[0][4]/20))+4
                prioridad = int(round(((paciente[0][4]*prioridad)/100)+5.3))
            elif paciente[0][9] == 0:
                prioridad = int(round(paciente[0][4]/30))+3
                prioridad = int(round(((paciente[0][4]*prioridad)/100)+5.3))

        id=0

        if paciente[0][4] >= 1 and paciente[0][4] <= 15 and prioridad <= 4:
            for consulta in consultas():
                if consulta[2] == 3:
                    id = consulta[0]
                    break
            if id > 0:
                return render_template('nueva_atencion.html',prioridad=prioridad, id_consulta=id, pacientes=paciente, tipo_consulta=3)
            else:
                flash("No hay consultas para el paciente.")
                return redirect('atenciones')  

        elif paciente[0][4] >= 16 and paciente[0][4] <= 100 and prioridad <= 4:
            for consulta in consultas():
                if consulta[2] == 1:
                    id = consulta[0]
                    break
            if id > 0:
                return render_template('nueva_atencion.html',prioridad=prioridad, id_consulta=id, pacientes=paciente, tipo_consulta=3)
            else:
                flash("No hay consultas para el paciente.")
                return redirect('atenciones')  

        elif paciente[0][4] >= 1 and paciente[0][4] <= 100 and prioridad > 4:
            for consulta in consultas():
                if consulta[2] == 1:
                    id = consulta[0]
                    break
            if id > 0:
                return render_template('nueva_atencion.html',prioridad=prioridad, id_consulta=id, pacientes=paciente, tipo_consulta=3)
            else:
                flash("No hay consultas para el paciente.")
                return redirect('atenciones')  
        
        
@app.route('/guardar-atencion', methods=['POST'])
def agregar_antencion():
    if request.method == 'POST':
        id_consulta = request.form['id_consulta']
        rut_paciente = request.form['rut']
        fecha_atencion = datetime.now().strftime('%Y-%m-%d')
        hora_atencion = datetime.now().strftime('%H:%M:%S')
        valor_consulta = request.form['valor']
        observacion = request.form['observacion']
        prioridad = request.form['prioridad']
        activo = 1

        cursor = mysql.connection.cursor()
        sql = "INSERT INTO atenciones (id_consulta, rut_paciente, fecha_atencion, hora_atencion, valor_consulta, observacion_atencion, prioridad, activo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql,(id_consulta, rut_paciente, fecha_atencion, hora_atencion, valor_consulta, observacion, prioridad, activo))
        mysql.connection.commit()
        flash("Atention agregada con exito.")
        return redirect('atenciones')

@app.route('/actualizar-atencion',methods=['POST'])
def actualizar_atencion():
    if request.method == 'POST':
        id_atencion = request.form['id_atencion']
        id_consulta = request.form['id_consulta']
        rut_paciente = request.form['rut']
        fecha_atencion = request.form['fecha']
        hora_atencion = request.form['hora']
        valor_consulta = request.form['valor']
        observacion = request.form['observacion']
    
        cursor = mysql.connection.cursor()
        sql = 'UPDATE  atenciones SET id_consulta=%s, rut_paciente=%s, fecha_atencion=%s, hora_atencion=%s, valor_consulta=%s, observacion_atencion=%s WHERE id_atencion = %s'
        cursor.execute(sql,(id_consulta, rut_paciente, fecha_atencion, hora_atencion, valor_consulta, observacion, id_atencion))
        mysql.connection.commit()
        flash("Actualizacion antencion con exito.")
        return redirect('lista_atenciones')

@app.route('/editar-atencion/<id>')
def editar_atencion(id):
    cursor = mysql.connection.cursor()
    sql = 'SELECT * FROM atenciones WHERE id_atencion = %s'
    cursor.execute(sql,[id])
    dato = cursor.fetchall()
    return render_template('editar_atencion.html',atenciones=dato, consultas=consultas())

@app.route('/eliminar-atencion/<id>')
def eliminar_atencion(id):
    cursor = mysql.connection.cursor()
    sql = 'UPDATE  atenciones SET activo = 0 WHERE id_atencion = %s'
    cursor.execute(sql,[id])
    mysql.connection.commit()
    return redirect('/atenciones')


#### FIN ####

#### Manegadores Consulta ####
def tipo_consulta():
    cursor = mysql.connection.cursor()
    sql = "SELECT * FROM tipo_consultas"
    cursor.execute(sql)
    tipos = cursor.fetchall()
    return tipos

def estado_consulta():
    cursor = mysql.connection.cursor()
    sql = "SELECT * FROM estado_consultas"
    cursor.execute(sql)
    estados = cursor.fetchall()
    return estados

@app.route('/consultas')
def consulta():
    cursor = mysql.connection.cursor()
    sql = "SELECT * FROM consultas"
    cursor.execute(sql)
    lista_consultas = cursor.fetchall()
    return render_template('consultas.html',consultas=lista_consultas, tipos=tipo_consulta(), medicos=medicos(), estados=estado_consulta())

@app.route('/guardar-consulta', methods=['POST'])
def agregar_consulta():
      if request.method == 'POST':
        rut = request.form['run']
        tipo_consulta = request.form['tipo']
        estado_consulta = request.form['estado']
        observacion = request.form['observacion']
        activa = 1

        cursor = mysql.connection.cursor()
        sql = 'INSERT INTO consultas (rut_medico, id_tipo_consulta, id_estado_consulta, observacion_consulta, activa) VALUES (%s, %s, %s, %s, %s)'
        cursor.execute(sql,(rut, tipo_consulta, estado_consulta, observacion, activa))
        mysql.connection.commit()
        flash('Consulta agregada con exito.')
        return redirect('/consultas')

@app.route('/actualizar-consulta',methods=['POST'])
def actualizar_consutla():
    if request.method == 'POST':
        
        medico = request.form['medico']
        tipo_consulta = request.form['tipo']
        estado_consulta = request.form['estado']
        observacion = request.form['observacion']
        id_consulta = request.form['id_consulta']

        cursor = mysql.connection.cursor()
        sql = 'UPDATE  consultas SET rut_medico=%s, id_tipo_consulta=%s, id_estado_consulta=%s, observacion_consulta=%s WHERE id_consulta = %s'
        cursor.execute(sql,(medico, tipo_consulta,estado_consulta, observacion, id_consulta))
        mysql.connection.commit()
        flash('Consulta actualizada con exito.')
        return redirect('/consultas')

@app.route('/editar-consulta/<id>')
def editar_consulta(id):
    cursor = mysql.connection.cursor()
    sql = 'SELECT * FROM consultas WHERE id_consulta = %s'
    cursor.execute(sql,[id])
    dato = cursor.fetchall()
    return render_template('editar_consulta.html',datos=dato, medicos=medicos(), tipos=tipo_consulta(), estados=estado_consulta())

@app.route('/eliminar-consulta/<id>')
def eliminar_consutla(id):
    cursor = mysql.connection.cursor()
    sql = 'UPDATE  consultas SET activa = 0 WHERE id_consulta = %s'
    cursor.execute(sql,[id])
    mysql.connection.commit()
    print(id)
    flash('Consulta eliminada con exito.')
    return redirect('/consultas')

#### FIN ####


   
@app.route('/')
def Index():
    return render_template('atenciones.html')



if __name__ == '__main__':
    app.run(debug=True)



    