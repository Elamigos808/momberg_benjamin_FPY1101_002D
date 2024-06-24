#trabajo hecho por Benjamin Momberg (solo...por eso esta tan malo)
#bienvenida
print("hola bienvenido a bilblioteca duoc")
print("--------------------")
#ingresar los libros y definirlos del 1 al 5
libro1=input("ingresse el primer libro: ")
print("--------------------")
libro2=input("ingresse el segundo libro: ")
print("--------------------")
libro3=input("ingresse el tercer libro: ")
print("--------------------")
libro4=input("ingresse el cuarto libro: ")
print("--------------------")
libro5=input("ingresse el quinto libro: ")
print("--------------------")
#libros guardados en la coleccion
coleccion=[libro1,libro2,libro3,libro4,libro5] 
#mostrar la lista
print("su coleccion es la siguiente: ",coleccion)
#opcion de modificar agregar y eliminar
opcion=int(input("¿desea modificar la lista? 1=si / 2=no(SALIR DEL PROGRAMA): "))
if opcion==1:
    opcion=int(input("que desea modificar 1_modificar un libro / 2_eliminar un libro / 3_agregar un libro / 4_salir(SALIR DEL PROGRAMA): "))
    if opcion==1:
        modificar=int(input("que libro desea modificar: "))
    elif opcion==2:
        eliminar=int(input("que libro desea eliminar: "))
    elif opcion==3:
        agregar=int(input("que libro desea agregar: "))
    elif opcion==4:
        print("saliendo del programa...")
        print("muchas gracias por ingresar al programa")
        #salida del programa
if opcion==2:
    print("saliendo del programa...")
    print("muchas gracias por ingresar al programa")
    #salida del programa
    