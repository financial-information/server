from django.urls import path

from database import views

urlpatterns = [
  path('user_list/', views.userList, name='user_list')
]
