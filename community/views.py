from django.shortcuts import render, redirect
from .models import Post
from django.views.generic.edit import CreateView, DeleteView, UpdateView

# Create your views here.


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'genre', 'text']
    template_name = 'community/create.html'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        if form.is_valid():
            form.instace.save()
            return redirect('/')
        else:
            return self.render_to_response({'form': form})


class PostDeleteView(DeleteView):
    model = Post
    success_url = '/'
    template_name = 'community/delete.html'


class PostUpdateVIew(UpdateView):
    model = Post
    fields = ['title', 'genre', 'text']
    template_name = 'community/update.html'


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'community/list.html', {'posts': posts})


