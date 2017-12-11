from django.conf.urls import url

from .views import HomeView

urlpatterns = [
	url(r'^$', HomeView.as_view(), name='index'),
	url(r'^trail_conditions/', HomeView.as_view(), name='index'),
]