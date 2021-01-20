from .models import Artista, Etiqueta, UsuarioArtista, UsuarioEtiquetaArtista

def vaciar_tablas():
    Artista.objects.all().delete()
    Etiqueta.objects.all().delete()
    UsuarioArtista.objects.all().delete()
    UsuarioEtiquetaArtista.objects.all().delete()

def cargar_artistas():
    lista = []
    artistas = []
    fileobj = open('./datos/artists.dat', "r", encoding="latin-1")

    for line in fileobj.readlines()[1:]:
        linea = line.split("\t")
        if len(linea) > 4:
            continue
        elif len(linea) == 3:
            lista.append(Artista(
                pk=int(linea[0]),
                nombre= linea[1],
                url= linea[2]))
        else:
            lista.append(Artista(
                pk=int(linea[0]),
                nombre= linea[1],
                url= linea[2],
                url_imagen= linea[3]))
        artistas.append(int(linea[0]))

    fileobj.close()
    Artista.objects.bulk_create(lista)

    print("Artistas insertados: " + str(Artista.objects.count()))
    print("---------------------------------------------------------")
    return artistas

def cargar_etiquetas():
    lista = []
    etiquetas = []
    fileobj = open('./datos/tags.dat', "r", encoding="latin-1")

    for line in fileobj.readlines()[1:]:
        linea = line.split("\t")
        lista.append(Etiqueta(
            pk=int(linea[0]),
            valor= linea[1]))
        etiquetas.append(int(linea[0]))


    fileobj.close()
    Etiqueta.objects.bulk_create(lista)

    print("Etiquetas insertadas: " + str(Etiqueta.objects.count()))
    print("---------------------------------------------------------")
    return etiquetas

def cargar_usuarios_artistas():
    lista = []
    fileobj = open('./datos/user_artists.dat', "r", encoding="latin-1")

    for line in fileobj.readlines()[1:]:
        linea = line.split("\t")
        lista.append(UsuarioArtista(
            usuario=int(linea[0]),
            artista= Artista.objects.get(id=int(linea[1])),
            tiempo_escuchado= int(linea[2])))

    fileobj.close()
    UsuarioArtista.objects.bulk_create(lista)

    print("Usuarios-Artistas insertados: " + str(UsuarioArtista.objects.count()))
    print("---------------------------------------------------------")

def cargar_usuarios_etiquetas_artistas(artistas, etiquetas):
    lista = []
    fileobj = open('./datos/user_taggedartists.dat', "r", encoding="latin-1")

    for line in fileobj.readlines()[1:]:
        linea = line.split("\t")
        artista_id = int(linea[1])
        etiqueta_id = int(linea[2])
        if artista_id in artistas and etiqueta_id in etiquetas:
            lista.append(UsuarioEtiquetaArtista(
                usuario=int(linea[0]),
                artista= Artista.objects.get(id=artista_id),
                etiqueta= Etiqueta.objects.get(id=etiqueta_id),
                dia= linea[3],
                mes= linea[4],
                anyo= linea[5]))

    fileobj.close()
    UsuarioEtiquetaArtista.objects.bulk_create(lista)

    print("Usuarios-Etiquetas-Artistas insertados: " + str(UsuarioEtiquetaArtista.objects.count()))
    print("---------------------------------------------------------")

def populateDatabase():
    vaciar_tablas()
    artistas = cargar_artistas()
    etiquetas = cargar_etiquetas()
    cargar_usuarios_artistas()
    cargar_usuarios_etiquetas_artistas(artistas, etiquetas)
    print("Finished database population")