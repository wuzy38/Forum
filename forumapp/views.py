from django.shortcuts import render
from django.shortcuts import HttpResponse, HttpResponseRedirect
# Create your views here.
user_pswd = {"user1":'pswd1', 'user2':'pswd2'}
user_imformation = {'name':'xiaojz','age':'19','where':'guangz','school':'sysu'} #测试用户信息


def test(request):
    # return HttpResponse("Hello World!!")
    return render(request,'test.html', {'form' : user_pswd})

# request表示网页上发过来的请求
def login(request):
    # request.method 表示请求的方法, 'GET'是请求网页,'POST'是发生数据到服务器
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        # 提交的用户名和密码
        username = request.POST.get('name')
        password = request.POST.get('password')
        # 在数据库中寻找用户名
        if username in user_pswd.keys() :
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
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('password')
        if username == '' :
            return render(request, 'register.html', {'inf' : ' 用户名不能为空'})
        elif password == '' :
            return render(request, 'register.html', {'inf' : ' 密码不能为空'})
        # 检测用户名是否已在数据库中
        elif username in user_pswd.keys() :
            return render(request, 'register.html', {'inf' : '用户名已被注册'})
        else :
            # 将用户加入数据库
            user_pswd[username] = password
            return render(request, 'register.html', {'inf' : '注册成功'})

# 主界面
def forum(request):
# 主界面, 传入user变量,代表是否已经认证, 传入'boards'变量
def home(request):
    return render(request, 'home.html', {'boards' : {}})
    pass


# 个人信息界面 打印
def user_info(request, user_id):
    if request.method == 'GET':
        return render(request,'person_imformation.html', {'form' : user_imformation})
    elif request.method == 'POST':
        pass



# 板块内部
def plate(request, plate_id):
    pass

def theme(request, plate_id, theme_id):
    pass