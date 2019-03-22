from django.shortcuts import render

# Create your views here.
from django.views import View

# 课程机构列表功能
class OrgView(View):

    def get(self, request):
        return render(request, 'org-list.html')
