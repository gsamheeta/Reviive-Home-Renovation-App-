from django.urls import path
from . import views

app_name = 'reviive'
urlpatterns = [
    # reviive_story views
    path('', views.reviive_list, name='reviive_list'),
    path('reviveStoryList', views.reviive_story_list, name='reviive_story_list'),
    path('getIdeas/', views.getIdeas, name='getIdeas'),
    path('findProf/', views.findProf, name='findProf'),
    path('budgetEstimation/', views.budgetEstimation, name='budgetEstimation'),
    path('findProf/customerReview/', views.customerReview, name='customerReview'),
    path('messageBox/', views.messageBox, name='messageBox'),
    path('renovationPriceGuide/', views.renovationPriceGuide, name='renovationPriceGuide'),
    path('contractors/', views.contractors, name='contractors'),
    path('reviveStoryList/edit/<int:renovation_id>/', views.edit_renovation, name='edit_renovation'),
    path('reviveStoryList/delete/<int:renovation_id>/', views.delete_renovation, name='delete_renovation'),
]