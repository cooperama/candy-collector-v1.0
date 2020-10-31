from django.urls import path
from . import views

urlpatterns = [
    # Static
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # Candy
    path('candy/', views.candy_index, name='candy_index'),
    # Seller(user)
    path('profile/', views.profile, name='profile'),
    path('accounts/signup/', views.signup, name='signup'),

]