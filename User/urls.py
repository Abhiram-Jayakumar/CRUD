from django.urls import path

from User import views




app_name = 'User'

urlpatterns = [
        path('Index/', views.Index, name='Index'),
        path('register/', views.register_user, name='register'),
        path('users/', views.user_list, name='user_list'),
        path('users/<int:user_id>/', views.user_detail, name='user_detail'),
        path('users/update/<int:user_id>/', views.update_user, name='update_user'),
        path('users/delete/<int:user_id>/', views.delete_user, name='delete_user'),
        
        ]