from django.shortcuts import render
from django.shortcuts import HttpResponse, HttpResponseRedirect
from sql import sql_p

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
                # request.session['user_id'] = 
                # 登录成功, 跳转到首页
                # 重定向, 跳转到另一个网页，即'ip:port/Forum/index/'
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
        elif username in user_pswd.keys() :
            return render(request, 'register.html', {'inf' : '用户名已被注册'})
        else :
            # 将用户加入数据库
            user_pswd[username] = password
            return render(request, 'register.html', {'inf' : '注册成功'})





# 个人信息界面 打印
def user_info(request, user_id):
    if request.method == 'GET':
        user_imformation = {}
        data = sql_p.select_from('user','*','where user_id='+str(user_id))
        if len(data)>0:
            user_imformation['id'] = data[0]
            user_imformation['name'] = data[1]
            user_imformation['register_time'] = data[2]
            user_imformation['grade'] = data[3]
            user_imformation['user_account'] =data[4]
            return render(request,'person_imformation.html', {'form' : user_imformation})
    elif request.method == 'POST':
        pass

# 主界面, 传入当前用户user变量,代表是否已经认证, 传入'plates'变量
def home(request):
    user = None
    plate_datas = sql_p.select_from('plate')
    print(plate_datas)
    plates = [{'plate_id' : plate_data[0], 'plate_name':plate_data[1], 'plate_size' : plate_data[2]} for plate_data in plate_datas]
    # plates = [{'plate_id' : 1, 'plate_name':'python', 'plate_size' : 1}]
    content = {'user' : user, 'plates' : plates}
    return render(request, 'home.html', content)

# 板块内部
def plate(request, plate_id):
    # 如果plate_id不存在，重定向回主页
    # plate_id=0
    plate_name = sql_p.select_from('plate', 'plate_name ', 'where plate_id=' + str(plate_id))
    print(plate_name)
    if len(plate_name) == 0:
        return HttpResponseRedirect('/Forum/')
    if request.method == 'GET' :
        # 根据plate_id获取plate_name 和对应的theme
        # plate_name = 'python'
        themes = sql_p.get_all_theme(plate_id)
        return render(request, 'plate.html', {'plate_name' : plate_name[0][0], 'themes' : themes})
    else:
        # 写主题, 添加到theme表中
        theme_content = request.POST.get('theme_content')
        sql_p.insert_into('theme', )
        pass


#贴子
def theme(request, theme_id):
    # 如果theme_id不存在, 重定向回主页
    if False:
        return HttpResponseRedirect('/Forum/')
    if request.method == 'GET' :
        # 根据theme_id获取 theme的内容和对应的replys
        theme = None
        replys = None
        return render(request, 'plate.html', {'theme' : theme, 'replys' : replys})
    else:
        # 写回复, 添加到reply表中
        pass