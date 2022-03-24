from django.contrib import admin
# 追記
from drf_test_app.models import User,Question

# 追記
admin.site.register(User)
admin.site.register(Question)