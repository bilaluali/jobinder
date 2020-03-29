from django.urls import path
from jobsearcher import views

app_name = "jobsearcher"

urlpatterns = [

    # Index Page
    path('', views.index, name='index'),
    path('company/', views.index_company, name='index_company'),



    path('company/profile/matches', views.show_matches, name='company_profile_matches'),
    path('company/profile/joboffers', views.show_joboffers, name='company_profile_joboffers'),
    path('company/profile/information/<int:pk>/edit', views.company_info_edit, name='company_profile_info_edit'),
    path('company/profile/insights', views.show_company_insights, name='company_profile_insights'),

    # JobOffer
    path('company/profile/joboffers/create', views.joboffer_create, name='joboffer_create'),
    path('company/profile/joboffers/<int:pk>/edit', views.joboffer_edit, name='joboffer_edit'),
    path('company/profile/joboffers/<int:pk>/delete', views.joboffer_delete, name='joboffer_delete'),



    path('applicant/profile/matches', views.show_applicant_matches, name='applicant_profile_matches'),
    path('applicant/profile/information/<int:pk>/edit', views.applicant_info_edit, name='applicant_profile_info_edit'),
    path('applicant/profile/insights', views.show_applicant_insights, name='applicant_profile_insights'),

]