from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from jobsearcher.forms import CompanyForm


def index(request):
    return render(request, 'index.html')


def is_signed(request):
    if request.user.is_authenticated:
        return redirect(reverse('jobsearcher:index'))
    return False


def sign_up(request):
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
    return render(request, 'sign/sign_up.html', args)

