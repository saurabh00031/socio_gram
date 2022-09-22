from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Reg_Profile)
admin.site.register(Reg_Post)
admin.site.register(Reg_LikePost)
admin.site.register(Reg_FollowersCount)