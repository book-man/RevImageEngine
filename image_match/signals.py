
#from image_match.matcher.color

from image_match.tasks import *
from image_match.models import *

from django.db.models.signals import post_save
from django.dispatch import receiver

""" Signal to compute uploaded images features """
@receiver(post_save, sender=UploadedImage)
def get_image_features(sender,instance,created, **kwargs):
    if created:
        print('Model created: %s'%created)
        compute_and_save_image_features.delay(up_img_pk=instance.pk)
        print('Computed features and saved to DB for %s'%instance.pk)
        #get_n_most_similar_images.delay(up_img_pk=instance.pk)
    else:
        print('Model created: %s'%created)
        #get_n_most_similar_images.delay(up_img_pk=instance.pk)


# """ Signal to compute similarity of uploaded image's features and stores image dataset features """
# # @receiver(post_save,sender=UploadedImage) 
# def get_n_most_similar_images(up_img_pk):
#     try:
#         ## Try get features or check if model.features != 0 
#         top10_pks = compute_n_most_similar_images(up_img_pk=up_img_pk,n=10)
#         print("Computed top 10")
#         print("pks are %s"%top10_pks)

#         if(type(top10_pks) is list):
#             try:
#                 ## Obtain most similar images 
#                 __mostsimilarimages, created = MostSimilarImages.objects.update_or_create(sim_uploaded_image=UploadedImage.objects.get(pk=up_img_pk),
#                                                                                             defaults={'sim_top_n':top10_pks},)
#                 print("Saved top 10 pks, mostsimilarimages model was created: %s"%created)
#             except:
#                 print("Failed to save MostSimilarImages")
#         else:
#             print("mostsimilarmodel not created as type not list")
#             pass
#     except:
#         """ Do nothing """
#         print("Did not compute most similar")
#         pass











