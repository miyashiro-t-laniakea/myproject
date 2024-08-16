from django.contrib import admin
from .models import Vehicle, RepairJob

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('make', 'model', 'year')
    search_fields = ('make', 'model')

@admin.register(RepairJob)
class RepairJobAdmin(admin.ModelAdmin):
    list_display = ('description', 'vehicle', 'status', 'start_date', 'end_date')
    list_filter = ('status', 'vehicle')
    search_fields = ('description', 'vehicle__make', 'vehicle__model')