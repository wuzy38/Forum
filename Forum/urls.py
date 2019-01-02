"""Forum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from forumapp import views as forum_views #导入views模块
from account import views as account_views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Forum/index/', forum_views.test),
    path('Forum/user_info/<int:user_id>/', account_views.user_info, name='user_info'),
    path('Forum/test/', forum_views.test, name='test'),
    path('Forum/', forum_views.home, name='home'),
    path('Forum/register/', account_views.register, name = "register"),
    path('Forum/login/', account_views.login, name = 'login'),
    path('Forum/plate/<int:plate_id>', forum_views.plate, name = 'plate'),
    path('Forum/theme/<int:theme_id>', forum_views.theme, name = 'theme'),
]
