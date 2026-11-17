from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name="home"),
    path('o-nas/', views.about_view, name="about"),
    path('pytania/', views.faq_view, name="faq"),
    path('prywatnosc/', views.privacy_view, name="privacy"),
    path('regulamin/', views.tos_view, name="tos"),
    path('wydarzenie/<int:id>', views.activity_view, name="activity"),
]
