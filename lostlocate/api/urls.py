from django.urls import path
from . import views


urlpatterns =[
path('police_stations/', views.PoliceStationListView.as_view(), name='police_station_list_view'),
path('police_stations/<int:id>/', views.PoliceStationDetailView.as_view(), name='police_station_detail_view'),
path('mortuaries/', views.MortuaryListView.as_view(), name='mortuary_list_view'),
path('mortuaries/<int:id>/', views.MortuaryDetailView.as_view(), name='mortuary_detail_view'),
path('police_officers/', views.PoliceOfficerListView.as_view(), name='police_officer_list_view'),
path('police_officers/<int:id>/', views.PoliceOfficerDetailView.as_view(), name='police_officer_detail_view'),
]