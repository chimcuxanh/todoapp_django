from . import views
from django.urls import path

urlpatterns = [
    path('', views.today, name="list"),
    path('update_T/<str:pk>', views.update_task, name="update"),
    path('delete_T/<str:pk>', views.delete_task, name="delete")
]