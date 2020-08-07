from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Blog, BlogComment, BlogView, Like, Category
from .forms import BlogForm, BlogCommentForm


def BlogListView(request):
    all_blogs = Blog.objects.all()
    category_menu = Category.objects.all()
    quary = None

    if 's' in request.GET:
        query = request.GET['s']
        if not query:
            messages.error(request, "Sorry! No Input? Try again Please")
            return redirect(reverse('blog:list'))

        search = Q(title__icontains=query) | Q(content__icontains=query)
        all_blogs = all_blogs.filter(search)

    context = {
        'all_blogs': all_blogs,
        'category_menu': category_menu,

    }
    return render(request, 'blog/blog_list.html', context)


def CategoryView(request, category):
    category_blogs = Blog.objects.filter(category=category)
    category_menu = Category.objects.all()
    all_blogs = Blog.objects.all()

    context = {
        'category': category,
        'category_blogs': category_blogs,
        'category_menu': category_menu,
        'all_blogs': all_blogs
    }

    return render(request, 'blog/blog_categories.html', context)


class BlogDetailView(DetailView):
    model = Blog

    def post(self, *args, **kwargs):
        """Adding comments to blogs"""
        form = BlogCommentForm(self.request.POST)
        if form.is_valid():
            blog = self.get_object()
            blogcomment = form.instance
            blogcomment.user = self.request.user
            blogcomment.blog = blog
            blogcomment.save()
            return redirect("blog:details", slug=blog.slug)
        return redirect("blog:details", slug=self.get_object().slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'form': BlogCommentForm()

        })
        return context

    def get_object(self, **kwargs):
        """Counts the number of authenticated users view the blog """
        object = super().get_object(**kwargs)
        if self.request.user.is_authenticated:
            BlogView.objects.get_or_create(user=self.request.user, blog=object)
        return object


class BlogCreateView(CreateView):
    form_class = BlogForm
    model = Blog
    success_url = '/blog/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type': 'create'
        })
        return context


class BlogUpdateView(UpdateView):
    form_class = BlogForm
    model = Blog
    success_url = '/blog/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type': 'update'
        })
        return context


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = '/blog/'


@login_required(login_url="/accounts/login")
def like(request, slug):
    """ Checks to see if the use has liked the blog
    If True, then delete the like if False then create the like"""
    blog = get_object_or_404(Blog, slug=slug)
    like_qs = Like.objects.filter(user=request.user, blog=blog)
    if like_qs.exists():
        # unlike the post
        like_qs[0].delete()
        return redirect('blog:details', slug=slug)
    Like.objects.create(user=request.user, blog=blog)
    return redirect('blog:details', slug=slug)
