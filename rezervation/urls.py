from django.urls import path, include
from .views import *

app_name = 'reservation'
urlpatterns = [

    path('admin_panel/', admin_panel_view),
    path('add_edit_plan/', add_plan_salon_ejtamaat_view, name='add_plan_salon'),
    path('delete-available-time/<int:pk>/',delete_available_time,name='delete_available_time'),
]
