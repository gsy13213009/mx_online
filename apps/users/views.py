from django.contrib.auth import authenticate, login as sys_login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.shortcuts import render

from users.models import UserProfile


# 自定义auth登录操作
class CustomBackend(ModelBackend):

    # 覆盖方法
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Q运算，求并集
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


# Create your views here.
def login(request):
    if request.method == 'POST':
        user_name = request.POST.get('username', '')
        pass_word = request.POST.get('password', '')
        # 如果用户验证成功，会返回用户对象，否则返回None
        user = authenticate(request, username=user_name, password=pass_word)
        if user is not None:
            sys_login(request, user)
            return render(request, 'index.html', {})
        else:
            return render(request, 'login.html', {'msg': '用户名或者密码错误'})
    elif request.method == 'GET':
        return render(request, 'login.html', {})
