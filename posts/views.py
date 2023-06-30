from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm

# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {
        'posts' : posts,
    }
    return render(request, 'posts/index.html', context)

def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST) # 사용자가 입력한 값으로 폼을 만들어 보여줌
        if form.is_valid():
            post = form.save()
            return redirect('posts:detail', id=post.id)

    
    else: # POST 가 아닌 GET요청일 경우 내가만든 폼을 보여줌
        form = PostForm()

    context = {
        'form' : form,
    }

    return render(request, 'posts/form.html', context)


def detail(request, id):
    post = Post.objects.get(id=id)
    comment_form = CommentForm()

    comments = post.comment_set.all() # 전체 댓글 가져오기

    context = {
        'post':post,
        'comment_form' : comment_form,
        'comments' : comments,
    }
    return render(request, 'posts/detail.html', context)

def comments_create(request, post_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False) #commit 저장단위 / 아직DB에 저장하지 말고 False로 기다려라
            comment.post_id = post_id # 인자로 받아온 post_id를 comment와 연결
            comment.save()

            return redirect('posts:detail', post_id)

    else:
        return redirect('posts:detail', post_id)
    

def comments_delete(requst, post_id, id):
    comment = Comment.objects.get(id=id)

    comment.delete()
    return redirect('posts:detail', post_id)