from __future__ import absolute_import, unicode_literals 

import sys
reload(sys)
sys.getdefaultencoding() ## Is currently 'ascii'
sys.setdefaultencoding('utf8')

## Celery requirements
from celery import shared_task, task

from .models import *
from .matcher.color_descriptor import ColorDescriptor
import cv2
import os

@task(name="compute_and_save_image_features")
def compute_and_save_image_features(up_img_pk):
    up_img = UploadedImage.objects.get(pk=up_img_pk)
    parent_dir = os.getcwd()
    up_file_path = str(up_img.up_file.name)

    print('file path: ',str(parent_dir+'/uploaded_images/'+up_file_path))

    cd = ColorDescriptor((8,12,3))
    try:
        image = cv2.imread(str(parent_dir+'/'+'uploaded_images/'+up_file_path)) ## problem in models.py??
        if(image is None):
            print("No image returned")
    except:
        print("failed to read in image: %s"%up_file_path)

    try:
        features = cd.describe(image)
        print('Features type: %s'%type(features))
    except:
        print("Failed to obtain image features")

    try:
        up_img.up_features = features
        up_img.save()
    except:
        print('Failed to save features to database')


@task(name='compute_n_most_similar_images')
def compute_n_most_similar_images(up_img_pk, n):
    ## load uploaded image features
    up_img = UploadedImage.objects.get(pk=up_img_pk)
    up_features = up_img.up_features

    ## load all features of dataset image 
    image_feature_set = [(image.pk, image.img_features) for image in Image.objects.all().order_by('pk')] 

    results = {}
    for img_feature in image_feature_set:
        results[img_feature[0]] chi2_distance(img_feature[1],up_features)

    ## Sort results so most similar (smallest distance) images are first
    ## Note: the pk and the features are swapped around before being sorted
    results = sorted([(v,k) for (k,v) in results.items()])

    ## Return list of top 10 pks
    top_n_results = results[:n]
    list_of_pks = [k for (v,k) in results]
    return list_of_pks


def chi2_distance(histA,histB,eps=1e-10):
    d = 0.5*sum([((a-b)**2)/(a+b+eps) for (a,b) in zip(histA,histB)])
    return d

