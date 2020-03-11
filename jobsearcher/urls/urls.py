from django.urls import path
from django.urls import reverse
from django.views.generic import TemplateView

from jobsearcher import views

app_name = "mypoints"

urlpatterns = [

    # Index Page: /jobsearcher
    path('', views.index, name='index'),


    path('company/profile/', views.company_profile, name='company_profile'),
    path('company/profile/joboffers', views.show_joboffers, name='company_profile_joboffers'),
    path('company/profile/joboffers/<int:pk>/edit', views.joboffer_detail, name='joboffer_detail'),
    path('company/profile/joboffers/<int:pk>/edit', views.edit_joboffer, name='joboffer_edit'),
]