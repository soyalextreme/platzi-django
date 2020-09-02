from django.contrib import admin

# models
from posts.models import Post

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("pk", "user", "title", "photo")
    list_editable = ("title", )
    search_fields = ("title", "user__pk", "pk")
    list_filter = (
        "created",
        "modified",
    )
    list_display_links = ("user", )

    readonly_fields = ("created", "modified")
