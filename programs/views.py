from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, DetailView, View
from memberships.models import UserMembership
from memberships.views import get_user_membership
from .models import Program, Workout


class ProgramListView(ListView):
    model = Program

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.info(request, "You Need to Login First")
            return redirect(reverse('account_login'))
        else:
            programs = Program.objects.all()

        context = {
            'programs': programs
        }
        return render(request, "programs/program_list.html", context)


class ProgramDetailView(DetailView):
    model = Program


class WorkoutDetailView(View):
    """ getting the workouts that are associated with the programs 
        and filtering by slug. Checks to see if the memebership type 
        is allowed to be viewed, if true, it adds it to context.
         (Logic and code from Mat @ JustDjango)"""

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
