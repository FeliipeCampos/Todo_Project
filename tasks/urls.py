from django.urls import path
from .views import TaskList, TaskUpdate, TaskDelete, TaskComplete, NotificationList

urlpatterns = [
    path('', TaskList.as_view(), name='task-list'),
    path('<int:pk>/', TaskUpdate.as_view(), name='task-detail'),
    path('<int:pk>/delete/', TaskDelete.as_view(), name='task-delete'),
    path('<int:pk>/complete/', TaskComplete.as_view(), name='task-complete'),
    path('notifications/', NotificationList.as_view(), name='notification-list'),
]
