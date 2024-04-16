from django.contrib import admin
from .models import Centralsection, Departmenthistory, Members, Picture, Video, Research


@admin.register(Centralsection)
class CentralsectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'updated_time']
    list_filter = ['title']
    search_fields = ['title']


@admin.register(Departmenthistory)
class DepartmenthistoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'updated_time']
    list_filter = ['title']
    search_fields = ['title']


# class MembersInline(admin.TabularInline):
#     model = MembersExpert
#     fk_name = 'members'


@admin.register(Members)
class MembersAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'updated_time']
    list_filter = ['title']
    search_fields = ['title']
    # inlines = [MembersInline]


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'updated_time']
    list_filter = ['title']
    search_fields = ['title']


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'updated_time']
    list_filter = ['title']
    search_fields = ['title']


@admin.register(Research)
class ResearchAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'updated_time']
    list_filter = ['title']
    search_fields = ['title']