peliculas={
    "Mejor guion": [],
    "Mejor direccion": [],
    "Mejor banda sonora": [],
    "Mejor animacion": [],
}
while True: 
    print("--- Menu ---")
    print("1. Registrar pelicula y su categoria")
    print("2. Registrar votos por titulos")
    print("3. Mostrar resultados actuales")
    print("4. Peliculas ganadoras (Se cerrara el programa despues de seleccionar esta funcion)")
    try: 
        menu=int(input("Ingresa un numero segun la operacion que desea realizar: "))
        if menu == 1:
            print("Registrar peliculas")
            try:
                titulo=str(input("Ingrese el nombre de la pelicula: "))
                categoria=str(input("Ingrese a la categoria que desea ingresar la pelicula: "))
                if categoria in peliculas:
                    peliculas[categoria].append({"Titulo": titulo,"Votos": 0})
                    print(f"Pelicula: {titulo} registrada correctamente")
                else:
                    print("Categoria no encontrada")
                
            except ValueError:
                print("Valor invalido")
            except IndexError:
                print("No existe la categoria adentro del diccionario")
            
        elif menu == 2: 
            print("Registrar votos por titulo")
            try:
                categoria=str(input("Ingrese la categoria a la que desea dar su voto: "))
                if categoria not in peliculas:
                    print("Categoria no existente")
                    continue
                print("Peliculas disponibles:")
                for peli in peliculas[categoria]:
                    print(f"- {peli["Titulo"]} (Votos: {[peli["Votos"]]})")
                pelicula=str(input("Ingrese a que pelicula desea dar su voto: "))
                encontrada=False
                for peli in peliculas[categoria]:
                    if peli["Titulo"].lower()==pelicula.lower():
                        peli["Votos"]+=1
                        print(f"Voto registrado para {pelicula}")
                        encontrada=True
                        break
                if not encontrada:
                    print("Le pelicula no se encuentra en la categoria indicada")
            except ValueError:
                print("Valor invalido")
            except IndexError:
                print("La pelicula o categoria no se encuentran dentro de la lista")
        elif menu == 3 :
            print("Mostrar resultados actuales")
            for cate in peliculas:
                print("-------------")
                print(f"Categoria: {cate}")
                for peli in peliculas[cate]:
                    print("------------")
                    print(f"Pelicula: {peli["Titulo"]}")
                    print(f"Votos: {peli["Votos"]}")        
        elif menu == 4 :
            x=0
            print("Peliculas ganadoras")
            for cate,lista_peliculas in peliculas.items():
                if not lista_peliculas:
                    print(f"{cate}: No hay peliculas registradas")
                else:
                    ganadora=max(lista_peliculas, key=lambda p: p["Votos"])
                    print(f"Categoria: {cate}: Ganadora: {ganadora["Titulo"]} con {ganadora["Votos"]} votos")
            print("Fin del programa...")
            break
    except ValueError:
        print("Debe ingresar un numero entero. Vuelva a intentarlo")