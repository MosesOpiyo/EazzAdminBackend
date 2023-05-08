from django.urls import path
import Notifications.views as views

urlpatterns = [
    path("Notification/<str:name>/<int:amount>/<str:code>",views.NotificationView,name="Notification"),
    path("GetNotifications",views.getNotifications,name="Get"),
    path("DeleteNotifications",views.deleteNotifications,name="Delete"),
   
]