from django.urls import path
from .views import HomePageView, AboutPageView, ContactPageView, BasePageView, BlogsPageView


urlpatterns = [
    path('blogs/', BlogsPageView.as_view(), name = "Blogs"),
    path('base/', BasePageView.as_view(), name = 'Base'),
    path('contact/', ContactPageView.as_view(), name = 'Contact'),
    path('about/', AboutPageView.as_view(), name = 'About'),
    path('', HomePageView.as_view(), name = "Home"), 
     

]