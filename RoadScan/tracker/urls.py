from django.urls import path
import views

app_name = 'tracker'

urlpatterns = [
    path('roadcrack/', views.RoadCrackListAPIView.as_view()),
    path('policebump/', views.PoliceBumpListAPIView.as_view())
]