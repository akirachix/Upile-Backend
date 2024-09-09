from django.urls import path
from .views import (
        MortuaryStaffListView, MortuaryStaffDetailView,
)

urlpatterns = [
    path('mortuary_staff/', MortuaryStaffListView.as_view(), name='mortuary_staff_list_view'),
    path('mortuary_staff/<int:id>/', MortuaryStaffDetailView.as_view(), name='mortuary_staff_detail_view'),
]