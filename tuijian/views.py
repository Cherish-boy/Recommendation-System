from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def listorders(request):
    return HttpResponse("科研训练项目开始")

# 导入 Company 对象定义
from  common.models import  Company

def listcompany(request):
    # 返回一个 QuerySet 对象 ，包含所有的表记录
    qs = Company.objects.values()

    # 检查url中是否有参数phonenumber
    ph = request.GET.get('phonenumber', None)

    # 如果有，添加过滤条件
    if ph:
        qs = qs.filter(phonenumber=ph)

    # 定义返回字符串
    retStr = ''
    for company in qs:
        for name, value in company.items():
            retStr += f'{name} : {value} | '
        # <br> 表示换行
        retStr += '<br>'

    return HttpResponse(retStr)