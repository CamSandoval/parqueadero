import mysql.connector

cnn= mysql.connector.connect(user="root",password="21042002",
                            host="localhost",
                            database="proyectoParqueadero",
                            port="3306",
                            )

print(cnn)
print("----------------------------------")

cur=cnn.cursor()



print("-------------------------------------")
def consulta_ciudades():
    cur = cnn.cursor()
    cur.execute("SELECT * FROM countries")
    datos = cur.fetchall()
    cur.close()    
    return datos

def inserta_vehiculo(PLACA, TIPO, MENSUALIDAD):
    cur = cnn.cursor()
    sql='''INSERT INTO vehiculo (placa, tipo, mensualidad) 
    VALUES('{}', '{}', '{}')'''.format(PLACA, TIPO,MENSUALIDAD)
    cur.execute(sql)
    n=cur.rowcount
    cnn.commit()    
    cur.close()
    return n   

def actualiza_vehiculo(PLACA,MENSUALIDAD):
    cur = cnn.cursor()
    sql='''UPDATE vehiculo SET mensualidad = '{}' WHERE placa = '{}' '''.format(MENSUALIDAD,PLACA)
    cur.execute(sql)
    n=cur.rowcount
    cnn.commit()    
    cur.close()
    return n  

def elimina_ciudad(Id):
    cur = cnn.cursor()
    sql='''DELETE FROM countries WHERE Id = {}'''.format(Id)
    cur.execute(sql)
    n=cur.rowcount
    cnn.commit()    
    cur.close()
    return n    

placa= str(input("Ingrese la placa de su vehiculo   "))
tipo= str(input("Ingrese la carroceria de su vehiculo   "))
mensualidad= int(input("Ingrese 1 si su vehiculo tiene mensualidad o 0 si no tiene      "))
inserta_vehiculo(placa,tipo,mensualidad)

placa_actualizar= str(input("Ingrese la placa de su vehiculo para actualizar   "))
nueva_mensualidad=int(input("Ingrese 1 para si o 0 para no    "))
actualiza_vehiculo(placa_actualizar,nueva_mensualidad)


cur.execute("SELECT * FROM vehiculo WHERE idvehiculo = 2")
for row in cur.fetchall():
    id=row[1]
    print(id)












