from django.urls import path
from .views import NextOfKinDetailView, NextOfKinListView
from .views import   UnidentifiedBodyListView, UnidentifiedBodyDetailView

"""Unidentified Body URLs & Nextofkin URLs"""
urlpatterns = [
    
    path('unidentified_bodies/', UnidentifiedBodyListView.as_view(), name='unidentified_body_list_view'),
    path('unidentified_bodies/<int:pk>/', UnidentifiedBodyDetailView.as_view(), name='unidentified_body_detail_view'),

    
    path('nextofkin/<int:pk>/', NextOfKinDetailView.as_view(), name='nextofkin-detail'),
    path('nextofkin/', NextOfKinListView.as_view(), name='nextofkin-list')
]