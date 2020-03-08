from django.urls import path
from django.urls import reverse
from django.views.generic import TemplateView

from jobsearcher import views

app_name = "mypoints"

urlpatterns = [

    # Index Page: /jobsearcher
    path('', views.index, name='index'),
    path('profile/', TemplateView.as_view(template_name='profile/profile_detail.html'), name='company_profile'),

]