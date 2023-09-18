from django.shortcuts import render
from django.contrib.auth.models import User


def index(request):
    return render(request, 'pages/index.html')

def login(request):
    return render(request, 'pages/login.html')

def register(request):
    return render(request, 'pages/register.html')

def forgot_password(request):
    return render(request, 'pages/forgot_password.html')

def faq(request):
    return render(request, 'pages/faq.html')


def contact_us(request):
    return render(request, 'pages/contact_us.html')
def sales_list(request):
    data = [
        {'username': 'John', 'first_name': 'week', 'last_name': 'John', 'email': 'john@email.com'},
        {'username': 'John', 'first_name': 'week', 'last_name': 'John', 'email': 'john@email.com'},
        # Add more data as needed
    ]
    context = {'data': data}
    return render(request, 'pages/sales_list.html',context=context)


def profile(request):
    return render(request, 'pages/profile.html')


def followers(request):
    return render(request, 'pages/followers.html')


def pricing(request):
    return render(request, 'pages/pricing.html')






""" 
def get_users(request):
    users = User.objects.all()
    context = {'users': users}
    #return render(request, 'users/home.html', context=context)
    return render(request, 'pages/tables/data2.html',context=context)


def table(request):
    data = [
        {'rendering': 'John', 'bowser': '30', 'platform': 'John', 'engine': '30', 'css': '30'},
        {'rendering': 'John', 'bowser': '30', 'platform': 'John', 'engine': '30', 'css': '30'},
        {'rendering': 'John', 'bowser': '30', 'platform': 'John', 'engine': '30', 'css': '30'},
        # Add more data as needed
    ]
    context = {'data': data}
    return render(request, 'pages/tables/data2.html',context=context)

from django.http import JsonResponse

def book_list(request):
    books = [
        {'title': 'Book 1', 'author': 'Author 1'},
        {'title': 'Book 2', 'author': 'Author 2'},
        {'title': 'Book 3', 'author': 'Author 3'},
        {'title': 'Book 1', 'author': 'Author 1'},
        {'title': 'Book 2', 'author': 'Author 2'},
    ]
    return JsonResponse({'books': books})


"""