from django.shortcuts import render, redirect
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

        print("I got the form")
        if form.is_valid():
            print("Form was valid")
            image = form.save(commit=False)
            image.user = current_user
            image.save()

            return redirect("/")
    else:
        form = ImageForm()

    return render(request, 'new_photo.html', {'form': form})
        
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
        return redirect('snaps:index')

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
            return redirect('snaps:image', image_id)
    else:
        return redirect('snaps:index')

@login_required(login_url='/accounts/login')
def follow_user(request, user_id):
    current_user = request.user
    user_follow = Followers.objects.filter(follower=current_user).first()
    tobe_user = User.objects.filter(pk = user_id).first()

    if tobe_user is None:
        print("Did this")
        return redirect('snaps:index')

    if user_follow:
        return redirect('snaps:profile', tobe_user.username)
    else:
        new_follow = Followers(user = tobe_user, follower = current_user)
        new_follow.save()

    return redirect('snaps:profile', tobe_user.username)


@login_required(login_url='/accounts/login')
def logout_user(request):
    logout(request)

    return redirect('/')