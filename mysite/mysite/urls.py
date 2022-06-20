from hompage.views import 홈페이지
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', 홈페이지),
]
