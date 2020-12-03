from django.urls import path
from . import views

app_name="movies"

urlpatterns = [
    path('', views.movie_list),
    path('detail/<int:movie_pk>/', views.movie_detail),
    path('detail/<int:movie_id>/rating_list_create/', views.rating_list_create),
    path('detail/<int:rating_pk>/rating_delete/', views.rating_delete),
    path('detail/<int:movie_pk>/rating_update/', views.rating_update),
]
