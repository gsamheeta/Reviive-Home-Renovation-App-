from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

from actions.models import Action
from users.models import Details


def profile(request, username):
    user = get_object_or_404(User, username=username)
    actions = Action.objects.all().order_by('-created')

    if request.method == 'POST':
        # Get data from the form
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        # Update user object
        user.email = email
        user.first_name = first_name
        user.last_name = last_name


        # Save the updated user object
        user.save()

        # Redirect to the profile page or a success page
        return HttpResponseRedirect(reverse('users:profile', args=[username]))

    return render(request, "users/user/profile.html", {"user": user, "actions": actions})



# def profile(request, username):
#     user1 = get_object_or_404(User, username=username)
#     return render(request,
#                   "users/user/profile.html",
#                   {"user": user1}
#                   )


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        user = User.objects.create_user(username, email, password)

        # Set first_name and last_name
        user.first_name = first_name
        user.last_name = last_name

        # Save the user object with the updated fields
        user.save()

        messages.add_message(request, messages.SUCCESS,
                             "You successfully registered with the username: %s" % user.username)
        # messages.add_message(request, messages.SUCCESS, "Review Successfully Edited")
        return redirect('reviive:reviive_story_list')
    else:
        return render(request,
                      "users/user/register.html",
                      )




def login_user(request):
    request.session.flush()
    username = request.POST.get("username")
    pw = request.POST.get("pw")

    user = authenticate(username=username, password=pw)
    if user is not None:
        request.session['username'] = username
        request.session['role'] = user.details.role
        messages.add_message(request, messages.SUCCESS,
                             "You have logged in successfully.")
        auth_login(request, user)
        return redirect('reviive:reviive_story_list')
    else:
        messages.add_message(request, messages.ERROR,
                             "Invalid username or password.")
    return render(request, 'reviive/reviive_story/list.html')


def logout_user(request):
    del request.session['username']
    del request.session['role']
    return redirect('reviive:reviive_story_list')

@user_passes_test(lambda u: u.is_superuser)
def change_user_role(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        new_role = request.POST.get('role')

        # Update user role
        print(new_role)
        user = User.objects.get(id=user_id)
        if new_role == 'admin':
            user.is_superuser = True
            user.is_staff = True  # Generally, superusers are also staff
        else:
            user.is_superuser = False
            user.is_staff = False
        user_details = Details.objects.get(user=user)
        user_details.role = new_role
        user_details.save()
        user.save()
        return redirect('users:manage_users')

    users = User.objects.all()
    return render(request, 'users/user/manage_users.html', {'users': users})


def user_management(request):
    all_users = User.objects.all()
    return render(request, 'users/user/manage_users.html', {'all_users': all_users})





