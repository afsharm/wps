from django.contrib import admin
from .models import UserProfile
from .models import Workplace
from .models import Comment

admin.site.register(UserProfile)
admin.site.register(Workplace)
admin.site.register(Comment)
