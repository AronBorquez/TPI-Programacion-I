import csv

def cargar_paises():
    paises = []
    archivo = open("Paises.csv", "r", encoding="utf-8")
    archivo.readline()
    for linea in archivo:
        datos = linea.strip().split(",")
        pais = {
            "nombre": datos[0],
            "poblacion": int(datos[1]),
            "superficie": int(datos[2]),
            "continente": datos[3]
        }
        paises.append(pais)
    archivo.close()

    return paises

def agregar_pais(paises):     
                pais_nuevo = input("Ingrese el nombre del nevo pais: ")
                while pais_nuevo == "":
                    print("Ingrese un nombre valido")
                    pais_nuevo = input("Ingrese el nombre del nevo pais: ")
                p_repetido = False
                for pais in paises:
                    if pais["nombre"].lower() == pais_nuevo.lower():
                        print("Debe ingresar un pais que no se encuentre en la lista")
                        p_repetido = True
                if p_repetido:
                     print("Ya existe ese nombre") 
                     return
                     pais_nuevo = input("Ingrese el nombre del nevo pais: ")
                     p_repetido = False
                     for pais in paises: 
                        if paises["nombre"].lower() == pais_nuevo.lower():
                            p_repetido = True
                while True:
                    try:    
                        poblacion = int(input("Ingrese la poblacion: "))
                        if poblacion < 0:
                            print("El numero no puede ser negativo")
                        else:
                            break    
                    except ValueError:
                        print("Debe ingresar un numero entero o decimal")
                while True:
                    try:    
                        area = int(input("Ingrese El area: "))
                        if area < 0:
                            print("El numero no puede ser negativo")
                        else:
                            break    
                    except ValueError:
                        print("Debe ingresar un numero entero o decimal")    
                continente = input('Ingrese el continente al que pertenece: ')  
                ingreso_pais ={
                    "nombre": pais_nuevo,
                    "poblacion": poblacion,
                    "superficie": area,
                    "continente": continente

                }          
                paises.append(ingreso_pais)
                print('Muchas Gracias')
                print(paises)
pass
def actualizar():
    nombre_pais = input("Ingrese el nombre del pais que desea actualizar")
    encontrado = False
    for pais in paises:
        if pais["nombre"].lower() == nombre_pais.lower():
            encontrado = True
            while True:
                try:
                    nueva_pobla = int(input('Ingrese la nueva poblacion: '))
                    if nueva_pobla < 0:
                                print("El numero no puede ser negativo")
                    else:
                        break    
                except ValueError:
                    print("Debe ingresar un numero entero")
            while True:
                    try:    
                        nueva_area = int(input("Ingrese la nueva area: "))
                        if nueva_area < 0:
                            print("El numero no puede ser negativo")
                        else:
                            break    
                    except ValueError:
                        print("Debe ingresar un numero entero") 
            pais["poblacion"] = nueva_pobla
            pais["superficie"] = nueva_area                
    if encontrado == False:
         print("No se encontro ese pais")
pass    
paises = cargar_paises()

menu = 0
while menu != 7:
    menu = int(input("~~~ Bienvenidos a PaisPedia ~~~\n1)Agregar un Pais \n2)Actualizar los datos de poblacion y superficie \n3)Buscar un pais por nombre \n4)Filtrar paises por... \n5)Ordenar paises por... \n6)Mostras estadisticas de.. \n7)Salir"))
    if menu == 1:
        agregar_pais(paises)
    elif menu == 2:
        pass
    elif menu == 3:
        pass
    elif menu == 4:
        pass
    elif menu == 5:
        pass
    elif menu == 6:
        pass
    elif menu == 7: 
        print("Hasta luego vuelva pronto!!")



            