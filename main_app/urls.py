from django.urls import path
from . import views

urlpatterns = [
    # no slash before path name, ex. /about/
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('explore_list/', views.explore_list, name='explore_list'),
    path('cats/', views.cats_list, name='cats'),
    path('cats/<int:cat_id>/', views.cat_details, name='details'),
    path('cats/create', views.CatCreate.as_view(), name='cat_create'),
    path('cats/<int:pk>/update/', views.CatUpdate.as_view(), name='cat_update'),
    path('cats/<int:pk>/delete/', views.CatDelete.as_view(), name='cat_delete'),
    path('cats/<int:cat_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('accounts/signup', views.signup, name='signup'),
    
]