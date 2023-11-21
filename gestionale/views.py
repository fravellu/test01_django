from django.http import HttpResponse, JsonResponse
import datetime

from gestionale.models import Esame, Paziente


def index(request):

    p = Paziente()
    p.codice_fiscale = 'TEST'
    p.nome = 'Mario'
    p.cognome = 'Rossi'
    p.save()

    esame = Esame()
    esame.data_ora = datetime.datetime.now()
    esame.tipo = 'test'
    esame.esito = 'esito2'
    esame.struttura = 'struttura3'
    esame.save()
    esame.save()

    return HttpResponse("Hello, world. You're at the Pollos Hermanos.")


def index2(request):
    esami = Esame.objects.all()

    result = []
    for esame in esami:
        result.append({
        'data_ora' : str(esame.data_ora),
        'tipo' : esame.tipo,
        'paziente' : esame.paziente
        })
    return JsonResponse(result, safe=False)
