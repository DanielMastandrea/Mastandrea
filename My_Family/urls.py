from django.contrib import admin
from django.urls import path
from My_Family.views import inicio
from Family.views import create_member, list_miembros

urlpatterns = [
    path('admin/', admin.site.urls),
    path("inicio/", inicio, name="inicio"),
    path("create_member/",create_member, name="Create_Member"),
    path("list_miembros/",list_miembros, name="Lista_Familia") 
]