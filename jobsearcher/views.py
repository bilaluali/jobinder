from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.urls import reverse

from jobsearcher.forms import CompanyForm, ApplicantForm
from jobsearcher.models import Company


def index(request):
    return render(request, 'index.html')


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
                return redirect(reverse('home'))
    else:
        form = AuthenticationForm()

    args = {'form': form}
    return render(request, "sign/sign_in.html", args)


def sign_up_company(request):
    is_already_signed = is_signed(request)

    if is_already_signed is not False:
        return is_already_signed

    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('signup_done'))

    else:
        form = CompanyForm()

    args = {'form': form}
    return render(request, 'sign/sign_up_company.html', args)


def sign_up_applicant(request):
    is_already_signed = is_signed(request)

    if is_already_signed is not False:
        return is_already_signed

    if request.method == "POST":
        form = ApplicantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('signup_done'))
        else:
            print("INVALIIID")
    else:
        form = ApplicantForm()

    args = {'form': form}
    return render(request, 'sign/sign_up_applicant.html', args)


def sign_out(request):
    do_logout(request)
    return redirect('/')


@login_required(login_url='/signin/')
def company_profile(request):
    company = get_object_or_404(Company, Q(id=request.user.id))
    context = {'company': company}
    return render(request, 'profile/company_profile.html', context)
