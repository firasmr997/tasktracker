from django.urls import path
from .views import *
urlpatterns = [
    path("", home, name="home"),
    path("login/", login_view, name="login_view"),
    path("logout/", logout_user, name="logout_user"),
    path("register", register, name="register"),
    path("manager", admin, name="manager"),
    path("employee", employer, name="employee"),
    path("addTask", addTask, name="addTask"),
    path("addEmployee", addEmployee, name="addEmployee")


]