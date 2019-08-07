from django.urls import path

from . import views

urlpatterns = [
    path('', views.bakra_home, name='bakra_home'),
    path('name:<slug:name>/id:<int:pk>/', views.bakra_display_name)
]
