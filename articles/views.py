from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from .models import Article

class ArticleCreateView(CreateView):
	model = Article
	template_name = 'articles/new_view.html'
	fields = ('title', 'body', 'author',)

class ArticleListView(ListView):
	model = Article
	template_name = 'articles/list_view.html'

class ArticleDetailView(DetailView):
	model = Article
	template_name = 'articles/detail_view.html'

class ArticleUpdateView(UpdateView):
	model = Article
	fields = ('title', 'body')
	template_name = 'articles/edit_view.html'

class ArticleDeleteView(DeleteView):
	model = Article
	template_name = 'articles/delete_view.html'
	success_url = reverse_lazy('article_list')