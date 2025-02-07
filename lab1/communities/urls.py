from django.urls import path
from . import views

app_name = 'communities'

urlpatterns = [
    path('', views.communities_list, name="communities"),
    path('new-communities/', views.communities_new, name="new-communities"),
    path('<slug:slug>/', views.communitie_page, name="communitie_page"),
]
