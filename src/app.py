from flask import Flask, jsonify, request
from flask_mysqldb import MySQL

from config import config

app = Flask(__name__)

conexion = MySQL(app)

@app.route('/carreras', methods=['GET'])
def listar_carreras():
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT IDCarrera, Nombre, Semestres FROM carreras"
        cursor.execute(sql)
        datos = cursor.fetchall()
        carreras = []
        for fila in datos:
            carrera = {'idCarrera':fila[0], 'nombre': fila[1], 'semestres':fila[2]}
            carreras.append(carrera)
        return jsonify({'carreras':carreras, 'mensaje':'carreras listadas.'})
    except Exception as ex:
        return jsonify({'mensaje':'Error'})
    
@app.route('/materias', methods=['GET'])
def listar_materias():
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT IDMateria, IDCarrera, Nombre, IDEspecialidad FROM materias"
        cursor.execute(sql)
        datos = cursor.fetchall()
        materias = []
        for fila in datos:
            materia = {'idMateria':fila[0], 'idCarrera': fila[1], 'nombre':fila[2], 'idEspecialidad':fila[3]}
            materias.append(materia)
        return jsonify({'materias':materias, 'mensaje':'materias listadas.'})
    except Exception as ex:
        return jsonify({'mensaje':'Error'})

@app.route('/especialidades', methods=['GET'])
def listar_especialidades():
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT IDEspecialidad, IDCarrera, Nombre FROM especialidades"
        cursor.execute(sql)
        datos = cursor.fetchall()
        especialidades = []
        for fila in datos:
            especialidad = {'idEspecialidad':fila[0], 'idCarrera': fila[1], 'nombre':fila[2]}
            especialidades.append(especialidad)
        return jsonify({'especialidad':especialidades, 'mensaje':'especialidades listadas.'})
    except Exception as ex:
        return jsonify({'mensaje':'Error'})
    
@app.route('/especialidades/<idCarrera>', methods=['GET'])
def leer_especialidad(idCarrera):
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT IDEspecialidad, IDCarrera, Nombre FROM especialidades WHERE IDCarrera = '{0}'".format(idCarrera)
        cursor.execute(sql)
        datos = cursor.fetchall()
        if datos:
            especialidades = []
            for fila in datos:
                especialidad = {'idEspecialidad':fila[0], 'idCarrera': fila[1], 'nombre':fila[2]}
                especialidades.append(especialidad)
            return jsonify({'especialidad':especialidades, 'mensaje':'Especialidades listadas.'})
        else:
            return jsonify({"mensaje": "No se encontraron especialidades para la carrera proporcionada."})
    except Exception as ex:
        print(ex)
        return jsonify({"mensaje": "Error"})
    
@app.route('/carreras/<idCarrera>', methods=['GET'])
def leer_carrera(idCarrera):
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT IDCarrera, Nombre, Semestres FROM carreras WHERE IDCarrera = '{0}'".format(idCarrera)
        cursor.execute(sql)
        datos=cursor.fetchone()
        if datos != None:
            carrera = {'idCarrera':datos[0], 'nombre': datos[1], 'semestres':datos[2]}
            return jsonify({'carreras': carrera, 'mensaje':"Carrera encontrada."})
        else:
            return jsonify({"mensaje": "Carrera no encontrada"})
    except Exception as ex:
        print(ex)
        return jsonify({"mensaje": "Error"})
    
@app.route('/materias/carrera/<idCarrera>', methods=['GET'])
def leer_materiaByCarrera(idCarrera):
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT IDMateria, IDCarrera, Nombre, IDEspecialidad FROM materias WHERE IDCarrera = '{0}'".format(idCarrera)
        cursor.execute(sql)
        datos = cursor.fetchall()
        if datos:
            materias = []
            for fila in datos:
                materia = {'idMateria':fila[0], 'idCarrera': fila[1], 'nombre':fila[2], 'idEspecialidad':fila[3]}
                materias.append(materia)
            return jsonify({'materias por carrera':materias, 'mensaje':'Materias por carrera listadas.'})
        else:
            return jsonify({"mensaje": "No se encontraron materias para la carrera proporcionada."})
    except Exception as ex:
        print(ex)
        return jsonify({"mensaje": "Error"})

@app.route('/materias/especialidad/<idEspecialidad>', methods=['GET'])
def leer_materiaByEspecialidad(idEspecialidad):
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT IDMateria, IDCarrera, Nombre, IDEspecialidad FROM materias WHERE IDEspecialidad = '{0}'".format(idEspecialidad)
        cursor.execute(sql)
        datos = cursor.fetchall()
        if datos:
            materias = []
            for fila in datos:
                materia = {'idMateria':fila[0], 'idCarrera': fila[1], 'nombre':fila[2], 'idEspecialidad':fila[3]}
                materias.append(materia)
            return jsonify({'materias por carrera':materias, 'mensaje':'Materias por carrera listadas.'})
        else:
            return jsonify({"mensaje": "No se encontraron materias para la especialidad proporcionada."})
    except Exception as ex:
        print(ex)
        return jsonify({"mensaje": "Error"})

@app.route('/carreras', methods=['POST'])
def registrar_carrera():
    try:
        #print(request.json)   RECUPERAMOS LOS DATOS INGRESADOS
        cursor = conexion.connection.cursor()
        sql = """INSERT INTO carreras (IDCarrera, Nombre, Semestres) 
        VALUES ('{0}','{1}', {2})""".format(request.json['idCarrera'], request.json['nombre'], 
                                            request.json['semestres'])
        cursor.execute(sql)
        conexion.connection.commit() #Confirma la accion de insersión
        return jsonify({"mensaje": "Carrera registrada"})
    except Exception as ex:
        print(ex)
        return jsonify({"mensaje": "Error"})
    
@app.route('/materias', methods=['POST'])
def registrar_materia():
    try:
        #print(request.json)   RECUPERAMOS LOS DATOS INGRESADOS
        cursor = conexion.connection.cursor()
        sql = """INSERT INTO materias (IDMateria, IDCarrera, Nombre, IDEspecialidad) 
        VALUES ('{0}','{1}', '{2}', '{3}')""".format(request.json['idMateria'], request.json['idCarrera'], 
                                            request.json['nombre'], request.json['idEspecialidad'])
        cursor.execute(sql)
        conexion.connection.commit() #Confirma la accion de insersión
        return jsonify({"mensaje": "Materia registrada"})
    except Exception as ex:
        print(ex)
        return jsonify({"mensaje": "Error"})
    
@app.route('/especialidades', methods=['POST'])
def registrar_especialidad():
    try:
        #print(request.json)   RECUPERAMOS LOS DATOS INGRESADOS
        cursor = conexion.connection.cursor()
        sql = """INSERT INTO especialidades (IDEspecialidad, IDCarrera, Nombre) 
        VALUES ('{0}','{1}', '{2}')""".format(request.json['idEspecialidad'], request.json['idCarrera'], 
                                            request.json['nombre'])
        cursor.execute(sql)
        conexion.connection.commit() #Confirma la accion de insersión
        return jsonify({"mensaje": "Especialidad registrada"})
    except Exception as ex:
        print(ex)
        return jsonify({"mensaje": "Error"})
    
@app.route("/carreras/<idCarrera>", methods=['PUT'])
def editar_carrera(idCarrera):
    try:
        #print(request.json)   RECUPERAMOS LOS DATOS INGRESADOS
        cursor = conexion.connection.cursor()
        sql = """UPDATE carreras SET Nombre = '{0}', Semestres = '{1}' 
        WHERE IDCarrera = '{2}'""".format(request.json['nombre'],request.json['semestres'],idCarrera)
        cursor.execute(sql)
        conexion.connection.commit() #Confirma la accion de insersión
        return jsonify({"mensaje": "Carrera actualizada"})
    except Exception as ex:
        print(ex)
        return jsonify({"mensaje": "Error"})
    
@app.route("/materias/<idMateria>", methods=['PUT'])
def editar_materia(idMateria):
    try:
        #print(request.json)   RECUPERAMOS LOS DATOS INGRESADOS
        cursor = conexion.connection.cursor()
        sql = """UPDATE materias SET IDCarrera = '{0}', Nombre = '{1}', IDEspecialidad = '{2}' 
        WHERE IDMateria = '{3}'""".format(request.json['idCarrera'],request.json['nombre'], 
                                          request.json['idEspecialidad'], idMateria)
        cursor.execute(sql)
        conexion.connection.commit() #Confirma la accion de insersión
        return jsonify({"mensaje": "Materia actualizada"})
    except Exception as ex:
        print(ex)
        return jsonify({"mensaje": "Error"})
    
@app.route("/especialidades/<idEspecialidad>", methods=['PUT'])
def editar_especialidad(idEspecialidad):
    try:
        #print(request.json)   RECUPERAMOS LOS DATOS INGRESADOS
        cursor = conexion.connection.cursor()
        sql = """UPDATE especialidades SET IDCarrera = '{0}', Nombre = '{1}' 
        WHERE IDEspecialidad = '{2}'""".format(request.json['idCarrera'],request.json['nombre'],idEspecialidad)
        cursor.execute(sql)
        conexion.connection.commit() #Confirma la accion de insersión
        return jsonify({"mensaje": "Especialidad actualizada"})
    except Exception as ex:
        print(ex)
        return jsonify({"mensaje": "Error"})

@app.route('/carreras/<idCarrera>', methods=['DELETE'])
def eliminar_carrera(idCarrera):
    try:
        #print(request.json)   RECUPERAMOS LOS DATOS INGRESADOS
        cursor = conexion.connection.cursor()
        sql = "DELETE FROM carreras WHERE IDCarrera = '{0}'".format(idCarrera)
        cursor.execute(sql)
        conexion.connection.commit() #Confirma la accion de insersión
        return jsonify({"mensaje": "Carrera eliminada."})
    except Exception as ex:
        print(ex)
        return jsonify({"mensaje": "Error"})

@app.route('/especialidades/<idEspecialidad>', methods=['DELETE'])
def eliminar_especialidad(idEspecialidad):
    try:
        #print(request.json)   RECUPERAMOS LOS DATOS INGRESADOS
        cursor = conexion.connection.cursor()
        sql = "DELETE FROM especialidades WHERE IDEspecialidad = '{0}'".format(idEspecialidad)
        cursor.execute(sql)
        conexion.connection.commit() #Confirma la accion de insersión
        return jsonify({"mensaje": "Carrera eliminada."})
    except Exception as ex:
        print(ex)
        return jsonify({"mensaje": "Error"})

@app.route('/materias/<idMateria>', methods=['DELETE'])
def eliminar_materia(idMateria):
    try:
        #print(request.json)   RECUPERAMOS LOS DATOS INGRESADOS
        cursor = conexion.connection.cursor()
        sql = "DELETE FROM materias WHERE IDMateria = '{0}'".format(idMateria)
        cursor.execute(sql)
        conexion.connection.commit() #Confirma la accion de insersión
        return jsonify({"mensaje": "Materia eliminada."})
    except Exception as ex:
        print(ex)
        return jsonify({"mensaje": "Error"})
    
def pagina_no_encontrada(error):
    return "<h1>La página que intentas buscar no existe...", 404

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    #app.run()
    app.run(host="0.0.0.0")