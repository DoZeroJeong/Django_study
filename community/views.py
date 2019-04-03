from django.shortcuts import render, redirect, reverse
from .models import Post, Comment
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView, FormView
from .forms import PostCreateForm, CommentForm


# Create your views here.


# 게시글 등록
class PostCreateView(CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'community/create.html'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        if form.is_valid():
            form.save()
            return redirect('/community/')
        else:
            return self.render_to_response({'form': form})


# 게시글 삭제
class PostDeleteView(DeleteView):
    model = Post
    success_url = '/community/'
    template_name = 'community/delete.html'


# 게시글 수정
class PostUpdateVIew(UpdateView):
    model = Post
    fields = ['title', 'genre', 'text']
    template_name = 'community/update.html'


# 게시글 상세보기
class PostDetailView(DetailView, FormView):
    model = Post
    template_name = 'community/detail.html'
    form_class = CommentForm


# 게시글 리스트
def post_list(request, genre):
    if genre == 'all':
        posts = Post.objects.all()
    else:
        posts = Post.objects.filter(genre=genre)
    return render(request, 'community/list.html', {'posts': posts})


# community 메인화면
def post_index(request):
    return render(request, 'community/index.html')

