from django.urls import path

from tracker import views

app_name = 'tracker'

urlpatterns = [
    path('', views.RoadCrackListAPIView.as_view()),
    path('policebump', views.PoliceBumpListAPIView.as_view())
]
