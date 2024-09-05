from django.urls import path
from .views import (
     MortuaryStaffListView, MortuaryStaffDetailView,
)
path('mortuary-staff/', MortuaryStaffListView.as_view(), name='mortuary_staff_list_view'),
path('mortuary-staff/<int:id>/', MortuaryStaffDetailView.as_view(), name='mortuary_staff_detail_view'),