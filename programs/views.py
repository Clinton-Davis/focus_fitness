from django.shortcuts import render
from django.views.generic import ListView, DetailView, View

from .models import Program, Workout


class ProgramListView(ListView):
    model = Program


class ProgramDetailView(DetailView):
    model = Program


class WorkoutDetailView(View):
    """ getting the workouts that are associated with the programs 
        and filtering by slug """

    def get(self, request, program_slug, workout_slug, *args, **kwargs):
        program_qs = Program.objects.filter(slug=program_slug)
        if program_qs.exists():
            program = program_qs.first()

        workout_qs = program.workouts.filter(slug=workout_slug)
        if workout_qs.exists():
            workout = workout_qs.first()

        context = {
            'object': workout
        }

        return render(request, "programs/workout_detail.html", context)
