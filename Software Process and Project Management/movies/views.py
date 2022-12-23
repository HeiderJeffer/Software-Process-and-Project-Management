from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from requests.packages.urllib3 import request
import json
from django import template
from django.http import HttpResponse
from .models import Movie, User, WishList, Rating


register = template.Library()
def index(request):
    return render(request, 'movies/home.html')

def login(request):
    if request.method == 'POST':
        # collecting form data
        username = request.POST.get('username')
        password = request.POST.get('password')
        # checking for user first
        user = authenticate(username=username, password=password)
        print user
        if user is not None:
            if user.is_active:
                # check if it is quest or manager
                # search for guest
                user = User.objects.get(username=username)
                auth_login(request, user)
                #return HttpResponseRedirect(reverse('movies:user', args=(user.id,)))
                return HttpResponseRedirect(reverse('home'))
            else:
                return render(request, 'movies/login.html', {
                    'error_message': "Account is not activated!"
                })
        else:
            return render(request, 'movies/login.html', {
                'error_message': "Wrong Email address or Password!"
            })
    else:
        return render(request, 'movies/login.html')

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('home'))

def register(request):
    return render(request, 'movies/register.html')

def registration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_confirm = request.POST.get('cpassword')
        if password == password_confirm:
            users = User.objects.all()
            for u in users:
                if u.username == username:
                    return render(request, 'movies/register.html', context={
                        'error_message':"User already exists!"
                    })
            new_user = User.objects.create_user(username, username, password)
            new_user.is_staff = False
            new_user.is_active = True
            new_user.is_superuser = False
            new_user.save()
            return render(request, 'movies/register.html', context={
                'info_message': "Account created successfully. Now you can login with you account!"
            })
        else:
            return render(request, 'movies/register.html', context={
                'error_message': "Password does not match the confirm password."
            })

@login_required(login_url='/')
def profile(request, user_id):
    this_user = get_object_or_404(User, pk=user_id)
    right_now = timezone.now()
    return render(request, 'movies/profile.html', context={
        'user': this_user,
        'time': right_now
    })

#class IndexView(generic.ListView):
 #   template_name = 'movies/index.html'
 #   context_object_name = 'latest_movie_list'

 #   def get_queryset(self):
  #      return Movie.objects.order_by('id')[:20]

def listing(request):
    movie_list = Movie.objects.order_by('id')
    if request.user.is_authenticated():
        try:
            wish_list = WishList.objects.values_list('movieId_id',flat=True).filter(userId_id=request.user.id)
            wish_list = list(wish_list)
            print wish_list
        except WishList.DoesNotExist:
            wish_list = None
    else:
        wish_list = None
    if wish_list !=None:
        for movie in movie_list:
            if movie.id in wish_list:
                movie.wishlist = True
    paginator = Paginator(movie_list, 20) 

    page = request.GET.get('page')
    try:
        movies = paginator.page(page)
    except PageNotAnInteger:
        movies = paginator.page(1)
    except EmptyPage:
        movies = paginator.page(paginator.num_pages)

    return render(request, 'movies/index.html', {'movies': movies})

def show_wish_list(request,user_id):
 
    try:
        wish_list = WishList.objects.values_list('movieId_id',flat=True).filter(userId_id=user_id)
        movie_list = Movie.objects.filter(id__in=wish_list)
        paginator = Paginator(movie_list, 20) 

        page = request.GET.get('page')
        try:
            movies = paginator.page(page)
        except PageNotAnInteger:
            movies = paginator.page(1)
        except EmptyPage:
            movies = paginator.page(paginator.num_pages)
        print movie_list
    except WishList.DoesNotExist:
        movies = None
    return render(request, 'movies/wishlist.html', {'movies':movies})

def add_to_wish_list(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        movie_id = json_data["movie_id"]
        user_id = json_data["user_id"]
        wished_movie= WishList(movieId_id= movie_id, userId_id= user_id)
        wished_movie.save()
    return HttpResponse(json.dumps({"success":"ok"}), content_type='application/json')

def remove_from_wish_list(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        movie_id = json_data["movie_id"]
        user_id = json_data["user_id"]
        WishList.objects.filter(movieId_id=movie_id, userId_id= user_id).delete()   
    return HttpResponse(json.dumps({"success":"ok"}), content_type='application/json')

def rate(request):
    if request.method == 'POST':
        rating = request.POST.get('rating')
        userID = request.POST.get('user_id')
        userID = User.objects.get(pk=userID)
        movieID = request.POST.get('movie_id')
        movieID = Movie.objects.get(pk=movieID)

        rate = Rating(userId=userID, movieId=movieID, rating=rating)
        rate.save()       
    return HttpResponseRedirect(reverse('movies:detail', args=(movieID.id,)))


@login_required(login_url='/')
def update(request, user_id):
    this_user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        updated_user = User.objects.get(pk=user_id)
        users = User.objects.all()
        for u in users:
            if u.username == username and username != updated_user.username:
                return render(request, 'movies/profile.html', context={
                    'error_message': "Username already taken!"
                })
        updated_user.username = username
        updated_user.first_name = first_name
        updated_user.last_name = last_name
        updated_user.email = email
        updated_user.save()
    return HttpResponseRedirect(reverse('movies:profile', args=(user_id,)))



def detail(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    isRated = 0
    if request.user.id:
    	user = User.objects.get(pk=request.user.id)
    	isRated = Rating.objects.filter(movieId_id=movie.id, userId_id=user.id)
    return render(request, 'movies/detail.html', {'movie': movie, 'isRated': isRated})


