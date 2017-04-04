import sys
reload(sys)
sys.getdefaultencoding() ## Is currently 'ascii'
sys.setdefaultencoding('utf8')

from celery import task
from .models import *
from matcher.color_descriptor import ColorDescriptor

@task(name="compute_image_features")
def compute_image_features(uploadedimage_pk):
    up_img = UploadedImage.objects.get(pk=uploadedimage_pk)
    up_path = str(up_img.file.name)

    col_descript = ColorDescriptor((8,12,3))
    
