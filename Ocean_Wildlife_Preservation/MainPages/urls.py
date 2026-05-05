from django.urls import path
from . import views

urlpatterns = [
    path("", views.home,name="home"),
    path("get-info/",views.GetInformation,name="get_info"),
    path("Info/",views.AdminPageInfo)
]