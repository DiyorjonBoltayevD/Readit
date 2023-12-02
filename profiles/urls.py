from django.urls import path

from profiles.views import profiles

app_name = 'profiles'

urlpatterns = [
    path('', profiles, name='profiles')
]
