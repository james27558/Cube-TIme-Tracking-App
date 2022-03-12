from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('addTime', views.addAttempt, name='addTime'),
    path('addFileOfTimes', views.addFileOfTimes, name='addFileOfTimes'),
    path('base', views.base, name='base'),
    path('addTimes', views.addTimesPage, name='addTimes'),
    path('stats', views.statsPage, name='stats'),
    path('deleteAllRecords/<int:confirm>', views.deleteAllRecordsPage, name='deleteAll')
]