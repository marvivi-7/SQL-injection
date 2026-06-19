#  SQL-injection (Dockerizado)

Aplicación web deliberadamente vulnerable, que permite demostrar cómo una mala gestión de consultas a bases de datos expone información confidencial.

## Estructura del Proyecto
- app.py: Aplicación Flask con la lógica de la base de datos y la vulnerabilidad de inyección SQL.
- Dockerfile: Instrucciones para empaquetar la aplicación en un contenedor.
- requirements.txt: Dependencias del proyecto (Flask).

## 1. Instrucciones de Instalación y Ejecución
### A. Descargar el proyecto
Clona el repositorio en tu máquina local:
git clone https://github.com/marvivi-7/SQL-injection.git
cd SQL-injection

### B. Construir la imagen
Ejecuta el siguiente comando para crear la imagen de Docker:
docker build -t mi-lab-sql .

### C. Ejecutar el contenedor
Levanta el servicio exponiendo el puerto 5001 hacia tu máquina local:
docker run -p 5001:5000 mi-lab-sql

## 2. Demostración del Ataque (SQL Injection)

Una vez que el contenedor esté corriendo, abre tu navegador y dirígete a http://localhost:5001/buscar para realizar las siguientes pruebas:

### Escenario A: Comportamiento Normal
Para buscar a un usuario legítimo (ejemplo: juan), usa:
http://localhost:5001/buscar?nombre=juan
Resultado: La aplicación devuelve únicamente los datos del usuario solicitado.

### Escenario B: Ataque (SQL Injection)
Para saltarte la seguridad y extraer toda la base de datos, usa:
http://localhost:5001/buscar?nombre=' OR '1'='1
Resultado: La consulta SQL se altera para evaluar una condición siempre verdadera ('1'='1'), lo que fuerza al sistema a mostrar todos los registros de la tabla, exponiendo información confidencial.

## 3. Análisis de la Vulnerabilidad

La aplicación es insegura porque concatena directamente la entrada del usuario en la sentencia SQL sin ninguna validación o sanitización:

consulta = "SELECT * FROM empleados WHERE nombre = '" + usuario_buscado + "'"
cursor.execute(consulta)

## 4. Mitigación (Cómo solucionarlo)

Para prevenir este ataque en aplicaciones reales, es obligatorio utilizar sentencias preparadas (prepared statements). De esta forma, la base de datos trata la entrada del usuario estrictamente como un dato y nunca como parte del código SQL:

cursor.execute("SELECT * FROM empleados WHERE nombre = ?", (usuario_buscado,))
