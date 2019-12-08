from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views, api

urlpatterns = [
	path('', views.IndexView.as_view(), name='first_page'),

    path('api/playlist', api.PlaylistList.as_view()),
    path('api/playlist/<int:pk>/', api.PlaylistDetail.as_view()),
    path('api/song/<int:pk>/', api.SongDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)