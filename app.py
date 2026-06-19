from flask import Flask, request
import sqlite3

app = Flask(__name__)

def iniciar_db():
    conexion = sqlite3.connect('mi_base.db')
    cursor = conexion.cursor()
    
    # Creamos una tabla con más datos profesionales
    cursor.execute('''CREATE TABLE IF NOT EXISTS empleados (
        id INTEGER PRIMARY KEY, 
        nombre TEXT, 
        correo TEXT,
        profesion TEXT, 
        rol TEXT,
        dato_confidencial TEXT
    )''')
    cursor.execute("DELETE FROM empleados") 
    
   
    cursor.execute("INSERT INTO empleados (nombre, correo, profesion, rol, dato_confidencial) VALUES ('admin', 'admin@sistema.com', 'Arquitecto de Software', 'Administrador', 'Token AWS: ZQ98-X12M-PL44')")
    cursor.execute("INSERT INTO empleados (nombre, correo, profesion, rol, dato_confidencial) VALUES ('juan', 'juan@sistema.com', 'Ingeniero de Pruebas', 'Usuario', 'Acceso estándar')")
    cursor.execute("INSERT INTO empleados (nombre, correo, profesion, rol, dato_confidencial) VALUES ('mariel', 'mariel@sistema.com', 'Desarrolladora Backend', 'Usuario', 'Acceso estándar')")
    cursor.execute("INSERT INTO empleados (nombre, correo, profesion, rol, dato_confidencial) VALUES ('carlos', 'carlos@sistema.com', 'Analista de Datos', 'Usuario', 'Acceso estándar')")
    
    conexion.commit()
    conexion.close()

iniciar_db()


@app.route('/buscar')
def buscar_usuario():
    usuario_buscado = request.args.get('nombre', '')
    
    conexion = sqlite3.connect('mi_base.db')
    cursor = conexion.cursor()
    
    consulta = "SELECT * FROM empleados WHERE nombre = '" + usuario_buscado + "'"
    
    try:
        cursor.execute(consulta)
        resultados = cursor.fetchall()
        
        return f"""
        <h3>Consulta ejecutada en la base de datos:</h3> 
        <p style="color:red; font-family:monospace; background:#eee; padding:10px;">{consulta}</p> 
        <h3>Resultados encontrados:</h3> 
        <p>{resultados}</p>
        """
    except Exception as e:
        return f"Error SQL: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)