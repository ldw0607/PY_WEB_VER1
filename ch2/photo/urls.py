from django.conf.urls import url
from photo.views import *

urlpatterns = [

    url(r'^$', AlbumLV.as_view(), name='index'),

]