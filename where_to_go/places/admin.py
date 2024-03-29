from django.contrib import admin
from .models import Place, Image
from django.utils.html import format_html
from adminsortable2.admin import SortableTabularInline, SortableAdminMixin, SortableAdminBase


class ImageInline(SortableTabularInline):
    model = Image

    readonly_fields = ('get_preview',)
    fields = ('image', 'get_preview', 'position')

    def get_preview(self, obj):
        return format_html('<img src="{url}" style = "max-height: 200px;"/>', url=obj.image.url)

    get_preview.short_description = "Превью"


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


