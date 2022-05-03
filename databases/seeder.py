import sqlite3 as sql

#CREO UNA RUTA ABSOLUTA A MI BASE DE DATOS
DB_PATH = "C:\\Users\\Usuario\\OneDrive\\Escritorio\\super_base_scorpion\\databases\\datitos.db"

#CREAMOS BASE DE DATOS A UTILIZAR
def crearBD():
    conectar = sql.connect(DB_PATH)
    cursor = conectar.cursor()
    cursor.execute("""CREATE TABLE datitos (
        nombre  text,
apellido  text,
edad  text,
fecha_nac  text,
email  text,
num_tel  text,
sobre_mi  text,
departamento text,
localidad text,
virtud1  text,
virtud2  text,
virtud3  text,
hab1  text,
hab2  text,
hab3  text,
soft1  text,
soft2  text,
soft3  text,
año1form  text,
año2form  text,
año3form  text,
enteduc1  text,
enteduc2  text,
enteduc3  text,
ciuform1  text,
ciuform2  text,
ciuform3  text,
añoinicio1 text,
añoinicio2  text,
añoinicio3  text,
añoinicio4  text,
añofin1  text,
añofin2  text,
añofin3  text,
añofin4  text,
nomempresa1  text,
nomempresa2  text,
nomempresa3  text,
nomempresa4  text,
puesto1  text,
puesto2  text,
puesto3  text,
puesto4  text,
actrealiz1  text,
actrealiz2  text,
actrealiz3  text,
actrealiz4  text,
contactoref1  text,
contactoref2  text,
contactoref3  text,
nombreref1  text,
nombreref2  text,
nombreref3  text,
empresaref1  text,
empresaref2  text,
empresaref3  text,
idioma1  text,
idioma2  text,
idioma3  text,
idiomanivel1  text,
idiomanivel2  text,
idiomanivel3  text
    )""")
    conectar.commit()
    conectar.close()

#DEFINIMOS UNA VARIABLE PARA AGREGAR DATOS CON TUPLES
def agregarval():
    conectar = sql.connect(DB_PATH)
    cursor = conectar.cursor()
    datos = [
        ("Javier", "Benitez", 24,"06-07-1997", "stevenreybritez@gmail.com", 9838291223 ,"De todo un poco, un poco mas que nada", "Alto Parana", "Ciudad Del Este" ,"Capo", "Genio", "Aparato","Javier", "Apellido", 800000,"Javier", "Apellido", 800000,"Javier", "Apellido", 800000,"Javier", "Apellido", 800000,"Javier", "Apellido", 800000,"Javier", "Apellido", 800000,"Javier", "Apellido", 800000,"Javier", "Apellido", 800000,"Javier", "Apellido", 800000,"Javier", "Apellido", 800000,"Javier", "Apellido", 800000,"Javier", "Apellido", 800000,"Javier", "Apellido", 800000,"Javier", "Apellido", 800000,"Javier", "Apellido", 800000, "Javier", "Apellido", 800000, "Alto", "Alto")
    ]
    cursor.executemany("""INSERT INTO datitos VALUES (?, ?, ?, ?, ?, ?, ?, ?,?, ?, ?,?, ?, ?,?, ?, ?,?, ?, ?,?, ?, ?,?, ?, ?,?, ?, ?,?, ?, ?,?, ?, ?,?, ?, ?,?, ?, ?,?, ?, ?,?, ?, ?,?, ?, ?,?, ?, ?,?, ?, ?,?, ?, ?,?, ?, ?)""", datos)
    conectar.commit()
    conectar.close()

if __name__ == "__main__":
    crearBD()
    agregarval()