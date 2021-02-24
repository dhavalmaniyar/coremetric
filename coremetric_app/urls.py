from django.urls import include,path
from . import views
from django.views.generic import TemplateView
urlpatterns = [
    path('',views.index,name='index'),
    path('submit',views.submit,name='submit'),
    path('robots.txt',TemplateView.as_view(template_name='robots.txt', content_type="text/plain"),),
]
