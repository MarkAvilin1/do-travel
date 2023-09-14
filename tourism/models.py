from django.db import models


# Ticket section.
class Ticket(models.Model):
    fullname = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"Name: {self.fullname} ===== Email: {self.email} ===== Phone Number: {self.phone}"


# Booking section.
class Booking(models.Model):
    fullname = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"Name: {self.fullname} ===== Email: {self.email} ===== Phone Number: {self.phone}"


# Trips section.
class Trip(models.Model):
    fullname = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"Name: {self.fullname} ===== Email: {self.email} ===== Phone Number: {self.phone}"


# Visas section.
class Visa(models.Model):
    fullname = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"Name: {self.fullname} ===== Email: {self.email} ===== Phone Number: {self.phone}"


# Education Services.
class Education(models.Model):
    fullname = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"Name: {self.fullname} ===== Email: {self.email} ===== Phone Number: {self.phone}"
