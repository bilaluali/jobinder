from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.utils import timezone

from jobsearcher.forms import CompanyForm, ApplicantForm, JobOfferForm
from jobsearcher.models import Company, JobOffer, Theme, Applicant, User


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
            return redirect(reverse('home'))
    else:
        form = ApplicantForm()

    args = {'form': form}
    return render(request, 'sign/sign_up_applicant.html', args)


# Function to load themes based on scope election in applicant form.
def load_themes(request):
    scope_id = request.GET.get('scope')
    themes = Theme.objects.filter(Q(scope__id=scope_id)).order_by('name')
    return render(request, 'sign/themes_dropdownlist.html', {'themes': themes})


def sign_out(request):
    do_logout(request)
    return redirect('/')


def isajax_req(request):
    return request.headers.get('X-Requested-With') == 'XMLHttpRequest'


@login_required()
def show_matches(request):
    company = get_object_or_404(Company, Q(id=request.user.id))
    context = {'company': company}
    return render(request, 'profile_company/profile_matches.html', context)


@login_required()
def show_joboffers(request):
    joboffers_list = JobOffer.objects.filter(Q(last_modified__lte=timezone.now()) & Q(company__id=request.user.id)).order_by('-last_modified')
    company = get_object_or_404(Company, Q(id=request.user.id))
    context = {'joboffers_list': joboffers_list, 'company':company}

    if isajax_req(request):
        context['isajax'] = True
    else:
        # Will render full page.
        context['isajax'] = False

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
def show_applicant_matches(request):
    applicant = get_object_or_404(Applicant, Q(id=request.user.id))
    context = {'applicant': applicant}
    return render(request, 'profile_applicant/profile_matches.html', context)


@login_required()
def applicant_info_edit(request, pk):
    applicant = get_object_or_404(Applicant, Q(pk=pk) & Q(id=request.user.id))

    if request.method == "POST":
        form = ApplicantForm(request.POST, request.FILES, instance=applicant)

        if form.is_valid():
            form.save()

            #Re-login because of password update
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)

            if user is not None:
                do_login(request, user)
            return redirect(applicant.get_absolute_url_edit())

    else:
        form = ApplicantForm(instance=applicant)

    args = {'form': form, 'applicant': applicant}
    args['isajax'] = True if isajax_req(request) else False
    return render(request, 'profile_applicant/applicant_form.html', args)