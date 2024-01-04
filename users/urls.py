from django.urls import path
from . import views


app_name = 'users'
urlpatterns = [
    # reviive_story views
    path('register', views.register, name='register'),
    path('profile/<str:username>', views.profile, name='profile'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('manage_users/', views.user_management, name='manage_users'),
    path('change_user_role/', views.change_user_role, name='change_user_role'),

]