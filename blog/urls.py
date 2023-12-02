from django.urls import path

from blog.views import IndexView, SingleBlogView, BlogView, login_user, logout_user, RegisterView

app_name = 'blog'

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('<int:pk>/', SingleBlogView.as_view(), name='single_blog'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('registration/', RegisterView.as_view(), name='registration')
]
