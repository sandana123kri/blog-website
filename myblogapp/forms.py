from django import forms
from .models import Comment,Post

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body','email',)
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        #image=forms.ImageField(upload_to='post_images/', blank=True,null=True)
        fields= ('title','content','image',)
