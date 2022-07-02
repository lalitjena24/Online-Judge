from django.urls import path

from . import views

app_name = 'OJ'

urlpatterns = [
    path('problems/',views.problems, name='problem'),
    path('problem/<str:question_name>',views.problem_details,name='problem_details'),
]