# from django.db import models
# from django.urls import reverse
# from django.contrib.sites.models import Site
# from my_profile.models import *
#
#
# class Facility(models.Model):
#     name = models.CharField(max_length=100)
#     icon = models.ImageField(upload_to='facility_icons/', blank=True, null=True)
#
#     def __str__(self):
#         return self.name
#
#
# class Mosque(models.Model):
#     name = models.CharField(max_length=200)
#     slug = models.CharField(max_length=200,unique=True)
#     rigen = models.TextField()
#     address = models.TextField()
#     description = models.TextField(blank=True, null=True)
#     logo = models.ImageField(upload_to='mosques/logos/', blank=True, null=True)
#     latitude = models.FloatField(blank=True, null=True)
#     longitude = models.FloatField(blank=True, null=True)
#     facilities = models.ManyToManyField('Facility', related_name='mosques', blank=True)
#
#     # 🔹 فیلدهای سئو
#     meta_title = models.CharField(max_length=255, blank=True, null=True)
#     meta_description = models.TextField(blank=True, null=True)
#
#     def __str__(self):
#         return self.name
#
#     def get_absolute_url(self):
#         return reverse('mosque_detail', kwargs={'slug': self.slug})
#
#
#
# class Hall(models.Model):
#     type_hall = [
#         ("salonejtemaat", 'سالن اجتماعات'),
#         ("sahne_asli", 'صحن اصلی'),
#     ]
#     mosque = models.ForeignKey('Mosque', related_name='halls', on_delete=models.CASCADE,)
#     name = models.CharField(max_length=200)
#     capacity = models.PositiveIntegerField()
#     is_active = models.BooleanField(default=True)
#     facilities = models.ManyToManyField('Facility', related_name='halls', blank=True)
#     video_file = models.FileField(upload_to='videos/',null=True,blank=True)  # ذخیره در پوشه media/videos/
#
#     price = models.IntegerField(null=True,
#         help_text='قیمت پایه رزرو سالن به تومان'
#     )
#     type_hall=models.CharField(max_length=50, choices=type_hall,default="salonejtemaat")
#     def __str__(self):
#         return f"{self.name} ({self.mosque.name})"
#
#
# class HallImage(models.Model):
#     hall = models.ForeignKey(Hall, related_name='images', on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='halls/images/')
#     caption = models.CharField(max_length=255, blank=True)
#
#
#     def __str__(self):
#         return f"Image for {self.hall.name}"
#
#
# # بازه‌های زمانی قابل رزرو برای هر مسجد
# class AvailableTime(models.Model):
#     DAYS_OF_WEEK = [
#         (0, 'شنبه'),
#         (1, 'یک‌شنبه'),
#         (2, 'دوشنبه'),
#         (3, 'سه‌شنبه'),
#         (4, 'چهارشنبه'),
#         (5, 'پنج‌شنبه'),
#         (6, 'جمعه'),
#     ]
#
#     Hall = models.ForeignKey(Hall, on_delete=models.CASCADE, related_name='available_times')
#     day_of_week = models.IntegerField(choices=DAYS_OF_WEEK)
#     start_time = models.TimeField()
#     end_time = models.TimeField()
#
#     def __str__(self):
#         return f"{self.get_day_of_week_display()} | {self.start_time} - {self.end_time} "
#
#     class Order(models.Model):
#         STATUS_CHOICES = [
#             ('pending', 'در انتظار پرداخت'),
#             ('paid', 'پرداخت شده'),
#             ('cancelled', 'لغو شده'),
#         ]
#
#         type_of_rezerve=[
#             ('khatm_sevom&haftom',"ختم(مراسم سوم و هفتم)"),
#             ('khatm_chehelom', "ختم(مراسم چهلم)"),
#             ('khatm_chehelom', "ختم(سالگرد)"),
#             ('amozesh_confrince', "آموزش_کنفرانس"),
#             ('valime', "ولیمه")
#         ]
#
#         user = models.ForeignKey(Mosque_customer, on_delete=models.CASCADE)
#         Hall = models.ForeignKey('Hall', on_delete=models.CASCADE)
#         available_time = models.ForeignKey("AvailableTime", on_delete=models.RESTRICT)
#         date = models.DateField()  # تاریخ خاص (مثلاً 1403-08-01)
#         price = models.PositiveIntegerField(default=0)
#         status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
#         type_of_rezerve=models.CharField(max_length=50,choices=type_of_rezerve)
#         created_at = models.DateTimeField(auto_now_add=True)
#
#         def __str__(self):
#             return f"{self.user} رزرو {self.mosque} - {self.date} ({self.available_time})"
#
