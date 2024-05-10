from django.contrib import admin
from account.models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'nickname', 'birth', 'gender', 'email')

    search_fields = ['username']

admin.site.register(User, UserAdmin)

