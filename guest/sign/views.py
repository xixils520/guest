from django.shortcuts import render
#username lisong  password  lisong123
# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from sign.models import Event
from sign.models import Event,Guest
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
def  index(request):
    return render(request,"index.html")

#登录请求
def login_action(request):
    if request.method=='POST':
        username=request.POST.get('username','')
        password=request.POST.get('password','')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            request.session['user']=username
            response=HttpResponseRedirect('/event_manage/')
            return response
        # if username=='admin' and password=='admin123':
        #     response=HttpResponseRedirect('/event_manage/')
        #     # response.set_cookie('user',username,3600)
        #     request.session['user']=username
        #     return response

        else:
            return render(request,'index.html',{'error':'用户名密码不匹配'})

@login_required
def event_manage(request):
            # username=request.COOKIES.get('user','')
    event_list=Event.objects.all()
    username = request.session.get('user', '')
    return render(request, "event_manage.html", {"user": username,"events":event_list})



@login_required
def search_name(request):
    username=request.session.get('user','')
    search_name=request.GET.get("name","")
    event_list=Event.objects.filter(name_contains=search_name)
    return render(request,"event_manage.html",{"user":username,"events":event_list})

# 嘉宾管理
# 嘉宾管理
@login_required
def guest_manage(request):
    guest_list = Guest.objects.all()
    username = request.session.get('username', '')

    paginator = Paginator(guest_list, 2)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # 如果页数不是整型, 取第一页.
        contacts = paginator.page(1)
    except EmptyPage:
        # 如果页数超出查询范围，取最后一页
        contacts = paginator.page(paginator.num_pages)
    return render(request, "guest_manage.html", {"user": username, "guests": contacts})
