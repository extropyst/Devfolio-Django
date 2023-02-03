from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

import requests
import json

TREFLE_API_TOKEN = '-4GeatwCRGmaD5d8CfvrnxoiMd_aObLSJsMFxxFKAu8'
plants_endpoint = 'https://trefle.io/api/v1/plants?token=' + TREFLE_API_TOKEN



# Create your models here.

def user_directory_path(instance, filename):

    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)



class Plant(models.Model):
    common_name = models.CharField(max_length=255)
    scientific_name = models.CharField(max_length=255)
    bibliography = models.CharField(max_length=255)
    image_url = models.URLField()
    # imagen_file = models.FileField(
    #     upload_to=user_directory_path+'% Y/% m/% d/', max_length=254)


# class User(AbstractUser):
#     pass



response = requests.get(plants_endpoint)
data = response.json()

plant_list = []
for plant in data['data']:
    plant_list.append({
    'common_name': plant.get('common_name'),
    'scientific_name': plant.get('scientific_name'),
    'bibliography': plant.get('bibliography'),
    'image_url': plant.get('image_url'),
    # 'year': plant.get('year')
    })

for plant_dict in plant_list:
    Plant.objects.create(
    common_name=plant_dict['common_name'],
    scientific_name=plant_dict['scientific_name'],
    bibliography=plant_dict['bibliography'],
    image_url=plant_dict['image_url'],
    # price=plant_dict['year'],
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

