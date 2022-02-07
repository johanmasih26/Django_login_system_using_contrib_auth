from django.urls import path
from apps.demo import views
from django.views.generic.base import TemplateView

app_name = 'demo'



urlpatterns = [
    
    path('', TemplateView.as_view(template_name = 'registration/login.html'), name="index")
]
