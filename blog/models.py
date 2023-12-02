from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.urls import reverse


class User(AbstractUser):
    picture = models.ImageField(upload_to='user/', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    groups = models.ManyToManyField(
        Group,
        related_name='blog_users',  # Add a unique related_name
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='blog_users',  # Add a unique related_name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.username


class Category(models.Model):
    objects = None
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title


class Tag(models.Model):
    objects = None
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title


class BlogModel(models.Model):
    objects = None
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Author',
                              related_name="BlogModel")
    title = models.CharField(max_length=221)
    description = models.TextField()
    image = models.ImageField(upload_to='blog/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, related_name='tag')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:single_blog', kwargs={'pk': self.id})


class Message(models.Model):
    objects = None
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(BlogModel, on_delete=models.CASCADE)
    message = models.TextField()
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f'{self.user.username}:{self.message[:30]} >> {self.parent}'

    @property
    def children(self):
        return Message.objects.filter(parent=self).reverse()

    @property
    def is_parent(self):
        if self.parent is None:
            return True
        return False
