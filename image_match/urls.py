from django.conf.urls import url

from . import views

app_name = 'image_match'

urlpatterns = [
    url(r'^',views.ImageCreateView.as_view(),name='home'),
    # url(r'^$','image_match.views.ImageCreateView',name='home')
    ]