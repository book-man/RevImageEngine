from __future__ import unicode_literals

## Python 2.7 compatibility
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
#from django.contrib.auth.models import User

from picklefield.fields import PickledObjectField

import datetime
import json


@python_2_unicode_compatible
class Image(models.Model):
    img_id = models.IntegerField(default=-1)
    img_file = models.ImageField(upload_to=None)
    img_features = PickledObjectField(default=0)

    def __str__(self):
        return self.img_file.name


@python_2_unicode_compatible
class UploadedImage(models.Model):
    up_file = models.ImageField(upload_to='uploaded_images/uploads')
    up_features = PickledObjectField(default=0)

    def __str__(self):
        return self.up_file.name


@python_2_unicode_compatible
class MostSimilarImages(models.Model):
    sim_uploaded_image = models.ForeignKey(UploadedImage,related_name='uploaded_image_most_sim',on_delete=models.CASCADE,null=True,blank=True)
    sim_top_n = PickledObjectField(default='') ##list of ordered pks

    def __str__(self):
        return 'top sim'




# # Create your models here.
# class Uploads(models.Model):
#     #up_user = models.ForeignKey(User, related_name='up_user',on_delete=models.SET_NULL,null=True,blank=True)
#     up_image = models.ImageField(upload_to='uploaded_images/uploads/')#,null=True,blank=True)
#     up_features = PickledObjectField(default=-1)
#     up_created_date = models.DateTimeField(auto_now_add=True,null=True,blank=True)

# class ImageDataset(model.Models):
#     im_image = models.ImageField(upload_to='uploaded_images/dataset/')
#     im_features = PickledObjectField(default=-1)
#     im_created_date = models.DateTimeField(auto_now_add=True,null=True,blank=True)

