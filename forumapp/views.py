from django.shortcuts import render
from django.shortcuts import HttpResponse, HttpResponseRedirect
# Create your views here.
user_pswd = {"user1":'pswd1', 'user2':'pswd2'}

def test(request):
    # return HttpResponse("Hello World!!")
    return render(request,'test.html', {'form' : user_pswd})

# request表示网页上发过来的请求
def login(request):
    # request.method 表示请求的方法, 'GET'是请求网页,'POST'是发生数据到服务器
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('password')
        if username in user_pswd.keys() and user_pswd :
            if user_pswd[username] == password:
                pass
                # 登录成功, 跳转到首页
                # 重定向, 跳转到另一个网页，即'ip:port/Forum/index/'
                # 若定向到当前页面的子页面, 则不需要前面的'/'.
                return HttpResponseRedirect('/Forum/index/')
            else:
                # 第三个参数代表传给html的数据, 在html中err_inf代表值为'密码错误'的变量
                return render(request, 'login.html', {'err_inf' : '密码错误'})
        else :
            return render(request, 'login.html', {'err_inf' : '用户不存在'})


def register(request):
    return render(request, 'register.html')

