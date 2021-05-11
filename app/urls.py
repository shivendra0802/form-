from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('check/', check, name='check'),
    # path('capfirst/', capfirst, name='capfirst'),
    # path('newlineremove/', newlineremove, name='newlineremove'),

]
