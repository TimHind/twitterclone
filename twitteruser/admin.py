from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from twitteruser.models import MyUser

class CustomUserAdmin(UserAdmin):
        fieldsets = (
        *UserAdmin.fieldsets, 
        (                      
            'Custom Fields',  
            {
                'fields': (                    
                    'bio',
                    'following'              

                ),
            },
        ),
    )
admin.site.register(MyUser, CustomUserAdmin)
