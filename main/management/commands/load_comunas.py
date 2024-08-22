'''
import csv
from django.core.management.base import BaseCommand
from main.models import Comuna

#se ejecuta usando python manage.py test_client

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        archivo = open('data/comunas.csv', 'r')
        reader = csv.reader(archivo, delimiter=';') #va leer el archivo csv y cree una comuna
        next(reader) #se salta la primera linea
        for fila in reader:
                Comuna.objects.create(nombre=fila[0], cod=fila[1], region_id=fila[3])
'''
import csv
from django.core.management.base import BaseCommand
from main.models import Comuna

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        with open('data/comunas.csv', 'r', encoding='utf-8') as archivo:  # Especificar la codificación
            reader = csv.reader(archivo, delimiter=';')
            next(reader)  # Saltar la primera línea (cabecera)

            for fila in reader:
                try:
                    Comuna.objects.create(
                        nombre=fila[0],
                        cod=fila[1],
                        region_id=fila[3]  # Asegúrate de que este ID sea válido
                    )
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Error al crear Comuna: {e}"))

        self.stdout.write(self.style.SUCCESS('Comunas cargadas exitosamente'))
