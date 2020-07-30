from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Article, STATUS_CHOICES
from django.http import HttpResponseNotAllowed
from django.urls import reverse


def index_view(request):

    data = Article.objects.all()
    return render(request, 'index.html', context={
        'articles': data
    })


def to_do_view(request, pk):
    article = get_object_or_404(Article, pk=pk)

    context = {'article': article}
    return render(request, 'to_do_view.html', context)


def to_do_update_view(request, pk):

    article = get_object_or_404(Article, pk=pk)

    if request.method == 'GET':
        return render(request, 'update.html', context={'article': article,
           'status_choices': STATUS_CHOICES
           })

    elif request.method == 'POST':
        article.description = request.POST.get("description")
        article.status = request.POST.get('status')
        article.full_description = request.POST.get("full_description")
        article.date = request.POST.get('date')
        article.save()
        return redirect('to_do_view', pk=article.pk)


def to_do_create_view(request):
    if request.method == "GET":
        return render(request, 'to_do_creat.html', context={
            'status_choices': STATUS_CHOICES
        })
    elif request.method == 'POST':
        description = request.POST.get("description")
        status = request.POST.get('status')
        full_description = request.POST.get("full_description")
        date = request.POST.get('date')
        article = Article.objects.create(description=description, status=status, date=date, full_description=full_description)
        context = {'article': article}
        return render(request, 'to_do_view.html', context)
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])


def delete_to_do(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'GET':
        return render(request, 'del_to_do.html', context={'article': article})
    elif request.method == 'POST':
        article.delete()
        return redirect('index')
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])



#    if request.method == "GET":
#        return render(request, 'del_to_do.html')
#    elif request.method == 'POST':
#        description = request.POST.get("description")
#        article = Article.objects.get(description=description)
#        context = {'article': article.delete()}
#        return render(request, 'delet.html', context)
#    else:
#        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])
