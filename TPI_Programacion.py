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
def buscar_pais():
    nombre_buscar = input("Ingrese el nombre del pais que desea buscar: ")
    while nombre_buscar == "":
        print("Ingrese un nombre valido")
        nombre_buscar = input("Ingrese el nombre del pais que desea buscar: ") 
    encontrado = False
    for pais in paises:
        if pais["nombre"].lower() == nombre_buscar.lower():  
             encontrado = True 
             print(f'El pais {pais["nombre"]} tiene una poblacion de {pais["poblacion"]}\nuna superficie de {pais["superficie"]} y pertenece al continente de {pais["continente"]}')
    if encontrado == False:
         print("El pais no existe en la lista")  
pass   
def filtrar_cont():
    fil_cont = input("Ingrese el continente que desea filtrar ")
    while fil_cont == "":
        print("Ingrese un nombre valido")  
        fil_cont = input("Ingrese el continente que desea filtrar ") 
    con_enco = False
    print(f"Los paises de {fil_cont} son:")   
    for pais in paises:
        if pais["continente"].lower() == fil_cont.lower():
            print(pais["nombre"])
            con_enco = True   
    if con_enco == False:
         print("El Continente no existe")           
pass 
def filtrar_pobla():
    while True:
        try:    
            fil_pobla1 = int(input("Ingrese la poblacion minima: "))
            if fil_pobla1 < 0:
                print("El numero no puede ser negativo")
            else:
                break    
        except ValueError:
            print("Debe ingresar un numero entero")
    while True:
        try:    
            fil_pobla2 = int(input("Ingrese la poblacion maxima: "))
            if fil_pobla2 < 0:
                print("El numero no puede ser negativo")
            else:
                break    
        except ValueError:
            print("Debe ingresar un numero entero") 
    if fil_pobla1 > fil_pobla2:
        print("La población mínima no puede ser mayor que la máxima.")
        return     
    encontrar_pobla = False   
    for pais in paises:
        if pais["poblacion"] >= fil_pobla1 and pais["poblacion"] <= fil_pobla2:
            print(f'{pais["nombre"]} su poblacion es de {pais["poblacion"]}')
            encontrar_pobla = True
    if encontrar_pobla == False:
        print("No se encontraron paises en ese rango de poblaciones")        
pass  
def filtrar_super():
    while True:
        try:    
            fil_super = int(input("Ingrese la superficie minima: "))
            if fil_super < 0:
                print("El numero no puede ser negativo")
            else:
                break    
        except ValueError:
            print("Debe ingresar un numero entero")
    while True:
        try:    
            fil_super2 = int(input("Ingrese la superficie maxima: "))
            if fil_super2 < 0:
                print("El numero no puede ser negativo")
            else:
                break    
        except ValueError:
            print("Debe ingresar un numero entero") 
    if fil_super > fil_super2:
        print("La superficie mínima no puede ser mayor que la máxima.")
        return 
    encontrar_super = False
    for pais in paises:
        if pais["superficie"] >= fil_super and pais["poblacion"] <= fil_super2:
            print(f'{pais["nombre"]} su poblacion es de {pais["poblacion"]}')
            encontrar_super = True
    if encontrar_super == False:
        print("No se encontraron paises en ese rango de superficies") 
pass
                   
          
          
                    
        

paises = cargar_paises()

menu = 0
while menu != 7:
    menu = int(input("~~~ Bienvenidos a PaisPedia ~~~\n1)Agregar un Pais \n2)Actualizar los datos de poblacion y superficie \n3)Buscar un pais por nombre \n4)Filtrar paises por... \n5)Ordenar paises por... \n6)Mostras estadisticas de.. \n7)Salir"))
    if menu == 1:
        agregar_pais(paises)
    elif menu == 2:
        actualizar(paises)
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



            