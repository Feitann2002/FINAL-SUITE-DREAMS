from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from decimal import Decimal
from django.core.validators import MinValueValidator, MaxValueValidator


class Admin(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username


class User(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    username = models.CharField(max_length=150, unique=True, default='')
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Room(models.Model):
    room_number = models.CharField(max_length=10, unique=True)
    room_type = models.CharField(max_length=30)
    capacity = models.CharField(max_length=30)
    price_per_hour = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Room {self.room_number} - {self.room_type}"

    class Meta:
        ordering = ['room_number']


class SpecialOffer(models.Model):
    room = models.ManyToManyField(Room)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    description = models.TextField()

    def clean(self):
        if self.start_date >= self.end_date:
            raise ValidationError("Start date must be before end date.")

    def __str__(self):
        room_numbers = ', '.join([room.room_number for room in self.room.all()])
        return f"Special Offer for Rooms {room_numbers}: {self.discount_percentage}%"


class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.start_date < timezone.now():
            raise ValidationError("Start date cannot be in the past.")
        if self.start_date >= self.end_date:
            raise ValidationError("End date must be after start date.")

        overlapping_appointments = Appointment.objects.filter(
            room=self.room,
            start_date__lt=self.end_date,
            end_date__gt=self.start_date
        )
        if overlapping_appointments.exists():
            raise ValidationError("The room is already booked for the selected dates.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    @property
    def total_cost(self):
        return self.calculate_total_cost()

    def calculate_total_cost(self):
        total_hours = (self.end_date - self.start_date).total_seconds() / 3600.0
        if total_hours < 0:
            return Decimal('0.00')

        total_cost = Decimal(total_hours) * self.room.price_per_hour

        applicable_offer = SpecialOffer.objects.filter(
            room=self.room,
            start_date__lte=self.start_date,
            end_date__gte=self.end_date
        ).first()

        if applicable_offer:
            discount_amount = total_cost * (applicable_offer.discount_percentage / Decimal('100'))
            total_cost -= discount_amount

        return total_cost

    def __str__(self):
        return f"Appointment by {self.user.name} for {self.room.room_number}"


class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        validators=[MinValueValidator(Decimal('1.0')), MaxValueValidator(Decimal('5.0'))]
    )
    comments = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.name
