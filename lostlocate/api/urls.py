from django.urls import path
from .views import (
     MortuaryStaffListView, MortuaryStaffDetailView,
     PoliceStationListView, PoliceStationDetailView,
     MortuaryListView, MortuaryDetailView,
     PoliceOfficerListView, PoliceOfficerDetailView,
)

urlpartens=[
    
path('mortuary-staff/', MortuaryStaffListView.as_view(), name='mortuary_staff_list_view'),
path('mortuary-staff/<int:id>/', MortuaryStaffDetailView.as_view(), name='mortuary_staff_detail_view'),
path('police-stations/', PoliceStationListView.as_view(), name='police_station_list_view'),
path('police-stations/<int:id>/', PoliceStationDetailView.as_view(), name='police_station_detail_view'),
path('mortuaries/', MortuaryListView.as_view(), name='mortuary_list_view'),
path('mortuaries/<int:id>/', MortuaryDetailView.as_view(), name='mortuary_detail_view'),
path('police-officers/', PoliceOfficerListView.as_view(), name='police_officer_list_view'),
path('police-officers/<int:id>/', PoliceOfficerDetailView.as_view(), name='police_officer_detail_view'),

]
