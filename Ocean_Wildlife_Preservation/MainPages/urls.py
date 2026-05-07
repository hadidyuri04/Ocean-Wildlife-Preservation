from django.urls import path
from . import views

urlpatterns = [
    path("", views.home,name="home"),
    path("get-info/",views.GetInformation,name="get_info"),
    path("Info/",views.AdminPageInfo),
    path('blogs/', views.blogs, name='blogs'),
    path('PrivatePolicy/', views.PrintPrivatePolicy, name='PrivatePolicy'),
    path('LandingPage/', views.home, name='LandingPage'),
    path('Blog1Page/',views.Blog1Page,name='Blog1Page'),
    path('Blog2Page/',views.Blog2Page,name='Blog2Page'),
    path('Blog3Page/',views.Blog3Page,name='Blog3Page')

]