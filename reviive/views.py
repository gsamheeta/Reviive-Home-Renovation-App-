
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from actions.models import Action
from reviive.forms import RenovationForm
from reviive.models import RenovationPrice
from .models import regular_user

# Create your views here.


def reviive_list(request):
    return render(request, "reviive/reviive_story/login.html")


def reviive_story_list(request):
    # if request.session.get("username", False):
        actions = Action.objects.all().order_by('-created')

        return render(request,
                      "reviive/reviive_story/list.html",
                      {"actions": actions}
                      )


def getIdeas(request):
        return render(request,
                      "reviive/reviive_story/getIdeas.html")


def findProf(request):
    if request.session.get("username", False):

        actions = Action.objects.all().order_by('-created')

        return render(request,
                  "reviive/reviive_story/findProf.html",
        {"actions": actions}
                      )


def budgetEstimation(request):
    return render(request,
                  "reviive/reviive_story/budgetEstimation.html")


def customerReview(request):

        if request.method == 'POST':
            # process the form
            title = request.POST.get('add-title')
            price = request.POST.get('add-description')
            name = request.session['username']
            # name = request.POST.get('add-name')
            # User.objects.filter()
            # print(title, price, name)

            rp = RenovationPrice(
                item=title,
                price=price,
                name=name,
            )
            rp.save()

            # log the action
            action = Action(
                user=name,
                verb="review added by",
                # target_id=rp
            )
            action.save()

            messages.add_message(request, messages.SUCCESS, "You successfully added a review: %s" % rp.item)

            return redirect("reviive:renovationPriceGuide")
        else:
            #show the form
            return render(request,
                  "reviive/reviive_story/customerReview.html")


def messageBox(request):
    return render(request,
                  "reviive/reviive_story/messageBox.html")


def edit_renovation(request, renovation_id):
    print(renovation_id)
    renovation = get_object_or_404(RenovationPrice, id=renovation_id)
    if request.method == 'POST':
        form = RenovationForm(request.POST, instance=renovation)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, "Review Successfully Edited")
            return redirect('reviive:renovationPriceGuide')  # Redirect to the list view or any other appropriate view
    else:
        form = RenovationForm(instance=renovation)

    return render(request, 'reviive/reviive_story/edit_renovation.html', {'form': form})


def delete_renovation(request, renovation_id):
    renovation = get_object_or_404(RenovationPrice, id=renovation_id)
    if request.method == 'POST':  # Confirm deletion
        renovation.delete()
        messages.add_message(request, messages.WARNING, "Review Successfully Deleted")
        return redirect('reviive:renovationPriceGuide')  # Redirect to the list view or any other appropriate view
    return render(request, 'reviive/reviive_story/confirm_delete.html', {'renovation': renovation})



def contractors(request):
    return render(request,
                  "reviive/reviive_story/contractors.html",
                  )


def renovationPriceGuide(request):
        renovations = RenovationPrice.objects.all()
        context = {"renovations": renovations
                   }
        return render(request,
                      "reviive/reviive_story/renovationPriceGuide.html",
                      context
                      )

# def login(request):
#     username = request.POST.get("username")
#     pw = request.POST.get("pw")
#     if(username == regular_user['username']) and (pw == regular_user['password']):
#         request.session['username'] = username
#         request.session['role'] = 'regular'
#         return redirect('reviive:reviive_story_list')
#     else:
#         return redirect('reviive:reviive_story_list')
#
# def logout(request):
#     del request.session['username']
#     del request.session['role']
#     return redirect('reviive:reviive_story_list')
