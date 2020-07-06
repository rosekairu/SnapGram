 
from django.contrib.auth.decorators import login_required
from .forms import  NewStatusForm, NewCommentForm
from django.shortcuts import render,redirect
from .models import Image, Profile, Comment

# Create your views here.
@login_required(login_url='/accounts/login/')
def timeline(request):
    current_user = request.user
    images = Image.objects.order_by('-pub_date')
    profiles = Profile.objects.order_by('-last_update')
    comment = Comment.objects.order_by('-date')
    return render(request, 'timeline.html', {"images":images, "profiles":profiles, "user_profile":user_profile, "comment":comment})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    # profile = Profile.objects.get(user_id=current_user.id)
    images = Image.objects.all().filter(profile_id=current_user.id)
    return render(request, 'profile.html', {"images":images, "profile":profile})

@login_required(login_url='/accounts/login/')
def new_status(request, username):
    current_user = request.user
    username = current_user.username
    if request.method =='POST':
        form = NewStatusForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save()
            image.user = request.user
            image.save()
        return redirect('allTimelines')
    else:
        form = NewStatusForm()
    return render(request, 'new_status.html', {"form":form}) 

#User Profile           
@login_required(login_url='/accounts/login/')
def user_profile(request, user_id):
    profile = Profile.objects.get(id=user_id)
    images = Image.objects.all().filter(user_id=user_id)
    return render(request, "profile.html", {"[profile":profile, "images":images})

@login_required(login_url='/accounts/login/')
def single_image(request, image_id):
    image = Image.objects.get(id = image_id)
    return render(request, "single_image.html",{"image":image})

def find_profile(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_user(search_term)
        message = f"{search_term}"
        return render(request, 'user_profile.html',{"message":message,"image": searched_images})

    else:
        message = "You haven't searched for any term yet"
        return render(request, 'single_image.html',{"message":message}) 

@login_required(login_url='/accounts/login/')
def single_image_like(request, image_id):
    image = Image.objects.get(id=image_id)
    image.likes = image.likes + 1
    image.save()
    return redirect('allTimelines')

@login_required(login_url='/accounts/login/')
def new_comment(request, username):
    current_user =request.user
    username = current_user.username
    if request.method =='POST':
        form = NewCommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save()
            comment.user = request.user
            comment.save()
        return redirect('allTimelines')
    else:
        form = NewCommentForm()
    return render(request, 'new_comment.html', {"form":form})