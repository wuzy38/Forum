from django.shortcuts import render
from django.shortcuts import HttpResponse, HttpResponseRedirect
from sql import sql_p

# Create your views here.

def get_cur_user(session):
    if not session.has_key('user_account') or session['user_account'] == None:
        user = None
    else:
        user = {
            "user_account" : session['user_account'],
            "user_id" : session['user_id'],
        }
    return user

# request表示网页上发过来的请求
def login(request):
    # request.method 表示请求的方法, 'GET'是请求网页,'POST'是发生数据到服务器
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        # 提交的用户名和密码
        user_account = request.POST.get('name')
        password = request.POST.get('password')
        # 在数据库中寻找用户名
        if sql_p.check_user(user_account) :
            pswd = sql_p.get_password_by_account(user_account)
            print(pswd)
            if pswd == password:
                request.session['user_account'] = user_account
                request.session['user_id'] = sql_p.get_user_id_by_account(user_account)
                # request.session['user_name'] = 
                # 登录成功, 跳转到首页
                # 重定向, 跳转到另一个网页，即'ip:port/Forum/'
                # 若定向到当前页面的子页面, 则不需要前面的'/'.
                return HttpResponseRedirect('/Forum/')
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
        elif sql_p.check_user(username) :
            return render(request, 'register.html', {'inf' : '用户名已被注册'})
        else :
            # 将用户加入数据库
            sql_p.create_user(username, password, username)
            return render(request, 'register.html', {'inf' : '注册成功'})


# 个人信息界面 打印
def user_info(request, user_id):
    user = get_cur_user(request.session)
    if request.method == 'GET':
        user_imformation = sql_p.get_user_info_by_id(user_id)
        if len(user_imformation) > 0:
            return render(request, 'person_imformation.html', {'form' : user_imformation})
    elif request.method == 'POST':
        pass