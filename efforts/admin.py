from django.contrib import admin

# Register your models here.
from .models import Effort, Route, Split

# class RouteInline(admin.StackedInline):
#     model = Route

# class EffortAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,                  {'fields': ['']}),
#         ('Date information',    {'fields': ['pub_date'], 'classes': ['collapse']}),
#     ]
#     inlines = [RouteInline]

class SplitInline(admin.TabularInline):
    model = Split
    extra = 1

class EffortAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                  {'fields': ['user','route','total_time','total_distance']}),
        ('Date and Time',         {'fields': ['effort_time']}),
    ]
    inlines = [SplitInline]

admin.site.register(Effort, EffortAdmin)
admin.site.register(Route)
