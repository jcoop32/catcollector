from django.urls import path
from . import views

urlpatterns = [
    # no slash before path name, ex. /about/
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cats/', views.cats_list, name='cats'),
    path('cats/<int:cat_id>/', views.cat_details, name='details'),
]