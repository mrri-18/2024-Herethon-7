from django.conf import settings
from django.conf.urls.static import static

app_name='Historyapp'

from django.urls import path
from . import views

urlpatterns=[
    path('',views.record_list, name='record_list')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)