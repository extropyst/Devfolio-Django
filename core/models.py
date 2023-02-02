from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.models import AbstractUser

import requests
import json

TREFLE_API_TOKEN = '-4GeatwCRGmaD5d8CfvrnxoiMd_aObLSJsMFxxFKAu8'
plants_endpoint = 'https://trefle.io/api/v1/plants?token=' + TREFLE_API_TOKEN



# Create your models here.


class Plant(models.Model):
    common_name = models.CharField(max_length=255)
    scientific_name = models.CharField(max_length=255)
    bibliography = models.CharField(max_length=255)
    image_url = models.URLField()


class user(AbstractUser):
    pass
    # username = models.CharField(
    #     max_length=255, verbose_name='Nombre de usuario')
    # email = models.EmailField(
    #     max_length=255, unique=True, verbose_name='Correo', help_text="Formato: username@nombredominio.extension", )
    # password = models.CharField(max_length=255, verbose_name='Contraseña')


class Carro(models.Model):
    common_name = models.CharField(max_length=255)
    scientific_name = models.CharField(max_length=255)
    bibliography = models.CharField(max_length=255)
    image_url = models.URLField()




response = requests.get(plants_endpoint)
data = response.json()

plant_list = []
for plant in data['data']:
    plant_list.append({
    'common_name': plant.get('common_name'),
    'scientific_name': plant.get('scientific_name'),
    'bibliography': plant.get('bibliography'),
    'image_url': plant.get('image_url')
    })

for plant_dict in plant_list:
    Plant.objects.create(
    common_name=plant_dict['common_name'],
    scientific_name=plant_dict['scientific_name'],
    bibliography=plant_dict['bibliography'],
    image_url=plant_dict['image_url']
    )












# COMMON_NAME = 'Common_Name'
# SCIENTIFIC_NAME = 'Scientific_Name'
# BIBLIOGRAPHY = 'Bibliography'
# IMAGE_URL = 'Image_URL'


# url = 'https://trefle.io/api/v1/plants?token=-4GeatwCRGmaD5d8CfvrnxoiMd_aObLSJsMFxxFKAu8'
# response = requests.get(url)
# data = json.loads(response.text)
# for d in data:
#     Plant.objects.create(
#         common_name=d['Common_Name'],
#         scientific_name=d['Scientific_Name'], 
#         bibliography=d['Bibliography'],
#         image_url=d['Image_URL']
#     )
# Plant.save()

# response = requests.get(plants_endpoint)
# data = response.json()

# for plant in data:
#     Plant.objects.create(
#         common_name=plant.get('common_name'),
#         scientific_name=plant.get('scientific_name'), 
#         bibliography=plant.get('bibliography'),
#         image_url=plant.get('image_url')
#     )
# Plant.save()

