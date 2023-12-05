from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings


from .form import SignupForm , ActivationForm
from .models import Profile




def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']


            user = form.save(commit=False)
            user.is_activate = False
            form.save()


            profile = Profile.objects.get(user__username=username)



            send_mail(
                "Activate Your Account",
                f"welcome {username} \n use this code {profile.code} to activate your account",
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )


            return redirect (f'/accounts/{username}/activate')



    else:
        form = SignupForm()
    return render(request,'registration/register.html',{'form':form})




def activate(request,username):
    profile = Profile.objects.get(user__username=username)
    if request.method == 'POST':
        form = ActivationForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            if code == profile.code:
                profile.code = ''

                user = User.objects.get(username=profile.user.username)
                user.is_activate = True
                user.save()
                profile.save()
                
                return redirect('/accounts/login')
            
    else:
        form = ActivationForm()

    return render(request, 'registration/activate.html', {'form': form})



def profile(requecst):
    pass 