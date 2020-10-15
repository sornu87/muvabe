"""muvabe URL Configuration

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

from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from rest_framework.urlpatterns import format_suffix_patterns
from tender import views
from  .models import Eoi, Empresa


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
router.register(r'eoi',views.EoiViewSet)
router.register(r'empresa',views.EmpresaViewSet)

# router = DefaultRouter()
# router.register(r'snippets', views.SnippetViewSet)
# router.register(r'users', views.UserViewSet)

# router = routers.DefaultRouter()
# router.register(r'eoi', views.EoiDetail)
# router.register(r'eois', views.EoiList)


# urlpatterns = [
#     path('eoi/', views.EoiViewSet),
# ]

# urlpatterns = [
#     path('eoiList/', views.EoiList.as_view()),
#     path('eoi/<int:pk>/', views.EoiDetail.as_view()),
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)



# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]