from django.urls import path
from . import views

app_name = "link"


urlpatterns = [
    path("", views.PostCreateApi.as_view(), name="api_create"),
    path("update/<int:pk>", views.LinkUpdateApi.as_view(), name="api_update"),
    path("delete/<int:pk>", views.LinkDeleteApi.as_view(), name="api_delete"),
    path("", views.PostListApi.as_view(), name="api_list"),
    path("active/", views.ActiveLinkView.as_view(), name="active_link"),
    path("recent/", views.RecentLinkView.as_view(), name="recent_link"),
]

