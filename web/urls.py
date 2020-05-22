from django.urls import path

from .views import basic

urlpatterns = [
	path("", basic.IndexView.as_view())
]
