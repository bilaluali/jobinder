from django.urls import path
from django.urls import reverse
from django.views.generic import TemplateView

from jobsearcher import views

app_name = "mypoints"

urlpatterns = [

    # Index Page: /jobsearcher
    path('', views.index, name='index'),
    path('company/profile/', views.company_profile, name='company_profile'),

]