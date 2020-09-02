from django.contrib import admin
from .models import Program, Workout


class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('title', 'Program', 'position', )
    list_filter = ('Program', 'position',)
    list_editable = ('position',)


admin.site.register(Program)
admin.site.register(Workout, WorkoutAdmin)
