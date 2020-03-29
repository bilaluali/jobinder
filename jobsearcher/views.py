from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
import json
import random

from jobsearcher.models import *
from jobsearcher.decorators import ajax_required


# Create your views here.
from django.urls import reverse
from django.utils import timezone

from jobsearcher.forms import CompanyForm, ApplicantForm, JobOfferForm



def index(request):
    return render(request, 'index.html')


def index_company(request):
    return render(request, 'index_company.html')


def is_signed(request):
    if request.user.is_authenticated:
        return redirect(reverse('jobsearcher:index'))
    return False


def sign_in(request):
    is_already_signed = is_signed(request)

    if is_already_signed is not False:
        return is_already_signed

    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                do_login(request, user)
                user_type = User.objects.get(username=request.user.username)

                # First_name is not a common field.
                if user_type.first_name:
                    return redirect(reverse('home'))
                else:
                    return redirect(reverse('home_company'))
    else:
        form = AuthenticationForm()

    args = {'form': form}
    return render(request, 'sign/sign_in.html', args)


def sign_up_company(request):
    is_already_signed = is_signed(request)

    if is_already_signed is not False:
        return is_already_signed

    if request.method == 'POST':
        form = CompanyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('home_company'))

    else:
        form = CompanyForm()

    args = {'form': form}
    return render(request, 'sign/sign_up_company.html', args)


def sign_up_applicant(request):
    is_already_signed = is_signed(request)

    if is_already_signed is not False:
        return is_already_signed

    if request.method == "POST":
        form = ApplicantForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            form.save_m2m()
            return redirect(reverse('home'))
    else:
        form = ApplicantForm()

    args = {'form': form}
    return render(request, 'sign/sign_up_applicant.html', args)


# Function to load themes based on scope election in applicant form.
def load_themes(request):
    scope_id = request.GET.get('scope')
    themes = Theme.objects.filter(Q(scope__id=scope_id)).order_by('name').values()
    return JsonResponse({"themes": list(themes)})


def sign_out(request):
    do_logout(request)
    return redirect('/')


def isajax_req(request):
    return request.headers.get('X-Requested-With') == 'XMLHttpRequest'


@login_required()
def show_matches(request):
    company = get_object_or_404(Company, Q(id=request.user.id))
    matches = get_company_matches(request)
    context = {'company': company,
               'matches': matches,
               'isajax': True if isajax_req(request) else False}

    return render(request, 'profile_company/profile_matches.html', context)


def get_company_matches(request):
    all_likes_of_company = Choice.objects.filter(company__id=request.user.id, jobOffer=None, choice=True)
    matches = []
    for like_choice in all_likes_of_company:
        applicant_liked_by_company = like_choice.applicant
        if Choice.objects.filter(applicant_id=applicant_liked_by_company,
                                 jobOffer__company_id=request.user.id, choice=True).exists():
            matches.append(applicant_liked_by_company)
    return matches


@login_required()
def show_joboffers(request):
    joboffers_list = JobOffer.objects.filter(Q(last_modified__lte=timezone.now()) & Q(company__id=request.user.id)).order_by('-last_modified')
    company = get_object_or_404(Company, Q(id=request.user.id))
    context = {'joboffers_list': joboffers_list,
               'company':company,
               'isajax': True if isajax_req(request) else False}

    return render(request, 'profile_company/profile_joboffers.html', context)


@login_required()
def joboffer_create(request):

    if request.method == "POST":
        form = JobOfferForm(request.POST)
        curr_user = get_object_or_404(Company, Q(id=request.user.id))

        if form.is_valid():
            instance = form.save(commit=False)
            instance.company = curr_user
            instance.save()

            return redirect(reverse('jobsearcher:company_profile_joboffers'))

    else:
        form = JobOfferForm()

    args = {'form': form}
    return render(request, 'profile_company/joboffer_form.html', args)


@login_required()
def joboffer_edit(request, pk):
    joboffer = get_object_or_404(JobOffer, Q(pk=pk) & Q(company__id=request.user.id))

    if request.method == 'POST':
        form = JobOfferForm(request.POST, instance=joboffer)
        curr_user = get_object_or_404(Company, Q(id=request.user.id))

        if form.is_valid():
            instance = form.save(commit=False)
            instance.company = curr_user
            instance.save()
            return redirect(reverse('jobsearcher:company_profile_joboffers'))

    else:
        form = JobOfferForm(instance=joboffer)

    args = {'form': form}
    args['isajax'] = True if isajax_req(request) else False
    return render(request, 'profile_company/joboffer_form.html', args)


@login_required()
def joboffer_delete(request, pk):
    joboffer = get_object_or_404(JobOffer, Q(pk=pk) & Q(company__id=request.user.id))
    joboffer.delete()
    return redirect(reverse('jobsearcher:company_profile_joboffers'))


@login_required()
def company_info_edit(request, pk):
    company = get_object_or_404(Company, Q(pk=pk) & Q(id=request.user.id))

    if request.method == 'POST':
        form = CompanyForm(request.POST, request.FILES, instance=company)
        if form.is_valid():
            form.save()

            # Re-Login because of password update.
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)

            if user is not None:
                do_login(request, user)
            return redirect(company.get_absolute_url_edit())
    else:
        form = CompanyForm(instance=company)

    args = {'form': form, 'company': company}
    args['isajax'] = True if isajax_req(request) else False
    return render(request, 'profile_company/company_form.html', args)


@login_required()
def show_company_insights(request):
    company = get_object_or_404(Company, Q(id=request.user.id))
    likes = Choice.objects.filter(company__id=request.user.id, jobOffer=None, choice=True)
    nopes = Choice.objects.filter(company__id=request.user.id, jobOffer=None, choice=False)
    context = {'company': company,
               'likes': likes,
               'nopes': nopes,
               'isajax': True if isajax_req(request) else False}

    return render(request, 'profile_applicant/profile_insights.html', context)


@login_required()
def show_applicant_matches(request):
    applicant = get_object_or_404(Applicant, Q(id=request.user.id))
    matches = get_applicant_matches(request)
    print(matches)
    context = {'applicant': applicant,
               'matches': matches,
               'isajax': True if isajax_req(request) else False}

    return render(request, 'profile_applicant/profile_matches.html', context)



def get_applicant_matches(request):
    all_likes_of_applicant = Choice.objects.filter(applicant__id=request.user.id, company=None, choice=True)
    matches = []
    for jobOffer_liked in all_likes_of_applicant:
        company_liked_by_applicant = jobOffer_liked.jobOffer.company
        if Choice.objects.filter(applicant__id=request.user.id, company=company_liked_by_applicant,
                                 jobOffer=None, choice=True).exists():
            matches.append((jobOffer_liked.jobOffer, company_liked_by_applicant))

    return matches


@login_required()
def applicant_info_edit(request, pk):
    applicant = get_object_or_404(Applicant, Q(pk=pk) & Q(id=request.user.id))

    if request.method == "POST":
        form = ApplicantForm(request.POST, request.FILES, instance=applicant)

        if form.is_valid():
            form.save()
            form.save_m2m()

            # Re-login because of password update
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)

            if user is not None:
                do_login(request, user)
            return redirect(applicant.get_absolute_url_edit())

    else:
        form = ApplicantForm(instance=applicant)

    args = {'form': form,
            'applicant': applicant,
            'isajax': True if isajax_req(request) else False}
    return render(request, 'profile_applicant/applicant_form.html', args)


@login_required()
def show_applicant_insights(request):
    applicant = get_object_or_404(Applicant, Q(id=request.user.id))
    likes = Choice.objects.filter(applicant__id=request.user.id, company=None, choice=True)
    nopes = Choice.objects.filter(applicant__id=request.user.id, company=None, choice=False)
    context = {'applicant': applicant,
               'likes': likes,
               'nopes': nopes,
               'isajax': True if isajax_req(request) else False}

    return render(request, 'profile_applicant/profile_insights.html', context)


@login_required
def searcher(request):
    # Username needed and verification
    is_applicant = Applicant.objects.filter(id=request.user.id).exists()
    user = query_user(request.user.id, is_applicant)
    try:
        profile = query_joboffer_profile(user.id) if is_applicant else query_applicant_profile(user.id)
    except IndexError:
        profile = None

    render_template = "joboffer.html" if is_applicant else "applicant.html"
    return render(request, "searcher/searcher_"+render_template, {'profile': profile, 'applicant':is_applicant})


def match(request):
    profile_id = request.POST.get('profile_id', None)
    print(profile_id)
    return render(request, "match/match.html")


def query_applicant_profile(id_company):
    try:
        applicants_already_chosen = Choice.objects.filter(company__id=id_company)
    except ObjectDoesNotExist:
        applicants_already_chosen = None
    if applicants_already_chosen:
        try:
            applicants = Applicant.objects.exclude(id__in=[choice.applicant.id for choice in applicants_already_chosen])
            return random.choice(applicants)
        except (IndexError, ObjectDoesNotExist):
            return None
    else:
        return random.choice(Applicant.objects.all())


def query_joboffer_profile(id_applicant):
    try:
        joboffers_already_chosen = Choice.objects.filter(applicant__id=id_applicant, company=None)
    except ObjectDoesNotExist:
        joboffers_already_chosen = None
    if joboffers_already_chosen:
        try:
            jobOffers = JobOffer.objects.exclude(id__in=[choice.jobOffer.id for choice in joboffers_already_chosen])
            return random.choice(jobOffers)
        except (IndexError, ObjectDoesNotExist):
            return None
    else:
        return random.choice(JobOffer.objects.all())


def query_user(id, applicant=True):
    return Applicant.objects.get(id=id) if applicant else Company.objects.get(id=id)


def query_joboffer(id):
    return JobOffer.objects.get(id=id)


@ajax_required
def _ajax_choice(request):
    user_pk = request.GET.get('user', None)
    profile_pk = request.GET.get('profile', None)
    like_bool = json.loads(request.GET.get('choice', 'false'))

    is_applicant = Applicant.objects.filter(id=user_pk).exists()
    usr = Applicant.objects.get(id=user_pk) if is_applicant else Company.objects.get(id=user_pk)
    # Profile can be either JobOffer if applicant answered or Applicant if company answered
    # Once saved, get the next query avoiding the previous choices
    is_match = False
    if is_applicant:
        profile = query_joboffer(profile_pk)
        Choice.objects.create(applicant=usr, jobOffer=profile, choice=like_bool)

        # Check if it is a match.
        if like_bool:
            is_match = Choice.objects.filter(company__id=profile.company.id, applicant__id=user_pk, choice=True).exists()
        return_data = {'is_match': is_match}
        next_joboffer = query_joboffer_profile(user_pk)
        if next_joboffer:
            return_data = {
                'is_applicant': is_applicant,
                'is_match': is_match,
                'id': next_joboffer.id,
                'name': next_joboffer.name,
                'company': next_joboffer.company.username,
                'city': next_joboffer.company.city,
                'theme': next_joboffer.theme.name,
                'description': next_joboffer.description
            }
            if next_joboffer.company.logo:
                return_data['photo_src'] = next_joboffer.company.logo.url
            else:
                return_data['photo_src'] = '/media/company_logos/default.png'
    else:
        profile = query_user(profile_pk)
        Choice.objects.create(applicant=profile, company=usr, choice=like_bool)

        if like_bool:
            is_match = Choice.objects.filter(company__id=user_pk, applicant__id=profile.id, choice=True).exists()
        return_data = {'is_match': is_match}
        next_applicant = query_applicant_profile(user_pk)
        if next_applicant:
            return_data = {
                'is_applicant': is_applicant,
                'is_match': is_match,
                'id': next_applicant.id,
                'name': next_applicant.username,
                'city': next_applicant.city,
                'description': next_applicant.description,
                'scope': next_applicant.scope.name,
                'themes': [theme.name for theme in next_applicant.themes.all()]
            }
            if next_applicant.photo:
                return_data['photo_src'] = next_applicant.photo.url
            else:
                return_data['photo_src'] = '/media/applicant_logos/default.png'

    return JsonResponse(return_data)
