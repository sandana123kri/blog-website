from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html

# Create your models here.
class Post(models.Model):
    id=models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)


    def __str__(self):
        return self.title
    def image_tag(self):
        return format_html('<img src="/media/{}" />'.format(self.image))
    
    class Meta:
        verbose_name='My Post'
        verbose_name_plural='My Posts'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    added_by=models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    body = models.CharField(max_length=255)
    pub_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        #comment by sandana kumari 
        #x=User()
        return f'Comment by {self.name} on {self.post}'
