from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_event, name="book_event"),
    path('bookings/', views.show_bookings, name='bookings'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('user-login/', views.user_login, name='user_login'),
    path('user-logout/', views.user_logout, name='user_logout'),
    path('booking-details/<int:id>', views.view_booking, name='booking-details'),
    path('confirm-booking/<int:id>', views.confirm_booking, name='confirm-booking'),
    path('approved-bookings/', views.confirmed_booking, name='approved-bookings'),
    # path('confirm-payment/', views.confirm_payment, name='confirm-payment'),
]