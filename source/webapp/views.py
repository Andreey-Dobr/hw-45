from django.shortcuts import render
from webapp.models import Article, STATUS_CHOICES
from django.http import HttpResponseNotAllowed


def index_view(request):

    data = Article.objects.all()
    return render(request, 'index.html', context={
        'articles': data
    })


def to_do_create_view(request):
    if request.method == "GET":
        return render(request, 'to_do_creat.html', context={
            'status_choices': STATUS_CHOICES
        })
    elif request.method == 'POST':
        description = request.POST.get("description")
        status = request.POST.get('status')
        date = request.POST.get('date')
        article = Article.objects.create(description=description, status=status, date=date)
        context = {'article': article}
        return render(request, 'to_do_view.html', context)
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])


def delete_to_do(request):
    if request.method == "GET":
        return render(request, 'del_to_do.html')
    elif request.method == 'POST':
        description = request.POST.get("description")
        article = Article.objects.get(description=description)
        context = {'article': article.delete()}
        return render(request, 'delet.html', context)
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])
