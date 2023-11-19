from django.urls import path, include
from . import views

urlpatterns = [
path("", views.index, name="index"), 
path("home", views.home, name="home"),
path("aboutme", views.aboutme, name="aboutme"),
path("signup", views.sign_up, name="sign-up"), 
path("dashboard", views.dashboard, name="dashboard"), 
path("logout", views.logout_view, name="logout"), 
path("signin", views.sign_in, name="login"),
path("projects", views.projects, name="projects"),

]