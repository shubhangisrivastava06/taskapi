
from django.contrib import admin
from django.urls import path,include
from Api import views
from rest_framework import routers
router =routers.DefaultRouter()

router.register('task', views.TaskViews)
router.register('tasktraker', views.TaskTrackerView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('mail/', views.mail, name='mail'),
]
