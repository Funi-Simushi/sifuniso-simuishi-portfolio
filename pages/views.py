from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class PortfolioPageView(TemplateView):
    template_name = 'portfolio.html'

class BlogsPageView(TemplateView):
    template_name = 'blogs.html'

class ContactPageView(TemplateView):
    template_name = 'contact.html'