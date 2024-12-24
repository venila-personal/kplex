from django.db import models
from django.forms import ValidationError

# Create your models here.
class Room(models.Model):
    ROOM_TYPES = [
        ('Meeting Room', 'Meeting Room'),
        ('Auditorium', 'Auditorium'),
        ('Office', 'Office'),
    ]
    name = models.CharField(max_length=50)
    room_type = models.CharField(max_length=20, choices=ROOM_TYPES)
    sheet_count = models.PositiveIntegerField()
    price_per_sheet = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    amenities = models.TextField(default="Tea, Coffee, Pantry, WiFi")

    def __str__(self):
        return self.name
    
    @property
    def available_sheets(self):
        # Replace with actual logic for booked sheets if necessary
        booked_sheets = 0  # Calculate booked sheets dynamically
        return self.sheet_count - booked_sheets
    
class Booking(models.Model):
    BOOKING_TYPES = [
        ('DAILY', 'Date Range'),
        ('MONTHLY', 'Monthly'),
        ('YEARLY', 'Yearly'),
    ]
    STATUS_CHOICES = [
        ('ACTIVE', 'Active'),
        ('CANCELED', 'Canceled'),
        ('COMPLETED', 'Completed'),
    ]

    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=100)
    sheets_booked = models.PositiveIntegerField()
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    booking_type = models.CharField(max_length=10, choices=BOOKING_TYPES, default='DAILY')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ACTIVE')
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    final_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.client_name} - {self.room.name} ({self.sheets_booked} sheets)"


class Quotation(models.Model):
    BOOKING_TYPES = [
        ('DAILY', 'Date Range'),
        ('MONTHLY', 'Monthly'),
        ('YEARLY', 'Yearly'),
    ]
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Cancelled', 'Cancelled'),
        ('Convert', 'Convert'),
    ]
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=100)
    sheets_booked = models.PositiveIntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    booking_type = models.CharField(max_length=10, choices=BOOKING_TYPES, default='DAILY')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    final_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Quotation for {self.client_name} ({self.room.name})"
    
    
    
    
class Enquiry(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Cancelled', 'Cancelled'),
        ('Convert', 'Convert'),
    ]
    ROOM_TYPES = [
        ('Meeting Room', 'Meeting Room'),
        ('Auditorium', 'Auditorium'),
        ('Office', 'Office'),
    ]

    client_name = models.CharField(max_length=100)
    employee_name = models.CharField(max_length=100)
    room_type = models.CharField(max_length=20, choices=ROOM_TYPES)
    required_sheets = models.PositiveIntegerField()
    from_date = models.DateField()
    to_date = models.DateField()
    referenced_by=models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    remarks = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    offer_price=models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    def clean(self):
        # Ensure from_date is before to_date
        if self.from_date > self.to_date:
            raise ValidationError("From date must be before or equal to To date.")

    def __str__(self):
        return f"Enquiry by {self.client_name} "

        