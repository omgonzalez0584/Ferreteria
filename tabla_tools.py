import pymysql

db = pymysql.connect('127.0.0.1','root','root','ferreteria')
cursor = db.cursor()

def mostrar_tools():
    cursor.execute('''SELECT * FROM herramientas''')
    resultado = cursor.fetchall()
    print("Lista de Herramientas disponibles:")
    for fila in resultado:
        print("{0}     :     {1}     :     {2}     :     {3}".format(fila[0], fila[1], fila[2], fila[3]))

def ingresar_tools(cod,name,price,cant,brand):
    if cursor.execute("""SELECT codigo FROM herramientas where codigo = %s""", cod):
        print("Codigo ya existe!")

    else:
        cursor.execute("""INSERT INTO herramientas(codigo,nombre,precio,cantidad,marca)
                      values(%s,%s,%s,%s,%s)""", (cod,name,price,cant,brand))
        db.commit()

def borrar_tools():
    print("Lista de Herramientas")
    cursor.execute("""select codigo,nombre from herramientas""")
    listado = cursor.fetchall()
    for i in listado:
        print(i)
    cod = input("Introduzca el codigo del articulo que desea borrar:  ")
    cursor.execute("""DELETE FROM herramientas where codigo = %s""",cod)
    db.commit()


def cerrar_tools():
    db.close()

