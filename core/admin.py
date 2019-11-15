from django.contrib import admin

from .models import CarType, Post, User

try:
    User.objects.create_superuser("user", "user@user.user", "user")
except:
    pass


class CarTypeAdmin(admin.ModelAdmin):
    list_display = ('model', 'contaminationRate')
    search_fields = ['model']


admin.site.register(CarType, CarTypeAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']


admin.site.register(Post, PostAdmin)
