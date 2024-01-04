"""
URL configuration for djangoProject project.

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
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reviive/', include('reviive.urls', namespace='reviive')),
    path('reviveStoryList/', include('reviive.urls', namespace='reviveStoryList')),
    path('getIdeas/', include('reviive.urls', namespace='getIdeas')),
    path('findProf/', include('reviive.urls', namespace='findProf')),
    path('budgetEstimation/', include('reviive.urls', namespace='budgetEstimation')),
    path('findProf/customerReview/', include('reviive.urls', namespace='customerReview')),
    path('messageBox/', include('reviive.urls', namespace='messageBox')),
    path('renovationPriceGuide/', include('reviive.urls', namespace='renovationPriceGuide')),
    path('contractors/', include('reviive.urls', namespace='contractors')),
    path('users/', include('users.urls', namespace='users')),
]
