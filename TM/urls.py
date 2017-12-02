from django.conf.urls import url
from TM.views import index
# from swint.models import Article, Category

urlpatterns = [
    url(r'^$', index, name='index-view'),
]
