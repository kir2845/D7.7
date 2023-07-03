from django.contrib import admin
from django.urls import path, include

urlpatterns = [
   path('admin/', admin.site.urls),
   path('at/', include('django.contrib.flatpages.urls')),
   # Делаем так, чтобы все адреса из нашего приложения (News_from_Ozersk/urls.py)
   # подключались к главному приложению с префиксом news/.
   path('', include('News_from_Ozersk.urls')),
#   path('articles/', include('News_from_Ozersk.urls')),
]