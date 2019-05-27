from django.urls import path

from pdf_app import views

urlpatterns = [
    path('', views.cv_view, name='cv'),
]
