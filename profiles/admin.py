from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):

    # list_display = ('name','password','email',)
    readonly_fields = ('password',)

    def save_model(self, request, obj, form, change):
        if not change:
            # obj.raw_password = obj.password
            obj.set_password(obj.raw_password)
        obj.save()

    def save_related(self, request, form, formsets, change):
        super(UserProfileAdmin, self).save_related(request, form, formsets, change)
        profile = form.instance
        # if not change:
        check_password = profile.check_password(profile.raw_password)
        if not check_password:
            # profile.raw_password = profile.password
            profile.set_password(profile.raw_password)
            profile.save()
            print(check_password) 

admin.site.register(UserProfile, UserProfileAdmin)
