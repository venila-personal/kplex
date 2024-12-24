from django.urls import path
from employee import views

app_name = "employee"

urlpatterns = [
    
    path('', views.dashboard, name='dashboard'),
    path('room', views.room, name='room'),
    path('create_room', views.create_room, name='create_room'),
    path('update_room/<int:id>/', views.update_room, name='update_room'),
    path('delete_room/<int:id>/', views.delete_room, name='delete_room'),
    
    path('room/<int:room_id>/availability/', views.room_availability, name='room_availability'),  # This is the URL pattern
    path('book-room/', views.book_room, name='book_room'),
    path('generate-invoice/<int:id>/', views.generate_invoice, name='generate_invoice'),
    path('edit_booking/<int:booking_id>/', views.edit_booking, name='edit_booking'),
    path('cancel-booking/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
    
    path('quotation/', views.quotation, name='quotation'),
    path('create-quotation/', views.create_quotation, name='create_quotation'),
    path('print-quotation/<int:quotation_id>/', views.print_quotation, name='print_quotation'),
    path('update_quotation/<int:id>/', views.update_quotation, name='update_quotation'),
    path('delete_quotation/<int:id>/', views.delete_quotation, name='delete_quotation'),
    
    path('clients/', views.clients_report, name='clients_report'),
    path('rooms/', views.rooms_report, name='rooms_report'),
    path('available_rooms/', views.available_rooms_report, name='available_rooms_report'),
    path('quotation_report/', views.quotation_report, name='quotation_report'),
    path('enquiry_report/', views.enquiry_report, name='enquiry_report'),
    
    
    path('enquiry/', views.enquiry, name='enquiry'),
    path('create-enquiry/', views.create_enquiry, name='create_enquiry'),
    path('update_enquiry/<int:id>/', views.update_enquiry, name='update_enquiry'),
    path('delete_enquiry/<int:id>/', views.delete_enquiry, name='delete_enquiry'),
       
]

