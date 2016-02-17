from django.contrib import admin
from .models import UserProfile
from .models import Workplace
from .models import Comment

class WorkplaceAdmin(admin.ModelAdmin):
	fields = ['province', 'city']

#admin.site.register(Workplace, WorkplaceAdmin)
admin.site.register(Workplace)
admin.site.register(UserProfile)
admin.site.register(Comment)
