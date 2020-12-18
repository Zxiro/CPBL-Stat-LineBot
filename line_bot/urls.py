from django.urls import path
from . import views


#urlpatterns = reserved word, type = List
urlpatterns = [
    path('', views.index, name = 'Index'),
    path('callback/', views.callback), 
]