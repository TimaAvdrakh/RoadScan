from django.urls import path
from .views import list_create_shops

app_name = 'tracker'

urlpatterns = [
    path('', list_create_shops, name="list")
    # path('<int:pk>/', TodoDetailAPIView.as_view(), name="detail"),
]