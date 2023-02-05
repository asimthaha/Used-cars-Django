from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    path("", views.base, name="base"),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_view, name='base'),
    path("home", views.home, name="home"),
    path("add_cars", views.add_cars, name="add_cars"),
    path('home', views.del_cars, name="del_cars"),
    path("up_cars", views.update_cars, name="up_cars"),
    path("del_cars", views.del_cars, name="del_cars"),
    path("message_user/<int:car_id>", views.message_user, name="message_user"),

]
