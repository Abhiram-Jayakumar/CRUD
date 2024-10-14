from django.urls import path

from Vlog import views




app_name = 'Vlog'

urlpatterns = [

        path('Vlog_written/', views.Vlog_written, name='Vlog_written'),
        path('add/', views.add_vlog, name='add_vlog'),
        path('vlogs/', views.vlog_list, name='vlog_list'),

]