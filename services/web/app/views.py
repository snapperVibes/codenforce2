# from django.http import HttpResponse
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.context import RequestContext
from .forms import NameForm, MunicipalityForm
from .models import Municipality


def index(request):
    # return HttpResponse("Hello, 🌍")
    return render(request, "public/home.html",)


class CEActionRequest:

    # @staticmethod
    # def select_municipality(request):
    #     if request.method == "POST":
    #         form = NameForm(request.POST)
    #         if form.is_valid():
    #             return HttpResponseRedirect('/thanks/')
    #     else:
    #         form = NameForm()
    #         munis =  Municipality.objects.values("muniname", "municode")
    #         [print(m) for m in munis]
    #     return render(request, "public/services/CEAction/selectMunicipality.html", {'form': form} )

    @staticmethod
    def select_municipality(request):
        if request.method == "POST":
            form = MunicipalityForm(request.POST)
            if form.is_valid():
                print("yay")
                return HttpResponseRedirect('/thanks/')
        else:
            form = MunicipalityForm()
        return render(request, "public/services/CEAction/selectMunicipality.html", {'form': form})
