from django.contrib import admin
from django.urls import path, include

app_name = 'notes'


urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('', include('notes.urls')),
]
