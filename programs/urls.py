from django.urls import path
from .views import ProgramListView, ProgramDetailView, WorkoutDetailView

app_name = 'programs'


urlpatterns = [

    path('', ProgramListView.as_view(), name='list'),
    path('<slug>', ProgramDetailView.as_view(), name='detail'),
    path('<program_slug>/<workout_slug>',
         WorkoutDetailView.as_view(), name='workout-detail'),



]
