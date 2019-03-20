from django.contrib.auth import authenticate, login as sys_login
from django.http import HttpResponse
from django.shortcuts import render

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
    elif request.method == 'GET':
        return render(request, 'login.html', {})
    return render(request, 'login.html', {})
