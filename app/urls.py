from rest_framework.routers import DefaultRouter
from django.urls import path
from app import views

urlpatterns  = [
    path('Dictionary/<str:pk>',views.DictionaryDetailViewSet.as_view(),name='dictionary-detail'),
    path('Dictionary/', views.DictionaryViewSet.as_view(),name='dictionary-list'),
    path('Language', views.LanguagesViewSet.as_view(),name='language-list'),

]