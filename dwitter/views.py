from django.shortcuts import render, redirect
from dwitter.models import Profile, Dweet
from dwitter.forms import DweetForm
# from django.http import HttpResponse, JsonResponse
# Create your views here.

def dashboard(request):
    message=""
    form = DweetForm(request.POST or None)
    if request.method == "POST":
       if form.is_valid():
           dweet = form.save(commit=False)#creates & returns model instance from the form , but it does not save it to the database.
           dweet.user = request.user
           dweet.save()
           return redirect('dwitter:dashboard')
    followed_dweet = Dweet.objects.filter(user__profile__in = request.user.profile.follows.all()) .order_by("-created_at")
    data = {
        "dweets": followed_dweet,
        "form" : form ,
        "message": message
    }
    return render(request, "dwitter/dashboard.html", data)


def profile_list(request):
    data = {
        "profiles" : Profile.objects.all()
    }
    return render(request, "dwitter/profile_list.html",data )


def profile(request, pk ):

    user_dweet = Dweet.objects.filter(user = request.user) .order_by("-created_at")
    profile = Profile.objects.get(pk=pk)

    if not hasattr(request.user, 'profile'):
        missing_profile = Profile(user=request.user)
        missing_profile.save()

    if request.method =="POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.follows.add(profile)
        if action == "unfollow":
            current_user_profile.follows.remove(profile)
        current_user_profile.save()


    data ={
        "dweets" :user_dweet, 
        "profile" :  profile
    }
    # return JsonResponse(data )
    return render(request,"dwitter/profile.html", data )
