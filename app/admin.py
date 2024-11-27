from django.contrib import admin
from .models import User, Admin, Room, Appointment, SpecialOffer, Feedback

# Register your models here.
admin.site.register(User),
admin.site.register(Admin),
admin.site.register(Room),
admin.site.register(Appointment),
admin.site.register(SpecialOffer),
admin.site.register(Feedback),
