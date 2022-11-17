
from django.contrib import admin
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from asosiy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get-token/',obtain_auth_token),
    path('mahsulotlar/',MahsulotlarAPIView.as_view()),
    path('mijozlar/',MijozlarAPIView.as_view()),
    path('users/',UserAPIView.as_view()),
    path('sotuvchi/',SotuvchiAPIView.as_view()),

]
