'''
import csv
from django.core.management.base import BaseCommand
from main.models import Comuna
from main.services import crear_inmueble
#se ejecuta usando python manage.py test_client

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        archivo = open('data/inmuebles.csv', 'r')
        reader = csv.reader(archivo, delimiter=',') #va leer el archivo csv y cree una comuna
        next(reader) #se salta la primera linea
        for fila in reader:
                crear_inmueble(fila[0], fila[1], fila[3], fila[4], fila[5], fila[6], fila[7], fila[8], fila[9], fila[10], fila[11], fila[12])
'''

import csv
from django.core.management.base import BaseCommand
from main.services import crear_inmueble


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        with open('data/inmuebles.csv', 'r') as archivo:
            reader = csv.reader(archivo, delimiter=',')
            next(reader)  # Saltar la cabecera

            for fila in reader:
                if len(fila) < 11:  # Verificar si la fila tiene al menos 13 columnas
                    self.stdout.write(self.style.ERROR(f"Fila incompleta: {fila}"))
                    continue  # Saltar a la siguiente fila si está incompleta
                
                try:
                    crear_inmueble(
                        fila[0], fila[1], fila[2], fila[3], fila[4],
                        fila[5], fila[6], fila[7], fila[8], fila[9],
                        fila[10], fila[11]
                    )
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Error al crear inmueble: {e}"))

        self.stdout.write(self.style.SUCCESS('Inmuebles cargados exitosamente'))


        
