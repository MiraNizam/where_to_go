from adminsortable2.admin import (
    SortableAdminBase,
    SortableAdminMixin,
    SortableTabularInline,
)
from django.contrib import admin
from django.utils.html import format_html

from .models import Image, Place


class ImageInline(SortableTabularInline):
    model = Image

    readonly_fields = ("get_preview",)
    fields = ("image", "get_preview", "position")

    def get_preview(self, obj):
        return format_html(
            '<img src="{url}" style = "max-height: {height}px; max-width: {width}px"/>',
            url=obj.image.url,
            height=200,
            width=400
        )

    get_preview.short_description = "Превью"


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    raw_id_fields = ("place",)


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
