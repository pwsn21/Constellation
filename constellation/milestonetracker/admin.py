from django.contrib import admin
from .models import dops, user


#admin.site.register(dops)
admin.site.register(user)

@admin.register(dops)
class dopsadmin(admin.ModelAdmin):
    list_display = ('dops_date', 'mentor')
    ordering = ('-dops_date',)
    search_fields = ('mentor__first_name', 'mentor__last_name', 'mentor__employeenumber',)


