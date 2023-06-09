from django.shortcuts import render
from django.views.generic.base import View

# Create your views here.

class LandingPageView(View):
    template_name = "index.html"
    context = {}

    def get(self, request):
        return render(request, self.template_name, self.context)
    

class AboutPageView(View):
    template_name = "about.html"
    context = {}

    def get(self, request):
        return render(request, self.template_name, self.context)
    

class ContactPageView(View):
    template_name = "contact.html"
    context = {}

    def get(self, request):
        return render(request, self.template_name, self.context)
    
