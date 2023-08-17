"""
URL configuration for AdminChange project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from rest_framework.routers import DefaultRouter
from django.urls import include, path
from django.contrib import admin
from auth_app.views import register_user, login_user, logout_user,list_users
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.routers import DefaultRouter
from task_app.views import ProjectModelViewSet, TaskModelViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="Task Management System",
        default_version='v1',
        description="Test Swagger Second app",
        terms_of_service="http://www.ourapp.com/policies/terms/",
        contact=openapi.Contact(email="contact@task.local"),
        license=openapi.License(name="Test License")
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


router = DefaultRouter()
router.register(r'api/projects', ProjectModelViewSet)
router.register(r'api/tasks', TaskModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api/auth/register/', register_user, name='register'),
    path('api/auth/users/', list_users, name='list-users'),
    path('api/auth/login/', login_user, name='login'),
    path('api/auth/logout/', logout_user, name='logout'),
    path('s/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
