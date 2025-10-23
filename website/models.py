from django.db import models
from django_jalali.db import models as jmodels


class Category(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name="نام دسته‌بندی"
    )
    slug = models.CharField(
        max_length=100,
        verbose_name="نامک (slug)"
    )
    image = models.ImageField(
        "تصویر دسته‌بندی",
        upload_to="media_category_picture"
    )

    # SEO Fields
    meta_title = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="عنوان سئو"
    )
    meta_description = models.TextField(
        blank=True,
        null=True,
        verbose_name="توضیحات سئو"
    )

    class Meta:
        verbose_name = "دسته‌بندی"
        verbose_name_plural = "دسته‌بندی‌ها"

    def __str__(self):
        return f"{self.name}"


class Occasion(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="occasions",
        verbose_name="دسته‌بندی"
    )
    name = models.CharField(
        max_length=200,
        help_text="مثلاً: دهه اول ماه محرم 1404",
        verbose_name="عنوان مناسبت"
    )
    year = models.IntegerField(verbose_name="سال")
    slug = models.CharField(max_length=100, verbose_name="نامک (slug)")
    image = models.ImageField(
        upload_to='media_night',
        default='null',
        verbose_name="تصویر مناسبت"
    )

    # SEO Fields
    meta_title = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="عنوان سئو"
    )
    meta_description = models.TextField(
        blank=True,
        null=True,
        verbose_name="توضیحات سئو"
    )

    class Meta:
        verbose_name = "مناسبت"
        verbose_name_plural = "مناسبت‌ها"

    def save(self, *args, **kwargs):
        if self.name:
            self.slug = self.name
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.year})"


class style_media_file(models.Model):
    name = models.CharField(max_length=50, verbose_name="نام سبک فایل")

    class Meta:
        verbose_name = "سبک فایل "
        verbose_name_plural = "سبک های فایل "

    def __str__(self):
        return self.name


class Night(models.Model):
    occasion = models.ForeignKey(
        Occasion,
        on_delete=models.CASCADE,
        related_name="nights",
        verbose_name="مناسبت"
    )
    number = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="شماره شب"
    )
    slug = models.CharField(
        max_length=100,
        help_text="این فیلد به عنوان نام شب در کد استفاده می‌شود",
        verbose_name="نامک (slug)"
    )
    image = models.ImageField(
        upload_to='media_night',
        default='null',
        verbose_name="تصویر شب"
    )

    # SEO Fields
    meta_title = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="عنوان سئو"
    )
    meta_description = models.TextField(
        blank=True,
        null=True,
        verbose_name="توضیحات سئو"
    )

    class Meta:
        verbose_name = "شب"
        verbose_name_plural = "شب‌ها"

    def __str__(self):
        return f"شب {self.number} - {self.occasion}"


class owner(models.Model):
    name = models.CharField(max_length=50, verbose_name="نام صاحب اثر (مداح یا سخنران)")

    class Meta:
        verbose_name = "صاحب اثر"
        verbose_name_plural = "صاحبان اثر"

    def __str__(self):
        return self.name


class MediaFile(models.Model):
    MEDIA_TYPE_CHOICES = [
        ('audio', 'صوتی'),
        ('video', 'ویدئویی'),
    ]

    night = models.ForeignKey(
        Night,
        on_delete=models.CASCADE,
        related_name="media_files",
        verbose_name="شب"
    )
    file = models.FileField(
        upload_to='media/',
        verbose_name="فایل "
    )
    media_type = models.CharField(
        max_length=10,
        choices=MEDIA_TYPE_CHOICES,
        verbose_name="نوع مدیا"
    )
    title = models.CharField(max_length=200, verbose_name="عنوان فایل")
    slug = models.CharField(max_length=100, verbose_name="نامک (slug)")
    image = models.ImageField(
        upload_to='media_night',
        default='null',
        verbose_name="تصویر نمایه"
    )
    style_media_file = models.ForeignKey(
        style_media_file,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="سبک مدیا(سخنرانی،زمینه،شور...)"
    )
    owner = models.ForeignKey(
        owner,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="صاحب اثر"
    )
    date = jmodels.jDateField(
        null=True,
        blank=True,
        verbose_name="تاریخ انتشار"
    )
    Selected = models.BooleanField(
        null=True,
        blank=True,
        verbose_name="نمایش در صفحه اصلی"
    )

    # SEO Fields
    meta_title = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="عنوان سئو"
    )
    meta_description = models.TextField(
        blank=True,
        null=True,
        verbose_name="توضیحات سئو"
    )

    class Meta:
        verbose_name = "فایل رسانه‌ای"
        verbose_name_plural = "فایل‌های رسانه‌ای"

    def __str__(self):
        return self.title


class clip(models.Model):
    name=models.CharField(max_length=50,verbose_name="تیتر")
    file=models.FileField(upload_to='media/',
        verbose_name="فایل ")
    slug=models.CharField(max_length=50)
    image=models.ImageField(upload_to='media_night',
        default='null',
        verbose_name="تصویر نمایه")

    owner = models.ForeignKey(
        owner,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="صاحب اثر"
    )

    meta_title = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="عنوان سئو"
    )
    meta_description = models.TextField(
        blank=True,
        null=True,
        verbose_name="توضیحات سئو"
    )

    class Meta:
        verbose_name = " کلیپ"
        verbose_name_plural = " کلیپ ها"
