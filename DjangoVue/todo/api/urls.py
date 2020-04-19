from django.urls import path,include
from .views import myrouter


urlpatterns = [
    path('',include(myrouter.urls)),
]