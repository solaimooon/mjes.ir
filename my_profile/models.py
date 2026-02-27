from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager



class MyUserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('Phone number must be provided')
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', 'operator')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(phone_number, password, **extra_fields)


class My_user(AbstractUser):
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    phone_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(blank=True, null=True)

    ROLE_CHOICES = [
        ('customer', 'Customer'),
        ('operator', 'Operator'),
        ('speaker', 'Speaker'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='customer')

    username = None  # چون از phone_number به‌جای username استفاده می‌کنیم
    password2 =None
    # تصریح کردیم که منیجر این مدل اینی هست که نوشتم
    objects = MyUserManager()

    def __str__(self):
        return f"{self.phone_number} ({self.get_role_display()})"


class Mosque_operator(models.Model):
    user = models.OneToOneField(My_user, on_delete=models.CASCADE, )
    national_id = models.CharField(max_length=10, blank=True, null=True)
    mosque = models.ForeignKey("rezervation.Mosque", on_delete=models.CASCADE)

    # سایر فیلدهای مربوط به مشتری
    def __str__(self):
        return f"{self.mosque.name}"



class Mosque_customer(models.Model):
    user = models.OneToOneField(My_user, on_delete=models.CASCADE, )
    mosque = models.ForeignKey("rezervation.Mosque", on_delete=models.CASCADE)
    adress = models.CharField(max_length=300)

    # سایر فیلدهای مربوط به مشتری
    def __str__(self):
        return f"{self.mosque.name}"