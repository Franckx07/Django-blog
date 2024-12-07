
from .views import *
from django.urls import path

app_name = "posts"

urlpatterns = [
    path('', BlogHome.as_view(), name="home"),
    path('create/', BlogPostCreate.as_view(), name="create"),
    path('delete/<str:slug>', BlogPostDelete.as_view(), name="delete"),
    path('edit/<str:slug>', BlogPostUpdate.as_view(), name="edit"),
    path('<str:slug>/', BlogPostDetail.as_view(), name="detail"),
]