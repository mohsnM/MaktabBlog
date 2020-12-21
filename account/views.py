from django.shortcuts import redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import get_user_model
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LogoutView, LoginView
from django.views.generic import ListView, TemplateView
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import Group
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.models import Post

User = get_user_model()


class SingInView(LoginView):
    template_name = 'account/auth/login.html'
    redirect_authenticated_user = True
    form_class = LoginForm


class SignOutView(LogoutView):
    template_name = 'blog/home.html'


class SignUpView(CreateView):
    template_name = 'account/auth/register.html'
    form_class = RegisterForm

    def form_valid(self, form):
        group = Group.objects.get(name='normal user')
        obj = form.save(commit=False)
        password = obj.password
        obj.set_password(obj.password)
        obj.save()
        obj.groups.add(group)
        user = authenticate(self.request, username=obj.email, password=password)
        if user:
            login(self.request, user)
        return redirect('blog:home')


class ProfileView(LoginRequiredMixin, ListView):
    template_name = 'account/profile/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)
