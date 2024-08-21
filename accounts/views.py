from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib import messages
from django.http import HttpResponse
from accounts.form import UserForm


# Create your views here.

class TestView(TemplateView):
    template_name = 'test.html'

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')
    
    def post(self, request):
        phone = request.POST['phone']
        password = request.POST['password']
        user = authenticate(phone = phone, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Successfuly Login')
            return redirect('home')
        messages.error(request, 'Incorrect login or password')
        return redirect('login')

class LogoutView(View):
    def get(self, request):
        return render(request, 'logout.html')
    
    def post(self, request):
        logout(request)
        messages.warning(request, "Successfully Logged Out!")
        return redirect('home')
    
class SignUpView(View):
    def get(self, request):
        form = UserForm()
        return render(request, 'signup.html', {'form' : form})
    
    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password2'])
            user.save()
            messages.success(request, "Siz tizimdan muvaffaqiyatli ro'yxatdan o'tdingiz!")
            return redirect('login')
        return render(request, 'signup.html', {'form' : form})
        
    
