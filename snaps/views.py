from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Image,Profile,Follow,Comments
from .forms import NewImageForm, UpdatebioForm,CommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    images = Image.objects.order_by('pub_date').reverse().all()
    image_comments = Image.get_images()
    return render(request, 'profile/home.html', {"images":images,"image_comments":image_comments})

def search_results(request):
    if 'user' in request.GET and request.GET['user']:
        search_term = request.GET.get('user')
        searched_user = Profile.search_by_user(search_term)
        message = f"{search_term}"

        return render(request, 'profile/search.html', {"message":message,"users":searched_user})
    else:
        message = "You haven't searched for any term"
        return render(request, 'profile/search.html', {"message":message})

def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    current_user = request.user
    comments = Comments.objects.filter(comment_image = image)
    print(comments)
    return render(request,"profile/image.html", {"image":image,'comments':comments})

@login_required(login_url='/accounts/login/')
def new_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.profile = current_user.profile
            image.save()
        return redirect('home')

    else:
        form = NewImageForm()
    return render(request, 'registration/new_image.html', {"form": form})

@login_required(login_url='/accounts/login/')
def update_profile(request):
    current_user = request.user
    if request.method == 'POST':
        if Profile.objects.filter(user_id=current_user).exists():
            form = UpdatebioForm(request.POST, request.FILES,instance=Profile.objects.get(user_id=current_user))
        else:
            form = UpdatebioForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('home')

    else:
        if Profile.objects.filter(user_id=current_user).exists():
            form = UpdatebioForm(instance = Profile.objects.get(user_id=current_user))
        else:
            form = UpdatebioForm()
    return render(request, 'registration/update_profile.html', {"form": form})

@login_required(login_url='/accounts/login/')
def profile(request,profile_id):
    current_user = request.user
    user = User.objects.get(pk=profile_id)
    images = Image.objects.filter(profile=profile_id)
    credentials = Profile.objects.filter(user = profile_id)

    if Follow.objects.filter(following=request.user,follower=user).exists():
        follows_me =True

    else:
        follows_me=False
    followers=Follow.objects.filter(follower = user).count()
    following=Follow.objects.filter(following = user).count()

    return render (request, 'registration/profile.html', {'images':images,'follows_me':follows_me,'following':following,'followers':followers, 'current_user': current_user,'credentials':credentials})

def follow(request,user_id):
    user = User.objects.get(id=user_id)
    follows_me=False
    if Follow.objects.filter(following=request.user,follower=user).exists():
        Follow.objects.filter(following=request.user,follower=user).delete()
        follows_me=False
    else:
        Follow(following=request.user,follower=user).save()
        follows_me=True
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='/accounts/login/')
def comment(request,image_id):
    current_user = request.user
    images = Image.objects.filter(id=image_id).first()
    prof = Profile.objects.filter(user=current_user).first()
    if request.method=='POST':
        form=CommentForm(request.POST,request.FILES)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.user= current_user
            comment.comment_image=images
            comment.save()
            return redirect('home')

    else:
        form=CommentForm()
    return render(request,'profile/comment.html',{'form':form,'image_id':image_id})
    
def comment_show(request,image_id):
    try:
        comment =Comment.objects.get(id =image.id)
    except:
        raise Http404()
        returnrender(request,'home.html',{"comment":comment})

def likes(request,id):
    likes=1
    image = Image.objects.get(id=id)
    image.like = image.like+1
    image.save()    
    return redirect("home")