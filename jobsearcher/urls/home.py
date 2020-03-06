from django.urls import path
from django.urls import reverse

from jobsearcher import views

app_name = "mypoints"

urlpatterns = [

    # Index Page: /jobsearcher
    path('', views.index, name='index'),
]