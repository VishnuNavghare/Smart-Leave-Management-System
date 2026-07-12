from django.urls import path
from . import views

urlpatterns = [

    # Home
    path("", views.home, name="home"),

    # Authentication
    path("register/", views.register, name="register"),
    path("login/", views.login_page, name="login"),
    path("logout/", views.logout_page, name="logout"),

    # Dashboard
    path("dashboard/", views.dashboard, name="dashboard"),

    # Leave
    path("apply_leave/", views.apply_leave, name="apply_leave"),
    path("my_leave/", views.my_leave, name="my_leave"),

    # Profile
    path("profile/", views.profile, name="profile"),
    path("edit_profile/", views.edit_profile, name="edit_profile"),

]