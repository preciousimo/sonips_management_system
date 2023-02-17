from django.urls import path

from .views import (
    ParentCreateView,
    ParentDeleteView,
    ParentDetailView,
    ParentListView,
    ParentUpdateView,
)

urlpatterns = [
    path("list/", ParentListView.as_view(), name="parent-list"),
    path("<int:pk>/", ParentDetailView.as_view(), name="parent-detail"),
    path("create/", ParentCreateView.as_view(), name="parent-create"),
    path("<int:pk>/update/", ParentUpdateView.as_view(), name="parent-update"),
    path("<int:pk>/delete/", ParentDeleteView.as_view(), name="parent-delete"),
]