"""blog_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from blog_api import settings

from main.views import CateryListView, PostViewSet, PostImageView

router = DefaultRouter()
router.register('posts', PostViewSet)


"""
create -> posts/ POST
list -> posts/ GET
retrive -> posts/id GET
update -> posts/id/ PUT
partial_update -> posts/id/ PATCH
destroy -> posts/id DELETE

"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('v1/api/categories/', CateryListView.as_view()),
    path('v1/api/add-image/', PostImageView.as_view()),
    path('v1/api/account/', include('account.urls')),
    path('v1/api/', include(router.urls))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
