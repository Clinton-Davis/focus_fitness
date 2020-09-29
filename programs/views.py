from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from memberships.models import UserMembership
from .models import Program, Workout


class ProgramListView(ListView):
    model = Program
    context_object_name = 'programs'


class ProgramDetailView(LoginRequiredMixin, DetailView):
    model = Program
    context_object_name = 'programs'


class WorkoutDetailView(LoginRequiredMixin, View):

    """Getting the workouts that are associated with the programs 
        and filtering by slug. Checks to see if the memebership type
        is allowed to be viewed, if true, it adds it to context.
         (Logic and code from Mat @ JustDjango) Understood and implemented."""

    def get(self, request, program_slug, workout_slug, *args, **kwargs):
        get_program = Program.objects.filter(slug=program_slug)
        if get_program.exists():
            program = get_program.first()

        get_workout = program.workouts.filter(slug=workout_slug)
        if get_workout.exists():
            workout = get_workout.first()

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
