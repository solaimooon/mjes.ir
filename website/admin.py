from django.contrib import admin
from django.contrib import admin
from .models import Category, Occasion, Night, MediaFile, style_media_file, owner,clip
from django.utils.html import format_html


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'نمایش_تصویر')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    fieldsets = (
        ('اطلاعات اصلی', {
            'fields': ('name', 'slug', 'image')
        }),
        ('تنظیمات سئو', {
            'fields': ('meta_title', 'meta_description'),
            'classes': ('collapse',)
        }),
    )

    def نمایش_تصویر(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="70" style="border-radius:8px;">', obj.image.url)
        return "—"
    نمایش_تصویر.short_description = 'تصویر دسته'


@admin.register(Occasion)
class OccasionAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'category', 'نمایش_تصویر')
    search_fields = ('name', 'year')
    list_filter = ('year', 'category')
    prepopulated_fields = {'slug': ('name',)}
    fieldsets = (
        ('اطلاعات مناسبـت', {
            'fields': ('category', 'name', 'year', 'slug', 'image')
        }),
        ('تنظیمات سئو', {
            'fields': ('meta_title', 'meta_description'),
            'classes': ('collapse',)
        }),
    )

    def نمایش_تصویر(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="70" style="border-radius:8px;">', obj.image.url)
        return "—"
    نمایش_تصویر.short_description = 'تصویر مناسبت'


@admin.register(Night)
class NightAdmin(admin.ModelAdmin):
    list_display = ('number', 'occasion', 'slug', 'نمایش_تصویر')
    list_filter = ('occasion',)
    search_fields = ('slug',)
    prepopulated_fields = {'slug': ('number',)}
    fieldsets = (
        ('اطلاعات شب', {
            'fields': ('occasion', 'number', 'slug', 'image')
        }),
        ('تنظیمات سئو', {
            'fields': ('meta_title', 'meta_description'),
            'classes': ('collapse',)
        }),
    )

    def نمایش_تصویر(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="70" style="border-radius:8px;">', obj.image.url)
        return "—"
    نمایش_تصویر.short_description = 'تصویر شب'


@admin.register(style_media_file)
class StyleMediaFileAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    verbose_name_plural = "استایل فایل‌ها"


@admin.register(owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    verbose_name_plural = "مداح یا قاری"


@admin.register(MediaFile)
class MediaFileAdmin(admin.ModelAdmin):
    list_display = ('title', 'media_type', 'night', 'date', 'نمایش_تصویر', 'Selected')
    list_filter = ('media_type', 'night__occasion', 'style_media_file', 'owner')
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('Selected',)
    fieldsets = (
        ('اطلاعات فایل رسانه‌ای', {
            'fields': ('night', 'file', 'media_type', 'title', 'slug', 'image')
        }),
        ('اطلاعات تکمیلی', {
            'fields': ('style_media_file', 'owner', 'date', 'Selected')
        }),
        ('تنظیمات سئو', {
            'fields': ('meta_title', 'meta_description'),
            'classes': ('collapse',)
        }),
    )

    def نمایش_تصویر(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="60" style="border-radius:8px;">', obj.image.url)
        return "—"
    نمایش_تصویر.short_description = 'تصویر'
@admin.register(clip)
class ClipAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "owner",
        "slug",
        "meta_title",
        "image_preview",
    )

    list_filter = ("owner",)
    search_fields = ("name", "slug", "meta_title", "meta_description")
    prepopulated_fields = {"slug": ("name",)}

    fieldsets = (
        ("اطلاعات اصلی", {
            "fields": ("name", "file", "image", "owner")
        }),
        ("سئو", {
            "classes": ("collapse",),
            "fields": ("meta_title", "meta_description"),
        }),
        ("سایر", {
            "fields": ("slug",),
        }),
    )

    readonly_fields = ("image_preview",)

    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="80" style="border-radius:5px;" />'
        return "بدون تصویر"
    image_preview.allow_tags = True
    image_preview.short_description = "پیش‌نمایش تصویر"

# فارسی‌سازی نام‌ها در پنل مدیریت
admin.site.site_header = "مدیریت محتوای رسانه‌ای هیئت"
admin.site.site_title = "مدیریت رسانه‌ها"
admin.site.index_title = "داشبورد مدیریت"

# Register your models here.
