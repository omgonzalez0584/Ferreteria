import tabla_tools
import validar_userDB
import getpass

def main():

   cont = 0
   while cont != 3:
       print("Sistema de Inventario")
       print("Login!")
       user = input("Usuario: ")
       password = getpass._raw_input("Password: ")
       acc =validar_userDB.validar_acceso(user,password)

       if acc == 0:
          print("Acceso autorizado!")
          while True:
              print("1.Mostrar Herramientas Disponibles")
              print("2.Ingresar nuevas Herramientas")
              print("3.Borrar Alguna Herramienta")
              print("4.Vender Herramientas")
              print("5.Salir del sistema: ")
              opc =  int(input("Escoja una opcion:  "))

              if opc == 5:
                  print("Adios...")
                  tabla_tools.cerrar_tools()
                  break

              elif opc == 1:
                  tabla_tools.mostrar_tools()

              elif opc == 2:
                   cod = input("Introduzca el codigo: ")
                   name = input("Nombre: ")
                   price = float(input("Precio: "))
                   cant= int(input("Cantidad: "))
                   brand = input("Marca: ")
                   tabla_tools.ingresar_tools(cod,name,price,cant,brand)
              elif opc == 3:
                  tabla_tools.borrar_tools()
              else:
                  print("En contruccion...!")

       else:
           print("Usuario Incorrecto")
           cont = cont + 1
           print("Tiene ",cont," intentos")
   if cont == 3:
       print("Tiene 3 intentos...Acceso Denegado!")
       print("Adios!")
       validar_userDB.cerrar_acceso()
   else:
       print("Adios....")


main()






