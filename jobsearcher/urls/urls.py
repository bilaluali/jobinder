from django.urls import path
from django.urls import reverse
from django.views.generic import TemplateView

from jobsearcher import views

app_name = "mypoints"

urlpatterns = [

    # Index Page
    path('', views.index, name='index'),
    path('company/', views.index_company, name='index_company'),

    # Profile Options
    path('company/profile/matches', views.show_matches, name='company_profile_matches'),
    path('company/profile/joboffers', views.show_joboffers, name='company_profile_joboffers'),
    #path('company/profile/information', views.show_info, name='company_profile_information'),


    # JobOffer
    path('company/profile/joboffers/create', views.joboffer_create, name='joboffer_create'),
    path('company/profile/joboffers/<int:pk>/edit', views.joboffer_edit, name='joboffer_edit'),
    path('company/profile/joboffers/<int:pk>/delete', views.joboffer_delete, name='joboffer_delete'),


    # Informartion
    path('company/profile/information/<int:pk>/edit', views.company_info_edit, name='company_profile_info_edit'),

]