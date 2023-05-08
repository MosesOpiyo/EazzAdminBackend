import debug_toolbar
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
    path('Authentication/', include("Authentication.urls")),
    path('RevenueRecords/', include("RevenueRecords.urls")),
    path('ReceiptGeneration/',include("ReceiptGeneration.urls")),
    path('Products/',include('Products.urls')),
    path('Employee/',include('Employees.urls')),
    path('Notifications/',include('Notifications.urls'))
]
