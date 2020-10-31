from django.urls import path, include
from . import views

urlpatterns = [
    # Static
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # Candy
    path('candy/', views.candy_index, name='candy_index'),
    # Seller(user)
    path('accounts/', include('django.contrib.auth.urls')),
]