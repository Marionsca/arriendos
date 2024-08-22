'''
import csv
from django.core.management.base import BaseCommand
from main.models import Comuna
from main.services import crear_user


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        archivo = open('data/users.csv', 'r')
        reader = csv.reader(archivo, delimiter=';') #va leer el archivo csv y cree una comuna
        next(reader) #se salta la primera linea
        for fila in reader:
                crear_user(fila[0], fila[1], fila[3], fila[4], fila[5], fila[6])
'''
import csv
from django.core.management.base import BaseCommand
from main.services import crear_user

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        with open('data/users.csv', 'r', encoding='utf-8') as archivo:
            reader = csv.reader(archivo, delimiter=';')
            next(reader)  # Saltar la cabecera

            for fila in reader:
                try:
                    # Llamar a crear_user con los valores del CSV y valores por defecto para los faltantes
                    crear_user(
                        username=fila[0],
                        first_name=fila[1],
                        last_name=fila[2],
                        email=fila[3],
                        password=fila[4],
                        pass_confirm=fila[5],
                        direccion=fila[6],
                        rol='arrendatario',  # Valor por defecto
                        telefono=None       # Valor por defecto
                    )
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Error al crear usuario {fila[0]}: {e}"))

        self.stdout.write(self.style.SUCCESS('Usuarios cargados exitosamente'))
