from django.conf.urls import url

from . import views

app_name = 'image_match'

urlpatterns = [
    url(r'^',views.home,name='home'),
    url(r'^thanks/$',views.thanks,name='thanks')
    # url(r'^$','image_match.views.ImageCreateView',name='home')
    ]