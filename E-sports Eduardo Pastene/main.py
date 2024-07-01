import funciones as fn

puntajes = [["Id Jugador","Nombre","VALORANT","FORTNITE","FIFA","Tipo"]]

menu=True
flag=True
while menu:
    #Identificador de Jugador, Nombre y apellido del jugador, juego, puntaje obtenido.
    jugador = ""
    nombreApellido=""
    opcion=0
    opcionJuego=0
    seguir=True
    dificultad=0
    puntaje=0
    texto=""
    nuevoValor=["","",0,0,0,1]

    print("Bienvenido al menu de registro de puntajes:")
    print("Ingrese una opcion (Escribir de 1 a 4)")
    print("1.- Registrar puntajes torneo")
    print("2.- Listar puntajes")
    print("3.- Imprimir por Tipo")
    print("4.- Salir")
    
    opcion = fn.menuSeleccion(1,4)
    

    if opcion==1:
        flag = True
        while flag:
            jugador=input("Ingrese el nick del jugador:\n")

            if len(jugador)>0:
                flag=False
            else:
                print("El nick del jugador no puede estar vacío")

        flag = True
        while flag:
            nombreApellido=input("Ingrese el Nombre y Apellido del jugador:\n")

            if len(nombreApellido)>0:
                flag=False
            else:
                print("El Nombre y Apellido del jugador no puede estar vacío")
        
        print("Ingrese el nivel de dificultad:")
        print("1.- Principiante")
        print("2.- Avanzado")
        print("3.- Experto")

        dificultad=fn.menuSeleccion(1,3)

        nuevoValor[0]=jugador
        nuevoValor[1]=nombreApellido
        nuevoValor[2]=0
        nuevoValor[3]=0
        nuevoValor[4]=0
        nuevoValor[5]=dificultad
   

        flag=True
        while flag:
            print("Ingrese la opción correspondiente al juego que va a añadir el puntaje:")
            print("1.- VALORANT")
            print("2.- FORTNITE")
            print("3.- FIFA")

            opcionJuego=fn.menuSeleccion(1,3)

            if 1<=opcionJuego<=3:
                nuevoValor[1+opcionJuego]=fn.corrigeInt("Ingresa el puntaje:\n")
                
            
            flag2=True
            while flag2:
                seguir=input("¿Desea actualizar otro puntaje del mismo jugador? (s/n):\n").lower()
                if seguir=="n":
                    flag=False
                    flag2=False
                elif seguir=="s":
                    flag2=False
                else:
                    print("Debes ingresar un valor válido (s o n)")

        puntajes.append(nuevoValor)            
    elif opcion == 2:
        #Listar
        cnt=0

        print("_"*90)
        for i in puntajes:
            if cnt==0:
                print(f"{str(i[0]).ljust(15)} / {str(i[1]).ljust(10)} / {str(i[2]).ljust(10)} / {str(i[3]).ljust(10)} / {str(i[4]).ljust(10)} / {str(i[5]).ljust(15)}")
            else:
                if i[5]==1:
                    print(f"{str(i[0]).ljust(15)} / {str(i[1]).ljust(10)} / {str(i[2]).ljust(10)} / {str(i[3]).ljust(10)} / {str(i[4]).ljust(10)} / {str("Principiante").ljust(15)}")
                elif i[5]==2:
                    print(f"{str(i[0]).ljust(15)} / {str(i[1]).ljust(10)} / {str(i[2]).ljust(10)} / {str(i[3]).ljust(10)} / {str(i[4]).ljust(10)} / {str("Avanzado").ljust(15)}")
                elif i[5]==3:
                    print(f"{str(i[0]).ljust(15)} / {str(i[1]).ljust(10)} / {str(i[2]).ljust(10)} / {str(i[3]).ljust(10)} / {str(i[4]).ljust(10)} / {str("Experto").ljust(15)}")
            print("_"*90)
            cnt+=1
    elif opcion==3:
        #Listar por dificultad

        print("Ingrese el nivel de dificultad:")
        print("1.- Principiante")
        print("2.- Avanzado")
        print("3.- Experto")

        dificultad=fn.menuSeleccion(1,3)

        cnt=0

        texto+=("_"*90)+"\n"
        for i in puntajes:
            if cnt==0:
                texto+=(f"{str(i[0]).ljust(15)} / {str(i[1]).ljust(10)} / {str(i[2]).ljust(10)} / {str(i[3]).ljust(10)} / {str(i[4]).ljust(10)} / {str(i[5]).ljust(15)}\n")
                texto+=("_"*90)+"\n"
            else:
                if i[5]==1 and dificultad==1:
                    texto+=(f"{str(i[0]).ljust(15)} / {str(i[1]).ljust(10)} / {str(i[2]).ljust(10)} / {str(i[3]).ljust(10)} / {str(i[4]).ljust(10)} / {str("Principiante").ljust(15)}\n")
                    texto+=("_"*90)+"\n"
                elif i[5]==2 and dificultad==2:
                    texto+=(f"{str(i[0]).ljust(15)} / {str(i[1]).ljust(10)} / {str(i[2]).ljust(10)} / {str(i[3]).ljust(10)} / {str(i[4]).ljust(10)} / {str("Avanzado").ljust(15)}\n")
                    texto+=("_"*90)+"\n"
                elif i[5]==3 and dificultad==3:
                    texto+=(f"{str(i[0]).ljust(15)} / {str(i[1]).ljust(10)} / {str(i[2]).ljust(10)} / {str(i[3]).ljust(10)} / {str(i[4]).ljust(10)} / {str("Experto").ljust(15)}\n")
                    texto+=("_"*90)+"\n"
            
            cnt+=1
        print(texto)

        texto2="Lista de Jugadores "
        if dificultad==1:
            texto2+="Principiantes"
        elif dificultad==2:
            texto2+="Avanzados"
        elif dificultad==3:
            texto2+="Expertos"
        

        with open(texto2+".txt","w") as archivo:
            archivo.write(texto)
            
    elif opcion==4:
        menu=False
        print("_"*90)
    else:
        print("Debes ingresar una opción valida (1 a 4)")
    
print("Has salido el programa")

            



            
                
            

        







            