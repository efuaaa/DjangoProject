from django.urls import path

from . import views

urlpatterns = [

    # path('', views.home, name = 'home'),
    path('login', views.login, name = 'login'),
    path('addNew', views.addNew , name = 'addNew'),
    path('members', views.members , name = 'members'),
  

]