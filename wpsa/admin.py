from django.contrib import admin
from .models import UserProfile
from .models import Workspace
from .models import Comment

admin.site.register(UserProfile)
admin.site.register(Workspace)
admin.site.register(Comment)
