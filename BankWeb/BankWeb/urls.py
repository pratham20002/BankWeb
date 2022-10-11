from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bank.urls')),
    path('accounts/', include('allauth.urls')),
]
admin.site.site_header = "Noob DataBase"
admin.site.site_title = "DB"
admin.site.index_title = "Welcome to Noob's Bank"