from image_match.matcher.color_descriptor import *
from image_match.models import *
import glob
import cv2

dataset_path = '/home/nickm/Django_Projects/image_engine/uploaded_images/dataset/jpg/'
cd = ColorDescriptor((8, 12, 3))

for imagePath in glob.glob(dataset_path + "/*.jpg"):
        ## Extract the image ID (i.e. the unique filename) from the image
        ## path and load the image itself
        imageID = imagePath[imagePath.rfind("/") + 1:]
        print('Image ID: ', imageID)

        img_id = int(imageID.replace(".jpg",''))
        
        image = cv2.imread(imagePath)
     
        ## Describe the image
        features = cd.describe(image)
        
        ## Save the features to db
        __image, created = Image.update_or_create( img_id=img_id,
                                                defaults = {
                                                    "img_file":imagePath,
                                                    "img_features":features
                                                },)
        if created:
            print(created)
