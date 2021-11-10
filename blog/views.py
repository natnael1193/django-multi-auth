from django.shortcuts import redirect, render
from django.urls.base import reverse, reverse_lazy
from .forms import AddBlog
from .models import Blog
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
# Create your views here.


def blog(request):

    return render(request, 'blog.html')


@login_required(login_url='/login_view/')
def add_blog(request):
    if request.user == 'is_admin': 
     msg = None
     if request.method == 'POST':
         form = AddBlog(request.POST)
         if form.is_valid():
             blog = form.save()
             msg = 'Blog Added'
             return redirect('blog')
         else:
             msg = 'Form is not valid'
     else:
         form = AddBlog()
         return render(request, 'add_blog.html', {'form': form, 'msg': msg})
    else:
        return redirect('not_authenticated')
     


# @method_decorator(login_required, name='dispatch')
class EditBlog(LoginRequiredMixin, UpdateView):
    login_url = '/login_view/'
    # redirect_field_name = 'redirect_to'
    model = Blog
    template_name = 'edit_blog.html'
    fields = '__all__'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('blog')

    def get(self, request, *args, **kwargs):
        if request.user == 'is_admin': 
            return render(request, self.template_name)
        else:
            return render(request, 'auth/not_authenticated.html')


