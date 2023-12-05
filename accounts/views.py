from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.core.mail import send_mail


from .form import SignupForm , ActivationForm
from .models import Profile




def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.changed_data['username']
            email = form.changed_data['password']
            form.save()


            profile = Profile.objects.get(user__username=username)



            send_mail(
                "Activate Your Account",
                f"welcome {username} \n use this code {profile.code} to activate your account",
                "from@example.com", # my account
                ["email"],
                fail_silently=False,
            )


            return redirect ('/accounts/{username}/activate')



    else:
        form = SignupForm()
    return render(request,'registration/register.html',{'form':form})


def activate(request,username):
    pass


def profile(requecst):
    pass 