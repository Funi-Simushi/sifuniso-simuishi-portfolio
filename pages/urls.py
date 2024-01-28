from django.urls import path
from .views import HomePageView, AboutPageView, PortfolioPageView, BlogsPageView, ContactPageView

urlpatterns = [
 
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('portfolio/', PortfolioPageView.as_view(), name='portfolio'),
    path('blogs/', BlogsPageView.as_view(), name='blogs'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),
]