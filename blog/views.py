from django.http import HttpResponseRedirect
from django.shortcuts import redirect, reverse
from .models import Post, Comment, CommentLike
from .forms import PostForm, EditPostForm, CommentForm

from .mixins import AuthorAccessMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, FormView


class HomeView(TemplateView):
    template_name = 'blog/home.html'


class PostsView(ListView):
    model = Post
    paginate_by = 4
    template_name = 'blog/posts.html'


class PostView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/post.html'

    def get_context_data(self, **kwargs):
        cm_parent = None
        if self.request.GET.get('parent'):
            cm_parent = Comment.objects.get(pk=int(self.request.GET.get('parent')))
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        context['parent'] = cm_parent
        context['setting'] = context.get('post').setting
        context['comments'] = context.get('post').get_comments()
        return context


class AddCommentView(CreateView):
    model = Comment
    fields = ('content',)

    def get_success_url(self):
        return reverse('blog:post', kwargs={'slug': self.kwargs.get('slug')})

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.post = Post.objects.get(slug=self.request.POST.get('post'))
        if self.request.POST.get('parent'):
            obj.parent = Comment.objects.get(pk=int(self.request.POST.get('parent')))
        return super().form_valid(form)


class AddPostView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/add_post.html'
    form_class = PostForm

    def get_success_url(self):
        return reverse('blog:posts')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        p = Post.objects.get(slug=self.request.POST.get('slug'))
        p.create_setting()
        return HttpResponseRedirect(self.get_success_url())


class EditPostView(AuthorAccessMixin, UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = 'blog/edit_post.html'

    def get_success_url(self):
        return reverse('blog:post', kwargs={'slug': self.kwargs.get('slug')})


class CommentLikeView(LoginRequiredMixin, FormView):

    def post(self, request, *args, **kwargs):
        author = request.user
        cm = Comment.objects.get(pk=request.POST.get('cm_id'))
        like_status = request.POST.get('like_status')
        like_status = True if like_status == 'True' else False
        if CommentLike.objects.filter(author=author, comment=cm).exists():
            CommentLike.objects.filter(author=author, comment=cm).update(condition=like_status)
        else:
            CommentLike.objects.create(author=author, comment=cm, condition=like_status)
        return redirect('blog:post', slug=kwargs.get('slug'))