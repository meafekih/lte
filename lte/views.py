from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def table(request):
    data = [
        {'rendering': 'John', 'bowser': '30', 'platform': 'John', 'engine': '30', 'css': '30'},
        {'rendering': 'John', 'bowser': '30', 'platform': 'John', 'engine': '30', 'css': '30'},
        {'rendering': 'John', 'bowser': '30', 'platform': 'John', 'engine': '30', 'css': '30'},
        # Add more data as needed
    ]
    context = {'data': data}
    return render(request, 'pages/tables/data2.html',context=context)
