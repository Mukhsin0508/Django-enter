from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class HomePageView(TemplateView): 
    template_name = "home.html"

class AboutPageView(TemplateView):
    template_name = "about.html"

class ContactPageView(TemplateView):
    template_name = "contact.html"

class BasePageView(TemplateView):
    template_name = "base.html"

class BlogsPageView(TemplateView):
    template_name = "blogs.html"
 
