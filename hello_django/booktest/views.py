# coding=utf-8
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext, loader
from models import BookInfo


# Create your views here.
def index(request):
    # 获取请求的数据
    booklist = BookInfo.objects.all()
    # 获取请求显示的模板
    template = loader.get_template("booktest/index.html")
    # 构建响应内容
    context = RequestContext(request, {'booklist': booklist})
    # 返回响应
    # return HttpResponse(template.render(context))  # 方式一
    return render(request, "booktest/index.html", {'booklist': booklist})  # 方式二


def detail(request, id):
    # 获取请求的数据
    book = BookInfo.objects.get(pk=id)
    # 获取请求显示的模板
    template = loader.get_template("booktest/detail.html")
    # 构建响应内容
    context = RequestContext(request, {'book': book})
    # 返回响应
    return HttpResponse(template.render(context))  # 方式一
    # return render(request, "booktest/detail.html", {'book': book})  # 方式二


def page_not_found(request):
    return render_to_response("booktest/404.html")
