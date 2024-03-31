from django.conf.urls.static import static
from django.urls import path

from app.views import *
from game_store import settings

urlpatterns = [
    path('', AppMain.as_view(), name='main_page')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)