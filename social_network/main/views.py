from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from django.views.generic import CreateView,ListView,DetailView,UpdateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from main.forms import CustomUserCreationForm,CustomAuthenticationForm
from main.models import CustomUser,UserComments
from django.contrib import messages

# Create your views here.
class UserRegistration(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('start_journey_page')
    template_name = 'register.html'

class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'login.html'

class UserProfileDetails(DetailView):
    model = CustomUser
    template_name = 'userprofiledetails.html'
    context_object_name = 'profile'
        
def UserProfileUpdate(request,pk):
    user = CustomUser.objects.get(id = pk)
    if request.method == 'POST':
        user.username = request.POST['username']
        user.password = request.POST['password']
        user.bio = request.POST['bio']

        if request.FILES.setdefault('avatar'):
            user.avatar = request.FILES.get('avatar')
        
        user.save()
        return redirect('user_profile', pk = user.pk)
    return render(request,'update.html',{'user' : user})

def home(request):
    if request.method == 'POST':
        temp_post = UserComments()
        temp_post.content = request.POST['user-thoughts']
        
        # Проверяем наличие файла в запросе
        if request.FILES.get('just-image'):
            temp_post.file = request.FILES.get('just-image')
            
        # Используем модель и его поле в качестве создателя комментария
        temp_post.user_creator = request.user
        temp_post.save()
        return redirect('home_page')
    
    context = {
        'user' : CustomUser.objects.get(id = request.user.pk),
        'posts' : UserComments.objects.all(),
    }
    return render(request,template_name='home_page.html',context=context)


# class UserPostsView(ListView):
#     model = UserComments
#     template_name = 'user_posts.html'
#     context_object_name = 'posts'
    
#     def get_context_data(self,**kwargs):
#         context = super().get_context_data(**kwargs)
#         pk = self.kwargs.setdefault('pk')
#         user_comments = UserComments.objects.get(pk=pk)
        
#         context['data'] = user_comments
        
#         return context