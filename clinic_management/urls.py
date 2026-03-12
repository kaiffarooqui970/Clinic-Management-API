from django.contrib import admin
from django.urls import path
from patient import views

urlpatterns = [
path('admin/', admin.site.urls),
path('api/register/', views.register_patient, name='register_patient'),
path('api/book/', views.book_appointment, name='book_appointment'),
]