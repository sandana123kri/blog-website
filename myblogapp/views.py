from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post,Comment
from .forms import CommentForm,PostForm
def post_list(request):
    posts = Post.objects.all()
    if request.method =='POST':
        form=PostForm(request.POST, request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.image=post.image
            post.save()
            return redirect('/')
        
    else:
        form=PostForm()
    return render(request, 'myblogapp/post_list.html', {'posts': posts,'form':form})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    coms=Comment.objects.filter(post=post)
    if request.method == 'POST':
        form= CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post= post
            comment.added_by=request.user
            comment.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form= CommentForm()
    return render(request, 'myblogapp/post_detail.html', {'post': post,'coms':coms,'form':form})

# Create your views here.
