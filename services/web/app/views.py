# from django.http import HttpResponse
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.context import RequestContext
from .forms import NameForm

def index(request):
    # return HttpResponse("Hello, 🌍")
    return render(request, "public/home.html",)


class CEActionRequest:

    @staticmethod
    def select_municipality(request):
        if request.method == "POST":
            form = NameForm(request.POST)
            if form.is_valid():
                return HttpResponseRedirect('/thanks/')
        else:
            form = NameForm()
        return render(request, "public/services/CEAction/selectMunicipality.html", {'form': form} )

# class TempMuni(forms.Form):
#     # muni = forms.CharField(label="What muni?", widget=forms.Select(choices=["allegheny", "turtle creek", "cogland"]))