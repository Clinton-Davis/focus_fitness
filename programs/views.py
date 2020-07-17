from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from memberships.models import UserMembership
from .models import Program, Workout


class ProgramListView(ListView):
    model = Program


class ProgramDetailView(DetailView):
    model = Program


class WorkoutDetailView(View):
    """ getting the workouts that are associated with the programs 
        and filtering by slug. Checks to see if the memebership type 
        is allowed to be viewed, if true, it adds it to contect."""

    def get(self, request, program_slug, workout_slug, *args, **kwargs):
        program_qs = Program.objects.filter(slug=program_slug)
        if program_qs.exists():
            program = program_qs.first()

        workout_qs = program.workouts.filter(slug=workout_slug)
        if workout_qs.exists():
            workout = workout_qs.first()

        user_membership = UserMembership.objects.filter(
            user=request.user).first()
        user_membership_type = user_membership.membership.membership_type

        program_allowed_mem_types = program.allowed_memberships.all()
        context = {
            'object': None
        }
        if program_allowed_mem_types.filter(membership_type=user_membership_type).exists():
            context = {
                'object': workout
            }

        return render(request, "programs/workout_detail.html", context)
