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
                pais_nuevo = input("Ingrese el nombre del nuevo pais: ")
                while pais_nuevo == "":
                    print("Ingrese un nombre valido")
                    pais_nuevo = input("Ingrese el nombre del nuevo pais: ")
                p_repetido = False
                for pais in paises:
                    if pais["nombre"].lower() == pais_nuevo.lower():
                        print("Debe ingresar un pais que no se encuentre en la lista")
                        p_repetido = True
                if p_repetido:
                     print("Ya existe ese nombre") 
                     return
                   
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

                continente = input('Ingrese el continente al que pertenece: ').lower()  
                while continente =="" or continente not in lista_continentes :
                    print("Ingrese un continente valido")
                    continente = input('Ingrese el continente al que pertenece: ')
                ingreso_pais ={
                    "nombre": pais_nuevo,
                    "poblacion": poblacion,
                    "superficie": area,
                    "continente": continente

                }          
                paises.append(ingreso_pais)
                print('Muchas Gracias')
                for pais in paises:
                    print(pais)

def actualizar(paises):
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

def buscar_pais(paises):
    nombre_buscar = input("Ingrese el nombre del pais que desea buscar: ")
    while nombre_buscar == "":
        print("Ingrese un nombre valido")
        nombre_buscar = input("Ingrese el nombre del pais que desea buscar: ") 
    encontrado = False
    for pais in paises:
        if nombre_buscar.lower() in pais["nombre"].lower():  
             encontrado = True 
             print(f'El pais {pais["nombre"]} tiene una poblacion de {pais["poblacion"]}\nuna superficie de {pais["superficie"]}km2 y pertenece al continente de {pais["continente"]}')
    if encontrado == False:
         print("El pais no existe en la lista")  

def filtrar_cont(paises):
    fil_cont = input("Ingrese el continente que desea filtrar ")
    while fil_cont == "":
        print("Ingrese un nombre valido")  
        fil_cont = input("Ingrese el continente que desea filtrar ") 
    con_enco = False
    print(f"Los paises de {fil_cont} son:")   
    for pais in paises:
        if pais["continente"].lower() == fil_cont.lower():
            print(f"{pais["nombre"]} | Poblacion: {pais["poblacion"]} | Superficie: {pais["superficie"]}km2 ")
            con_enco = True   
    if con_enco == False:
         print("El Continente no existe")           

def filtrar_pobla(paises):
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
        
def filtrar_super(paises):
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
        if pais["superficie"] >= fil_super and pais["superficie"] <= fil_super2:
            print(f'{pais["nombre"]} su superficie es de {pais["superficie"]}')
            encontrar_super = True
    if encontrar_super == False:
        print("No se encontraron paises en ese rango de superficies") 
def ord_nombre(paises):
    cantidad_elementos = len(paises)  
    for indice_pasada in range(cantidad_elementos - 1):  
        intercambio = False 
        for indice_actual in range(cantidad_elementos - 1 - indice_pasada ):
            if paises[indice_actual]["nombre"] > paises[indice_actual + 1]["nombre"]:   
                paises[indice_actual], paises[indice_actual + 1] = paises[indice_actual + 1], paises[indice_actual]
                intercambio = True
        if intercambio == False:
            break        
    for pais in paises:
        print(f'{pais["nombre"]} - {pais["poblacion"]} habitantes')                  
def ord_poblacion(paises):
    cantidad_elementos = len(paises)  
    for indice_pasada in range(cantidad_elementos - 1):  
        intercambio = False 
        for indice_actual in range(cantidad_elementos - 1 - indice_pasada ):
            if paises[indice_actual]["poblacion"] > paises[indice_actual + 1]["poblacion"]:   
                paises[indice_actual], paises[indice_actual + 1] = paises[indice_actual + 1], paises[indice_actual]
                intercambio = True
        if intercambio == False:
            break        
    for pais in paises:
        print(f'habitantes {pais["poblacion"]} - {pais["nombre"]}')   
def ord_superficie(paises):
    cantidad_elementos = len(paises)  
    for indice_pasada in range(cantidad_elementos - 1):  
        intercambio = False 
        for indice_actual in range(cantidad_elementos - 1 - indice_pasada ):
            if paises[indice_actual]["superficie"] > paises[indice_actual + 1]["superficie"]:   
                paises[indice_actual], paises[indice_actual + 1] = paises[indice_actual + 1], paises[indice_actual]
                intercambio = True
        if intercambio == False:
            break        
    for pais in paises:
        print(f'superficie {pais["superficie"]} - {pais["nombre"]}') 


def mostrar_estadiscas(paises):
    mayor= paises[0]
    menor= paises[0]
    total_pobla=0
    total_super=0
    for pais in paises:
        if pais["poblacion"]>=mayor["poblacion"]:
            mayor= pais
        elif pais["poblacion"]<menor["poblacion"]:
            menor= pais
        total_pobla+=pais["poblacion"]
        total_super+=pais["superficie"]
        
    promedio_pobla= total_pobla/len(paises)
    promedio_super= total_super/len(paises)
    print("-----ESTADISTICAS-----")
    print(f"Pais con mayor poblacion {mayor["nombre"]}: {mayor["poblacion"]} habitante\nPais con menor poblacion {menor["nombre"]}: {menor["poblacion"]} habitantes")
    print(f"Promedio de poblacion total: {promedio_pobla:.2f} habitantes\nPromedio de superficie total: {promedio_super:.2f} km2 ")   

def mostrar_paises_cont(paises):
    america=0
    africa=0
    asia=0
    europa=0
    oceania=0
    antartida=0
    for pais in paises:
        if pais["continente"].lower()=="america":
            america+=1
        if pais["continente"].lower()=="africa":
            africa+=1
        if pais["continente"].lower()=="asia":
            asia+=1
        if pais["continente"].lower()=="europa":
            europa+=1
        if pais["continente"].lower()=="oceania":
            oceania+=1
        if pais["continente"].lower()=="antartida":
            antartida+=1
    print(f"Paises por continentes:\nAmerica:{america}\nAfrica:{africa}\nAsia:{asia}\nEuropa:{europa}\nOceania:{oceania}\nAntartida:{antartida}")      
def guardar_paises(paises):
    with open("Paises.csv", "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["nombre", "poblacion", "superficie", "continente"])
        for pais in paises:
            escritor.writerow([
                pais["nombre"],
                pais["poblacion"],
                pais["superficie"],
                pais["continente"]
            ])                
                   
        

paises = cargar_paises()
lista_continentes=["america","africa","antartida","europa","asia","oceania"]
menu = 0
while menu != 7:
    try:
        menu = int(input("\n~~~ Bienvenidos a PaisPedia ~~~\n1)Agregar un Pais \n2)Actualizar los datos de poblacion y superficie \n3)Buscar un pais por nombre \n4)Filtrar paises por... \n5)Ordenar paises por... \n6)Mostras estadisticas \n7)Salir"))
        if menu == 1:
            agregar_pais(paises)
        elif menu == 2:
            actualizar(paises)
        elif menu == 3:
            buscar_pais(paises)
        elif menu == 4:
            try:
                opcion= int(input("1-Filtrar por continente\n2-Filtrar por rango de poblacion\n3-Filtrar por superficie"))
                if opcion == 1:
                    filtrar_cont(paises)
                elif opcion == 2:
                    filtrar_pobla(paises)
                elif opcion == 3:
                    filtrar_super(paises) 
                else:
                    print("Error. No ingreso ninguna opcion posible")
            except ValueError:
                print("Error. Debe ingresar un numero entero")
        elif menu == 5:
            try:
                opcion= int(input("1-Ordenar por nombre\n2-Ordenar por poblacion\n3-Ordenar por superficie"))
                if opcion == 1:
                    ord_nombre(paises)
                elif opcion == 2:
                    ord_poblacion(paises)
                elif opcion == 3:
                    ord_superficie(paises) 
                else:
                    print("Error. No ingreso ninguna opcion posible")
            except ValueError:
                print("Error. Debe ingresar un numero entero")
        elif menu == 6:
            mostrar_estadiscas(paises)
            mostrar_paises_cont(paises)
        elif menu == 7: 
            print("Hasta luego vuelva pronto!!")
        else:
            print("Opcion invalida, ingrese otra opcion")
        guardar_paises(paises)    
    except ValueError:
        print("Error. Debe ingresar un numero")


            
