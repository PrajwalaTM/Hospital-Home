from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
	url(r'^process/',views.process,name="process"),
    url(r'^', TemplateView.as_view(template_name= "finddoctor/finddoctor.html"), name="finddoctor"),
    #url(r'^',views.display,name="finddoctor"),

    ]