from django.contrib.auth import authenticate, login as sys_login
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from users.forms import LoginForm, RegisterForm, ForgetForm, ModifyPwdForm
from users.models import UserProfile, EmailVerifyRecord

# 自定义auth登录操作
from utils.email_send import send_register_email


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


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html', {})

    def post(self, request):
        login_form = LoginForm(request.POST)
        # 如果LoginForm校验通过
        if login_form.is_valid():
            user_name = request.POST.get('username', '')
            pass_word = request.POST.get('password', '')
            # 如果用户验证成功，会返回用户对象，否则返回None
            user = authenticate(request, username=user_name, password=pass_word)
            if user is not None:
                if user.is_active:
                    sys_login(request, user)
                    return render(request, 'index.html', {})
                else:
                    return render(request, 'login.html', {'msg': '用户未激活'})
            else:
                return render(request, 'login.html', {'msg': '用户名或者密码错误'})
        else:
            return render(request, 'login.html', {'login_form': login_form})


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'register.html', locals())

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            email = request.POST.get('email', '')
            if UserProfile.objects.filter(email=email):
                return render(request, 'login.html', {'msg': '用户已经存在'})
            password = request.POST.get('password', '')
            user_profile = UserProfile()
            user_profile.username = email
            user_profile.email = email
            user_profile.is_active = False
            user_profile.password = make_password(password)
            user_profile.save()

            send_register_email(email, 'register')
            return render(request, 'login.html')
        else:
            return render(request, 'register.html', locals())


class ActiveUser(View):

    def get(self, request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
        else:
            return HttpResponse('链接已失效')
        return render(request, 'login.html')


class ForgetView(View):

    def get(self, request):
        forget_form = ForgetForm()
        return render(request, 'forgetpwd.html', locals())

    def post(self, request):
        forget_form = ForgetForm(request.POST)
        if forget_form.is_valid():
            email = request.POST.get('email')
            send_register_email(email, 'forget')
            return HttpResponse('邮件已经发送，请查收')
        else:
            return render(request, 'forgetpwd.html', locals())


class ResetView(View):

    def get(self, request, reset_code):
        all_records = EmailVerifyRecord.objects.filter(code=reset_code)
        if all_records:
            for record in all_records:
                email = record.email
                return render(request, 'password_reset.html', locals())
        else:
            return HttpResponse('hhhhhhhhhh')

class ModifyPwdView(View):
    def post(self, request):
        modify_form = ModifyPwdForm(request.POST)
        if modify_form.is_valid():
            pwd1 = request.POST.get('password1', '')
            pwd2 = request.POST.get('password2', '')
            email = request.POST.get('email', '')
            if pwd1 != pwd2:
                return render(request, 'password_reset.html', {'msg': '密码不一致'})
            users = UserProfile.objects.filter(email=email)
            for user in users:
                if user:
                    user.password = make_password(pwd1)
                    user.save()
            return render(request, 'login.html')
        else:
            return render(request, 'password_reset.html', locals())
