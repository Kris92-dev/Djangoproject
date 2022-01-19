from django.shortcuts import render, redirect
from . models import *
from django.contrib.auth.models import User

# Create your views here.


def index(request):
    user = User.objects.get(id=1)
    request.session['userid'] = user.id
    return render(request, 'index.html')

def create(request):
    user = User()
    userp = user_profile()
    firstname = request.POST['fname']
    lastname = request.POST['lname']
    username = request.POST['uname']
    password = request.POST['password']
    email1 = request.POST['email']
    address1 = request.POST['add']
    date1 = request.POST['dob']
    image1 = request.FILES['img']
    user.first_name = firstname
    user.last_name = lastname
    user.username = username
    user.password = password
    user.email = email1
    user.save()
    userp.address = address1
    userp.dob = date1
    userp.image = image1
    userp.user = user
    userp.save()
    return redirect('/')


def view(request):
    user = User.objects.get(id=request.session['userid'])
    user_p = user_profile.objects.get(user=user)
    context = {'user':user, 'user_p': user_p}
    return render(request, 'display.html', context)


# def view_text(request, word):
#     print(word)
#     return redirect('view')    


