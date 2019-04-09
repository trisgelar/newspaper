from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from .models import Article

class ArticleCreateView(LoginRequiredMixin,CreateView):
	model = Article
	template_name = 'articles/new_view.html'
	fields = ('title', 'body', 'author',)
	login_url = 'login'

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


class ArticleListView(LoginRequiredMixin, ListView):
	model = Article
	template_name = 'articles/list_view.html'
	login_url = 'login'


class ArticleDetailView(LoginRequiredMixin, DetailView):
	model = Article
	template_name = 'articles/detail_view.html'
	login_url = 'login'

class ArticleUpdateView(LoginRequiredMixin, UpdateView):
	model = Article
	fields = ('title', 'body')
	template_name = 'articles/edit_view.html'
	login_url = 'login'

	def dispatch(self, request, *args, **kwargs):
		obj = self.get_object()
		if obj.author != self.request.user:
			raise PermissionDenied
		return super().dispatch(request, *args, **kwargs)

class ArticleDeleteView(LoginRequiredMixin, DeleteView):
	model = Article
	template_name = 'articles/delete_view.html'
	success_url = reverse_lazy('article_list')
	login_url = 'login'

	def dispatch(self, request, *args, **kwargs):
		obj = self.get_object()
		if obj.author != self.request.user:
			raise PermissionDenied
		return super().dispatch(request, *args, **kwargs	)
