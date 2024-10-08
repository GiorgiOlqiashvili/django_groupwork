from django.contrib import admin
from django.urls import path
from cars import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/', views.car_list, name='car_list'),
    path('cars/<int:pk>/', views.car_detail, name='car_detail'),
    path('cars/add/', views.add_car, name='add_car'),
]


from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

