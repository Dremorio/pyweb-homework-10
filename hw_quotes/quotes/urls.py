from django.urls import path

from . import views


urlpatterns = [
    path('', views.main, name="root"),
    path('<int:page>', views.main, name="root_paginate"),
    path('author/<str:author>/', views.AuthorView.as_view(), name='author'),
    path('tag/<str:tag>/', views.QuotesByTagView.as_view(), name='quotes_by_tag')
]
