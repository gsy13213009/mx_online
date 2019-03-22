"""mx_online URL Configuration

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
from django.conf.urls import url
from django.urls import path, include
from django.views.generic import TemplateView
import xadmin
from organization.views import OrgView
from users.views import LoginView, RegisterView, ActiveUser, ForgetView, ResetView, ModifyPwdView

urlpatterns = [
    path('admin/', xadmin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^active/(?P<active_code>.*)/$', ActiveUser.as_view(), name='active'),
    url(r'^forget/$', ForgetView.as_view(), name='forget_pwd'),
    url(r'^reset/(?P<reset_code>.*)/$', ResetView.as_view()),
    url(r'^reset/$', ModifyPwdView.as_view(), name='reset_pwd'),

    url(r'^org_list/$', OrgView.as_view(), name='org_list'),

]
