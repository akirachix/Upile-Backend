from django.urls import path
from .views import MissingPersonDetailView, MissingPersonListView
from . import views



urlpatterns=[

    path('missing_persons/', MissingPersonListView.as_view(), name='missing_person_list_view'),
    path('missing_persons/<int:id>/', MissingPersonDetailView.as_view(), name='missing_person_detail_view'),
    path('police_stations/', views.PoliceStationListView.as_view(), name='police_station_list_view'),
    path('police_stations/<int:id>/', views.PoliceStationDetailView.as_view(), name='police_station_detail_view'),
    path('mortuaries/', views.MortuaryListView.as_view(), name='mortuary_list_view'),
    path('mortuaries/<int:id>/', views.MortuaryDetailView.as_view(), name='mortuary_detail_view'),
    path('police_officers/', views.PoliceOfficerListView.as_view(), name='police_officer_list_view'),
    path('police_officers/<int:id>/', views.PoliceOfficerDetailView.as_view(), name='police_officer_detail_view'),
    path('mortuary_staff/', views.MortuaryStaffListView.as_view(), name='mortuary_staff_list_view'),
    path('mortuary_staff/<int:id>/', views.MortuaryStaffDetailView.as_view(), name='mortuary_staff_detail_view'),
    path('unidentified_bodies/', views.UnidentifiedBodyListView.as_view(), name='unidentified_body_list_view'),
    path('unidentified_bodies/<int:pk>/', views.UnidentifiedBodyDetailView.as_view(), name='unidentified_body_detail_view'),
    path('nextofkin/<int:pk>/', views.NextOfKinDetailView.as_view(), name='nextofkin-detail'),
    path('nextofkin/', views.NextOfKinListView.as_view(), name='nextofkin-list')
]
