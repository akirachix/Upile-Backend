from django.urls import path
from .views import MissingPersonDetailView, MissingPersonListView



urlpatterns=[

    path('missing_persons/', MissingPersonListView.as_view(), name='missing_person_list_view'),
    path('missing_persons/<int:id>/', MissingPersonDetailView.as_view(), name='missing_person_detail_view'),

]
