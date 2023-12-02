from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseForbidden
from django.views import View

from django.views.generic import ListView, DetailView, CreateView, TemplateView

from blog.forms import UserForm, RegistrationForm, MessageForm
from blog.models import BlogModel, Category, Tag, User, Message

from django.shortcuts import render, redirect


class IndexView(ListView):
    model = BlogModel
    template_name = 'blog/index.html'
    context_object_name = 'form'
    paginate_by = 1


class BlogView(ListView):
    model = BlogModel
    template_name = 'blog/blog.html'
    context_object_name = 'forms'
    paginate_by = 2


class SingleBlogView(DetailView):
    model = BlogModel
    template_name = 'blog/blog_single.html'
    context_object_name = 'blog'

    def post(self, request, pk):
        blg = BlogModel.objects.get(id=pk)
        form = MessageForm()

        if request.method == 'POST':
            form = MessageForm(request.POST or None)
            if form.is_valid():
                msg = form.save(commit=False)
                msg.user = request.user
                msg.blog = blg
                msg.save()
                return redirect('blog:single_blog', pk=pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['tags'] = Tag.objects.all()
        context['message'] = Message.objects.filter(blog=self.object)
        context['form'] = MessageForm

        search_query = self.request.GET.get('search')
        if search_query:
            context['blogs'] = BlogModel.objects.filter(category__title__icontains=search_query)
        else:
            context['blogs'] = BlogModel.objects.all()

        return context


def login_user(request):
    if request.method == 'POST':
        data = request.POST
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username, password=password)
        print(user)

        if user:
            login(request, user)
        return redirect('blog:home')

    form = UserForm()
    context = {'form': form}

    return render(request, 'blog/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('blog:login')


#
# class RegistrationView(View):
#     def get(self, request):
#         form = RegistrationForm()
#         return render(request, 'blog/registration.html', {'form': form})
#
#     def post(self, request):
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             email = form.cleaned_data['email']
#             image = form.cleaned_data['image']
#             # Create a new user
#             user = User.objects.create_user(username=username, password=password, email=email, image=image)
#             # Log the user in
#             login(request, user)
#             return redirect('blog:home')
#         return render(request, 'blog/registration.html', {'form': form})
#
#
# def csrf_failure_view(request, reason=''):
#     return HttpResponseForbidden('CSRF verification failed. Reason: ' + reason)

class RegisterView(TemplateView):
    template_name = 'blog/registration.html'
    form_class = RegistrationForm

    def get(self, request):
        form = self.form_class()
        message = ''
        return render(request, self.template_name, context={'form': form, 'message': message})

    def post(self, request):
        form = RegistrationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form = form.save()
            return redirect('blog:home')
        message = 'Registration Failed!'
        return render(request, self.template_name, context={'form': form, 'message': message})
