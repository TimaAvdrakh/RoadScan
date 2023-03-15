from django.urls import path
from .views import list_create_crack

app_name = 'tracker'

urlpatterns = [
    path('', list_create_crack, name="list")
    # path('<int:pk>/', TodoDetailAPIView.as_view(), name="detail"),
]