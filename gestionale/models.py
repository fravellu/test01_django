from django.db import models

# Create your models here.
# Sostanzialmente vengono istanziate le classi con i campi che corrisponderanno alle tabelle del DB

class Esame(models.Model):
    id = models.AutoField(primary_key=True)     # campo autoincrementale, se non inserito esplicitamente 
                                                # viene creato in automatico
    data_ora = models.DateTimeField()           # data con orario
    tipo = models.CharField(max_length=255)     # campo caratteri di lunghezza 255
    esito = models.CharField(max_length=255)
    struttura = models.CharField(max_length=255, default = 'prova')
    file_referto = models.FileField()
    cda2 = models.TextField()
    paziente = models.ForeignKey('Paziente', null= True, on_delete=models.CASCADE)
    

class Paziente(models.Model):
    codice_fiscale = models.CharField(max_length=16)
    nome = models.CharField(max_length=255)
    cognome = models.CharField(max_length=255)
