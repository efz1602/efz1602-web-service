from django.conf.urls import url

from .views import registration

urlpatterns = [
    url('register', registration, name='user-register'),
]
