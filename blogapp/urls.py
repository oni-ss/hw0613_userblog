from django.urls import path
from . import views

urlpatterns = [
    path('', views.read, name="home"),
    ### forms.py 이용X
    path('blogapp/', views.create, name="create"),
    path('update/<int:pk>', views.update, name="update"),
    path('delete/<int:pk>', views.delete, name="delete"),
    path('detail/<int:pk>', views.detail, name="detail"),
    ### forms.py 이용
    path('blogapp2/', views.blogpost, name="create2"),
] 
