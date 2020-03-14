"""jobinder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView, TemplateView

import jobsearcher


urlpatterns = [
    path('admin/', admin.site.urls),


    path('', RedirectView.as_view(pattern_name='jobsearcher:index'), name='home'),
    path('jobsearcher/', include(('jobsearcher.urls', 'jobsearcher'), namespace='jobsearcher')),


    path('company/', RedirectView.as_view(pattern_name='jobsearcher:index_company'), name='home_company'),
    path('company/signup/', jobsearcher.views.sign_up_company, name='sign_up_company'),

    path('signup/', jobsearcher.views.sign_up_applicant, name='sign_up_applicant'),
    path('signup_done/', TemplateView.as_view(template_name='sign/signup_done.html'), name='signup_done'),
    path('signin/', jobsearcher.views.sign_in, name='sign_in'),
    path('signout/', jobsearcher.views.sign_out, name='sign_out'),

    # Path to get themes of scope via AJAX.
    path('applicant/signup/load-themes', jobsearcher.views.load_themes, name='load_themes'),

]
