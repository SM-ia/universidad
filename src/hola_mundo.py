saldo_principal = int(input("¿Cuánto dinero tienes?: "))
usuario = "Cliente"
Ingresar = 0
Retirar = 0
Nada = "Ni ingresar ni retirar"
fallido = 0

if saldo_principal <= 0:
    print("Error: Saldo inicial no válido")
    fallido += 1

# Cambiamos la condición para que el bucle siga mientras el saldo no sea 0
while saldo_principal > 0:
    # Guardamos la opción en una variable en vez de hacer print(input(...))
    opcion = input("Desea ingresar, retirar dinero o salir: ").strip().lower()

    if opcion == "ingresar":
        ingreso = int(input("¿Cuánto deseas ingresar?: "))
        saldo_principal += ingreso
        Ingresar += 1
        print(f"Tienes un total de {saldo_principal}€")

    elif opcion == "retirar":
        retiro = int(input("¿Cuánto deseas retirar?: "))
        # Comprobamos si hay suficiente saldo DESPUÉS de pedir el dinero
        if saldo_principal >= retiro:
            saldo_principal -= retiro
            Retirar += 1
            print(f"Tienes un total de {saldo_principal}€")
        else:
            print("Error: No tienes suficiente saldo")
            fallido += 1

    elif opcion == "salir":
        print("Salir")
        break  # El break se usa solo cuando el usuario quiere SALIR

    else:
        print("Error: Opción no válida")
        fallido += 1

# Resumen final al salir del bucle
print("\n--- RESUMEN ---")
print(saldo_principal, "€")
print(Ingresar, "veces ingresado")
print(Retirar, "veces retirado")
print(fallido, "errores o fallos")