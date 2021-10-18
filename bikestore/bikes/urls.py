from django.urls import path

from . import views


urlpatterns = [
    path('details/',views.bike_page,name='bikepage')
]