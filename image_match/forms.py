from django import forms
from models import UploadedImage

class UploadFileForm(forms.Form):
    ## keep the name to file as that is what dropzone is using
    file = forms.ImageField(required=True)


# class UploadFileForm(forms.ModelForm):

#     class Meta:
#         model = UploadedImage
#         fields = ['up_file']