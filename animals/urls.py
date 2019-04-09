from django.urls import path, re_path
from . import views


app_name = 'animals'
urlpatterns =[
    # path('owner/<int:owner_id>/', views.owner_animals, name='owner'),
    path('', views.index, name='initial'),
    re_path('all/(?P<pk>[-\w]+)/', views.AnimalList.as_view(), name='animal'),
    re_path('details/(?P<pk>[-\w]+)/', views.AnimalDetail.as_view(), name='details'),
    re_path('update/(?P<pk>[-\w]+)/', views.AnimalUpdate.as_view(), name='update'),
    re_path('delete/(?P<pk>\d+)/', views.DeleteANimal.as_view(), name='delete'),

    # path('dogs/', views.all_dogs, name='dogs'),
    # path('cats/', views.all_cats, name='cats'),
    # re_path('^get_animal/$', views.search, name='search'),
     re_path('^create/$', views.AnimalCreate.as_view(), name='create'),
    # re_path('^edit/$', views.update_animal, name='create'),
    re_path('^all/(?P<animal_id>\d+)*/*$', views.read_animals_data, name='all'),

]