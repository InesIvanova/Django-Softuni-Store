from django.urls import path, re_path
from . import views

urlpatterns =[
    path('owner/<int:owner_id>/', views.owner_animals, name='owner'),
    path('', views.index, name='initial'),
    path('all/<int:animal_id>/', views.AnimalList.as_view(), name='animal'),
    path('dogs/', views.all_dogs, name='dogs'),
    path('cats/', views.all_cats, name='cats'),
    re_path('^get_animal/$', views.search, name='search'),
    re_path('^create/$', views.create_animal_form, name='create'),
    re_path('^edit/$', views.update_animal, name='create'),
    re_path('^all/(?P<animal_id>\d+)*/*$', views.read_animals_data, name='all'),
    path('delete/<int:animal_id>/', views.delete_animal, name='delete'),

]