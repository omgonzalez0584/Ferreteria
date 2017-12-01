import pymysql

db = pymysql.connect('127.0.0.1','root','root','usuarios')
cursor = db.cursor()

def validar_acceso(user,password):
    if cursor.execute("""SELECT * FROM vendedores WHERE user = %s""", user) and cursor.execute("""SELECT * FROM vendedores WHERE pass = %s""", password):
       return 0
    else:
        return 1

def cerrar_acceso():
    db.close()





