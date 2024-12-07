from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
user = get_user_model()


class BlogPost(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name='Title')
    slug = models.CharField(max_length=255, unique=True, blank=True, verbose_name='Slug')
    author = models.ForeignKey(user, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Author')
    last_update = models.DateTimeField(auto_now=True)
    created_on = models.DateField(blank=True, null=True)
    published = models.BooleanField(default=True, verbose_name='Published')
    content = models.TextField(blank=True, verbose_name='Content')
    thumbnail = models.ImageField(blank=True, upload_to='blog/')

    class Meta:
        ordering = ['-created_on']
        verbose_name = 'Article'
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    @property
    def author_or_defaulf(self):
        return self.author.username if self.author else 'Unkown Author'


    def get_absolute_url(self):
        return reverse('posts:home')