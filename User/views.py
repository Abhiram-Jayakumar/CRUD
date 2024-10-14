from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages

from User.models import UserProfile

def Index(request):
    return render(request,'User/index.html')

#///////////////////////////////////////////////////////////////////////////////////////

def register_user(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        address = request.POST['address']
        bio_description = request.POST['bio_description']
        password = request.POST['password']


        if UserProfile.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return redirect('User:register')

        user_profile = UserProfile(
            name=name,
            email=email,
            phone_number=phone_number,
            address=address,
            bio_description=bio_description,
            password=password 
        )
        user_profile.save()

        return redirect('User:Index')  

    return render(request, 'User/register.html')


#/////////////////////////////////////////////////////////////////////////////////////////////////////////

def user_list(request):
    users = UserProfile.objects.all()
    return render(request, 'User/user_list.html', {'users': users})



def user_detail(request, user_id):
    user = get_object_or_404(UserProfile, id=user_id)
    return render(request, 'User/user_detail.html', {'user': user})

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def update_user(request, user_id):
    user = get_object_or_404(UserProfile, id=user_id)

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        address = request.POST['address']
        bio_description = request.POST['bio_description']
        password = request.POST['password']

        user.name = name
        user.email = email
        user.phone_number = phone_number
        user.address = address
        user.bio_description = bio_description

        if password:
            user.password = password 

        user.save()  
        messages.success(request, "Profile updated successfully!")
        return redirect('User:user_detail', user_id=user.id) 

    return render(request, 'User/update_user.html', {'user': user})
#///////////////////////////////////////////////////////////////////////////////////////

def delete_user(request, user_id):
    user = get_object_or_404(UserProfile, id=user_id)

    if request.method == 'POST':
        user.delete()
        messages.success(request, "User deleted successfully!")
        return redirect('User:user_list')
