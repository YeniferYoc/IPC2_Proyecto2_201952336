print("AQUI SE SELECCIONAN LOS DATOS ")
            print("")
            nombrearch=fd.askopenfilename(initialdir = "/",title = "Seleccione archivo",filetypes = (("txt files","*.txt"),("todos los archivos","*.*")))
        
            doc = minidom.parse(nombrearch)
            pisos = doc.getElementsByTagName("piso")
            for piso in pisos:
                nombre = piso.attributes['nombre'].value 
                R = piso.getElementsByTagName("R")[0]
                C = piso.getElementsByTagName("C")[0]
                F = piso.getElementsByTagName("F")[0]
                S = piso.getElementsByTagName("S")[0]
                fila = R.firstChild.data
                columna = C.firstChild.data
                volteo = F.firstChild.data
                intercambio = S.firstChild.data

                patrones = piso.getElementsByTagName('patron')
                lista_patrones = Estructuras_patron.ListaDoble_patron()
                for patron in patrones:
                    codigo_pat = patron.attributes['codigo'].value 
                    patron_letras = patron.childNodes[0].data
                    #print(codigo_pat)
                    #print(patron.childNodes[0].data)
                    patron_nuevo = Patron(codigo_pat, patron_letras)
                    lista_patrones.añadirNodoPrincipio(patron_nuevo)

                piso_nuevo = Piso(nombre, fila, columna, volteo, intercambio, lista_patrones)
                #piso_nuevo.mostrar_piso()
                lista_pisos.añadirNodoPrincipio(piso_nuevo)


            lista_pisos.imprimirLista()