import shelve


from django.shortcuts import render
from .populate import populateDatabase
from .models import Artista, UsuarioArtista
from .forms import FormularioUsuario

# Create your views here.

def index(request):
    return render(request, 'index.html')

def popularBD(request):
    populateDatabase()
    return render(request, 'populate.html')

def popularDic(request):
    loadDict()
    return render(request, 'populate.html')

def loadDict():
    PrefsUsuarios = {}
    shelf = shelve.open("dataRS.dat")
    usuarios_artistas = UsuarioArtista.objects.all()
    for u_a in usuarios_artistas:
        usuario_id = int(u_a.usuario)
        artista_id = int(u_a.artista.id)
        tiempo_escuchado = int(u_a.tiempo_escuchado)

        PrefsUsuarios.setdefault(usuario_id, {})
        PrefsUsuarios[usuario_id][artista_id] = tiempo_escuchado
    print(PrefsUsuarios)
    # PrefsUsuarios = {'usuarioId0': {'artistaId0':tiempo_escuchado, 'artistaId1':tiempo_escuchado},
    #                  'usuarioId0': {'artistaId0':tiempo_escuchado, 'artistaId1':tiempo_escuchado},...}

    shelf['PreferenciasUsuarios'] = PrefsUsuarios
    shelf.close()

def infoUsuario(request):
    if request.method == 'GET':
        form=FormularioUsuario(request.GET)
        if form.is_valid():
            usuario_id = form.cleaned_data['usuario_id']
            print(usuario_id)
            shelf = shelve.open("dataRS.dat")
            prefs_usuarios = shelf['PreferenciasUsuarios']
            shelf.close()
            artistas = prefs_usuarios[usuario_id]
            artistas_escuchados = []
            for a_id, seg in artistas.items():
                artista = Artista.objects.get(pk=a_id)
                tiempo_escuchado = seg
                artistas_escuchados.append((artista, tiempo_escuchado))

            return render(request, 'info_usuario.html', {'artistas_escuchados':artistas_escuchados})

    form=FormularioUsuario()
    return render(request, 'formulario_artistas_usuario.html', {'form':form})

