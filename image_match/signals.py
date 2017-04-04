
#from image_match.matcher.color

from image_match.tasks import *

from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=UploadedImage)
def get_image_features(sender,instance,created, **kwargs):
    if created:
        compute_and_save_image_features.delay(up_img_pk=instance.pk)
        print('Computed features and saved to DB for %s'%instance.pk)
    else:
        print('Model created: %s'%created)


""" Signal to compute similarity of uploaded image's features and stores image dataset features """
@receiver(post_save,sender=UploadedImage) 
def get_n_most_similar_images(sender,instance,created, **kwargs):
    up_img_pk = instance.pk
    try:
        """ Try get features/ Check if model.features != 0 """
        top10_pks = compute_n_most_similar_images(up_img_pk=up_img_pk,n=10)

        try:
            ## Obtain 
            __mostsimilarimages, created = MostSimilarImages.objects.update_or_create(sim_uploaded_image=UploadedImage.objects.get(pk=up_img_pk),
                                                        defaults={'sim_top_n':top10_pks})
        except:

    except:
        """ Do nothing """
        pass











