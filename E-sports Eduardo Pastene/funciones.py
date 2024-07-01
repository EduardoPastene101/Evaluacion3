def menuSeleccion(a1,a2):
    flagMenuSeleccion=True
    while flagMenuSeleccion:
        try:
            opcionMenuSeleccion=int(input("-->"))
        except:
            print(f"La opción ingresada no es válida: (Debe escoger de {a1} a {a2})")
        else:
            if not a1<=opcionMenuSeleccion<=a2:
                print(f"Debe ingresar una opción en el rango de {a1} a {a2}")
            else:
                flagMenuSeleccion=False
    return opcionMenuSeleccion

def corrigeInt(v):
    corrigeIntFlag=True
    while corrigeIntFlag:
        try:
            corrigeIntVal= int(input(v))
        except:
            print(f"La opción ingresada no es válida, debe ser un número")
        else:
            corrigeIntFlag=False
            return corrigeIntVal
