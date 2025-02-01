from django.contrib import admin

# Register your models here.

from main_app.models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("model", "year", "owner", "car_details")

    @staticmethod
    def car_details(obj:Car):
        try:
            owner_name = obj.owner.name
        except AttributeError:
            owner_name = 'No owner'

        try:
            registration = obj.registration.registration_number
        except AttributeError:
            registration = 'No registration number'

        return f"Owner: {owner_name}, Registration: {registration}"

    car_details.short_description = 'Car Details'


