#GESTOR DE RECETAS DE COCINA
recetas_favoritas = []
recetas = []
print("Bienvenido al Gestor de Recetas de Cocina")
continuar=True
while continuar:
    print("")
    print("1. Agregar Receta")
    print("2. Buscar receta por nombre")
    print("3. Agregar receta a favoritas")
    print("4. Ver recetas favoritas" )
    print("5. Ver todas las recetas")
    print("6. Eliminar receta")
    print("7. Salir")
    print("")

    opcion = input("Digite el número de la opción que desea seleccionar: ")
    if opcion == "1":
        nombre = input("Ingrese el nombre de la receta: ").strip().lower()
        ingredientes_input = input("Ingrese los ingredientes (separados por comas): ")
        ingredientes = [i.strip() for i in ingredientes_input.split(",")]
        pasos = input("Ingrese los pasos de la receta: ").strip()
        nueva_receta = {
            "nombre": nombre,
            "ingredientes": ingredientes,
            "pasos": pasos
        }
        recetas.append(nueva_receta)
        print(f"la receta {nombre} se agregó con éxito!")

    elif opcion == "2":
        busqueda = input("Ingrese el nombre de la receta: ").strip().lower()
        encontrada = False

        for receta in recetas:
            if receta["nombre"].lower() == busqueda:
                ingredientes_texto = ", ".join(receta['ingredientes'])
                print(f"Receta encontrada: {receta["nombre"].upper()}")
                print(f"Ingredientes: {ingredientes_texto}")
                print(f"Pasos para la preparación: {receta['pasos']}")
                encontrada = True
                break
        if not encontrada:
            print("Receta no encontrada")

    elif opcion=="3":
        nombre = input("Ingrese el nombre de la receta que desea agregar a favoritas: ").strip().lower()
        encontrada = False

        for receta in recetas:
            if receta["nombre"].lower()==nombre:
                recetas_favoritas.append(receta)
                print(f"La receta {receta["nombre"]} se agregó a favoritas")
                encontrada = True
                break
        if not encontrada:
            print("No se encontró esa receta en la lista principal")

    elif opcion=="4":
        for fav in recetas_favoritas:
                ingredientes_texto = ", ".join(fav['ingredientes'])
                print(f"* {fav['nombre'].capitalize()}: {ingredientes_texto}")

    elif opcion=="5":
      for receta in recetas:
                ingredientes_texto = ", ".join(receta['ingredientes'])
                print(f"* {receta['nombre'].capitalize()}: {ingredientes_texto}")


    elif opcion=="6":
        busqueda = input("Ingrese el nombre de la receta que desea eliminar: ").strip().lower()
        encontrada = False

        for receta in recetas:
            if receta["nombre"].lower() == busqueda:
                recetas.remove(receta)
                print(f"La receta '{busqueda}' ha sido eliminada con éxito")
                encontrada = True
                break

    elif opcion=="7":
        print("Hasta luego!")
        break

    else:
        print("Opción no válida. Intente de nuevo")