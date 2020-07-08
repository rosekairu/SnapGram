from django.shortcuts import render, redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User as AbstractUser
from django.contrib.auth import logout
from .forms import ImageForm
from .email import send_welcome_email
from .models import Profile, User, Image, Comment, ImageLike, Followers



@login_required(login_url='/accounts/login/')
def index(request):
    current_user = request.user
    all_images = Image.objects.all()
    return render(request, 'index.html', {'images': all_images})


@login_required(login_url='/accounts/login/')
def create_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.account_holder = current_user
            profile.save()
        return redirect('myprofile')

    else:
        form = NewProfileForm()
    return render(request, 'new-profile.html', {"form": form})


@login_required(login_url='/accounts/login/')
def myprofile(request):
    current_user = request.user

    if Profile.objects.filter(user=current_user).first():
        all_images = Image.get_user_images(current_user)
        profile = Profile.objects.filter(user=current_user).first()
    else:
        profile = Profile(user=current_user)
        profile.save()
        send_welcome_email(current_user.username, current_user.email)

    all_images = Image.objects.filter(user = current_user).all()

    return render(request, 'profile.html', {'user': current_user, 'images': all_images, 'profile' : profile})


@login_required(login_url='/accounts/login')
def create_post(request):
    current_user = request.user
    form = ImageForm()
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()

            return redirect("/")
    else:
        form = ImageForm()

    return render(request, 'new_photo.html', {'form': form})


@login_required(login_url='/accounts/login/')
def delete_image(request, image_id):
    current_user = request.user
    try:
        profile = Profile.objects.get(user = current_user)
    except Profile.DoesNotExist:
        raise Http404()

    try:
        image = Image.objects.get(id = image_id)
    except Image.DoesNotExist:
        raise Http404()   

    if image.user == current_user:
        image.delete_image()
        return redirect('snaps:myprofile')
    else:
        raise Http404()


@login_required(login_url='/accounts/login/')
def update_caption(request, image_id):
    current_user = request.user
    try:
        profile = Profile.objects.get(user = current_user)
    except Profile.DoesNotExist:
        raise Http404()

    try:
        image = Image.objects.get(id = image_id)
    except Image.DoesNotExist:
        raise Http404()

    if image.user == current_user:
        if 'newcaption' in request.GET and request.GET["newcaption"]:
            new_caption = request.GET.get("newcaption")
            image.caption = new_caption
            image.update_caption(new_caption)

            return redirect('snaps:myprofile')
        else:
            return render(request, 'new-caption.html', {"image":image})

    else:
        raise Http404()

        
def search(request):
    if request.GET['q']:
        users = Profile.search_by_username(request.GET['q'])

    return render(request, 'search.html', {'users': users})

def view_image(request, image_id):
    curr_image = Image.objects.filter(pk = image_id).first()
    return render(request, 'image_view.html', {'image': curr_image})


@login_required(login_url='/accounts/login')
def like_image(request, image_id):
    current_user = request.user
    image = Image.objects.filter(pk=image_id).first()
    user_image_likes = image.imagelike_set.filter(user = current_user).first()

    if image and not user_image_likes:
        image.likes += 1
        image.save()
        image_like = ImageLike(user=current_user, image = image)
        image_like.save()
    else:
        return redirect('/')

    return redirect('snaps:image', image_id)

def user_profile(request, username):
    search_user = User.objects.filter(username=username).first()

    if search_user:
        user_profile = search_user.profile
        user_followers = Followers.objects.filter(user = search_user).all()
        user_following = Followers.objects.filter(follower = search_user).all()

        all_images = Image.objects.filter(user = search_user).all()
    else:
        return redirect('index')

    return render(request, 'uprofile.html', {'profile': user_profile, 'images': all_images, 'followers': user_followers, 'following': user_following})


@login_required(login_url='/accounts/login')
def comment_image(request, image_id):
    current_user = request.user
    image = Image.objects.filter(pk = image_id).first()

    if request.method == 'GET':
        if image and request.GET.get('comment'):
            new_comment = Comment(user = current_user, image = image, comment=request.GET.get('comment'))
            new_comment.save()
            return redirect('snaps:image', image_id)
        else:
            return redirect('image', image_id)
    else:
        return redirect('/')


@login_required(login_url='/accounts/login')
def follow_user(request, user_id):
    current_user = request.user
    user_follow = Followers.objects.filter(follower=current_user).first()
    follow_user = User.objects.filter(pk = user_id).first()

    if follow_user is None:
        return redirect('/')

    if user_follow:
        return redirect('snaps:profile', follow_user.username)
    else:
        new_follow = Followers(user = follow_user, follower = current_user)
        new_follow.save()

    return redirect('snaps:profile', follow_user.username)


@login_required(login_url='/accounts/login')
def logout_user(request):
    logout(request)

    return redirect('/')