from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseNotAllowed
from django.views.generic import View, TemplateView
from webapp.forms import AskForm

from webapp.models import Article

from django.urls import reverse


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        data = Article.objects.all()
        context = {'articles':data}
        return context



class TO_Do_View(TemplateView):
    template_name = 'to_do_view.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        pk = self.kwargs.get('pk')
        article = get_object_or_404(Article, pk=pk)

        context['article'] = article
        return context



class To_Do_Update_View(TemplateView):
    template_name = 'update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        pk = self.kwargs.get('pk')
        article = get_object_or_404(Article, pk=pk)
        initial = {}
        for key in 'description', 'full_description', 'date':
            initial[key] = getattr(article, key)

        form = AskForm(initial=initial)

        context['article'] = article
        context['form'] = form

        return context

    def post(self, request, pk):
        article = get_object_or_404(Article, pk=pk)
        form = AskForm(data=request.POST)
        if form.is_valid():
            for key, value in form.cleaned_data.items():
                if value is not None:
                    setattr(article, key, value)
            article.save()
            return redirect('to_do_view', pk=article.pk)
        else:
            return self.render_to_response({
                'article': article,
                'form': form
            })


class To_Do_Create_View(TemplateView):
    template_name = 'to_do_creat.html'

    def get_context_data(self, **kwargs):


        form = AskForm()

        context = {'form': form}
        return context

    def post(self, request):
        form = AskForm(data=request.POST)
        if form.is_valid():

            data = {}
            for key, value in form.cleaned_data.items():
                if value is not None:
                    data[key] = value
            article = Article.objects.create(**data)
            return redirect('to_do_view', pk=article.pk)
        else:
            return self.render_to_response({

                'form': form
            })




class Delete_To_Do(TemplateView):
    template_name = 'del_to_do.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        pk = self.kwargs.get('pk')
        article = get_object_or_404(Article, pk=pk)


        context['article'] = article

        return context

    def post(self, request, pk):
        article = get_object_or_404(Article, pk=pk)
        article.delete()
        return redirect('index')





#def delete_to_do(request, pk):
#    article = get_object_or_404(Article, pk=pk)
#    if request.method == 'GET':
#        return render(request, 'del_to_do.html', context={'article': article})
#    elif request.method == 'POST':
#        article.delete()
#        return redirect('index')
#    else:
#        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])




