from django.db import models


# Hair transplant section.
class Hair(models.Model):
    fullname = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    full = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"Name: {self.fullname} ===== Email: {self.email} ===== Phone Number: {self.phone}"


# Dentistry section.
class Dentist(models.Model):
    fullname = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    date_added = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"Name: {self.fullname} ===== Email: {self.email} ===== Phone Number: {self.phone}"


# Ophthalmology section.
class Optic(models.Model):
    fullname = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    date_added = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"Name: {self.fullname} ===== Email: {self.email} ===== Phone Number: {self.phone}"


# Plastic surgery section.
class Plastic(models.Model):
    fullname = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    date_added = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"Name: {self.fullname} ===== Email: {self.email} ===== Phone Number: {self.phone}"


# General treatment section.
class General(models.Model):
    fullname = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    date_added = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"Name: {self.fullname} ===== Email: {self.email} ===== Phone Number: {self.phone}"
