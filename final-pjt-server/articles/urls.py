from django.urls import path 
from . import views 

urlpatterns=[
    path('', views.article_list_create),
    path('<int:article_pk>/', views.article_update_delete),
    # path('detail/<int:article_pk>/', views.article_detail),
    path('<int:article_pk>/comment_list_create/', views.comment_list_create),
    path('<int:comment_pk>/comment_delete/', views.comment_delete),
]