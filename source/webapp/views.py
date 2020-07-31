from django.shortcuts import render, get_object_or_404, redirect

from webapp.forms import AskForm

from webapp.models import Article# STATUS_CHOICES
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
        form = AskForm(initial={
            'description': article.description,
            'status': article.status,
            'full_description': article.full_description,
            'date': article.date,
        })
        return render(request, 'update.html', context={
            'form': form,
            'article': article
        })

    elif request.method == 'POST':
        form = AskForm(data=request.POST)
        if form.is_valid():
            article.description = form.cleaned_data['description'],
            article.status = form.cleaned_data['status'],
            article.full_description = form.cleaned_data['full_description'],
            article.date = form.cleaned_data['date']
            article.save()
            return redirect('to_do_view', pk=article.pk)
        else:
            return render(request, 'update.html', context={
                'article': article,
                'form': form
            })
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])

def to_do_create_view(request):
    if request.method=='GET':
        form=AskForm()
        return render(request, 'to_do_creat.html',
                      {'form':form})
    elif request.method == 'POST':
        form = AskForm(data=request.POST)
        if form.is_valid():
            article = Article.objects.create(
                description=form.cleaned_data['description'],
                status=form.cleaned_data['status'],
                full_description=form.cleaned_data['full_description'],
                date=form.cleaned_data['date']
            )
            return redirect('to_do_view', pk=article.pk)
        else:
            return render(request, 'to_do_creat.html', context={
                'form': form
            })
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




