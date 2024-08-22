'''
import csv
from django.core.management.base import BaseCommand
from main.models import Region

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        archivo = open('data/comunas.csv', 'r', encoding='utf-8')
        reader =csv.reader(archivo, delimiter=';')
        next(reader) 
        nombre_regiones = []
        for fila in reader:
            if fila in reader:
                if fila[2] not in nombre_regiones:
                    Region.objects.create(nombre=fila[2], cod=fila[3]) #buscara en el data de comunas el nombre y el codigo
                    nombre_regiones.append(fila[2])
        print(nombre_regiones)

#cargar primero las regiones, luego comunas, users, inmuebles
'''
import csv
from django.core.management.base import BaseCommand
from main.models import Region

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        nombre_regiones = []

        with open('data/comunas.csv', 'r', encoding='utf-8') as archivo:
            reader = csv.reader(archivo, delimiter=';')
            next(reader)  # Saltar la cabecera si la hay
            
            for fila in reader:
                nombre_region = fila[2]
                codigo_region = fila[3]

                if nombre_region not in nombre_regiones:
                    Region.objects.create(nombre=nombre_region, cod=codigo_region)
                    nombre_regiones.append(nombre_region)

        print(nombre_regiones)
