from django.urls import path
from.import views
urlpatterns=[
    path('',views.index,name='index'),
    path('view_leave',views.view_leave,name='view_leave'),
    path('leave/edit/<int:leave_id>/', views.update_view_leave, name='update_view_leave'),
     path('leave/delete/<int:leave_id>/', views.delete_leave, name='delete_leave'),  # Add this line
]
