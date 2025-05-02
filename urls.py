from django.contrib import admin
from django.urls import path, include

app_name = 'notes'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('notes.urls')),
    path('accounts/', include('accounts.urls')),
]
