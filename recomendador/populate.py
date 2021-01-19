from .models import Artista

def deleteTables():
    Artista.objects.all().delete()

def cargar_artista():
    lista=[]
    fileobj = open('./datos/artists.dat', "r", encoding="ISO-8859-1")

    for line in fileobj.readlines():
        linea = line.split()
        if len(linea) != 4:
            continue
        lista.append(Artista(
            pk=int(linea[0].strip()),
            nombre= linea[1].strip(),
            url= linea[2].strip(),
            url_imagen= linea[3].strip()
        ))

    fileobj.close()
    Artista.objects.bulk_create(lista)

    print("Artistas inserted: " + str(Artista.objects.count()))
    print("---------------------------------------------------------")


def populateDatabase():
    deleteTables()
    cargar_artista()
    print("Finished database population")