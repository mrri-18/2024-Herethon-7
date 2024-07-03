from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import edit_profile
app_name='profile'
urlpatterns = [
    path('', edit_profile, name='edit_profile'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
