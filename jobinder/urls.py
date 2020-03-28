"""jobinder URL Configuration"""
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView, TemplateView

from jobsearcher import views
from jobinder import settings


from django.conf.urls import url
from jobsearcher import views

urlpatterns = [
    path('admin/', admin.site.urls),


    path('', RedirectView.as_view(pattern_name='jobsearcher:index'), name='home'),
    path('jobsearcher/', include(('jobsearcher.urls', 'jobsearcher'), namespace='jobsearcher')),


    path('company/', RedirectView.as_view(pattern_name='jobsearcher:index_company'), name='home_company'),
    path('company/signup/', views.sign_up_company, name='sign_up_company'),

    path('signup/', views.sign_up_applicant, name='sign_up_applicant'),
    path('signup_done/', TemplateView.as_view(template_name='sign/signup_done.html'), name='signup_done'),
    path('signin/', views.sign_in, name='sign_in'),
    path('signout/', views.sign_out, name='sign_out'),

    url(r'^searcher/$', views.searcher, name='searcher'),

    url(r'^match/$', views.match, name='match'),

    # AJAX
    # Path to get themes of scope via AJAX.
    path('applicant/signup/load-themes', views.load_themes, name='load_themes'),
    url(r'^ajax_search_button/$', views._ajax_choice, name='ajax_search_button'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
