from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterForm,ProfileUpdateForm,UserUpdateForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form =UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data.get('username')
            messages.success(request,f'Your account has been created! You are now able to login ')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form':form})


def profile_update(request):
    form = ProfileUpdateForm(request.POST or None, request.FILES or None, instance=request.user.profile)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect('profile')
    context = {'form' : form}
    return render(request, 'users/profile1.html', context=context)


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(data=request.POST, files=request.FILES,instance=request.user.profile)
        print(request.POST)
        img = request.POST.get('image')
        
        # print(p_form.cleaned_data)
        if u_form.is_valid() and p_form.is_valid(): 
            print(p_form.cleaned_data)
            instance = p_form.save(commit=False)
            instance.image = img
            print('inmg', img, instance.image)
            print(instance)
            instance.save()
            u_form.save()
            # p_form.save()
            messages.success(request,f'Your account has been updated! ')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request,'users/profile.html',context)