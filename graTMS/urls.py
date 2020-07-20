from django.urls import path

from . import views

app_name = 'graTMS'
urlpatterns = [
    path('', views.home, name='home'),
    path('add_coplaint/', views.add_coplaint, name='add_coplaint'),
    path('complaint/detail/<int:id>/', views.viewCompliant, name='view-complaint'),
]
