from django.urls import path
from . import views
from .views import (BasePageView, DatabasePageView, HomePageView, AboutPageView, ContactPageVew, OfferListView,
                    FAQsPageView, PrivacyPolicyPageView, TermsAndConditionView, FeedbackListView, OfferDetailView,
                    UserSplashView, AdminCreateView, AdminUpdateView, AdminDeleteView, AppointmentDetailView,
                    register, login, admin_login, account_settings, AppointmentUpdateView, AppointmentCreateView,
                    UserCreateView, UserUpdateView, UserDeleteView, RoomCreateView, RoomUpdateView, RoomDeleteView,
                    PartnersPageView, FooterPageView, RoomSliderPageView, RoomPageView, Appointment2CreateView,
                    Appointment2DeleteView, Appointment2UpdateView, SpecialOfferCreateView, SpecialOfferUpdateView,
                    FeedbackCreateView, FeedbackUpdateView, Feedback2DeleteView, SpecialOffer2DeleteView,)

urlpatterns = [
    path('', BasePageView.as_view(), name='base'),
    path('register/', register, name='register'),
    path('user_login/', login, name='login'),
    path('user_splash/', UserSplashView.as_view(), name='user_splash'),
    path('admin_login/', admin_login, name='admin_login'),
    path('listview/', OfferListView.as_view(), name='listview'),
    path('detail_view/<int:pk>', OfferDetailView.as_view(), name='detail_view'),
    path('database/', DatabasePageView.as_view(), name='database'),
    path('feedback/add/', views.add_feedback, name='add-feedback'),
    path('account_settings/', account_settings, name='account_settings'),
    path('appointments/edit/<int:pk>/', AppointmentUpdateView.as_view(), name='edit_appointment'),
    path('book_appointment/', AppointmentCreateView.as_view(), name='book_appointment'),

    path('appointment/<int:pk>/', AppointmentDetailView.as_view(), name='appointment_detail'),
    path('dbadmin/create', AdminCreateView.as_view(), name='create_admin'),
    path('dbadmin/<int:pk>/edit', AdminUpdateView.as_view(), name='admin_update'),
    path('dbadmin/<int:pk>/delete', AdminDeleteView.as_view(), name='admin_delete'),

    path('adduser/create', UserCreateView.as_view(), name='create_user'),
    path('dbuser/<int:pk>/edit', UserUpdateView.as_view(), name='user_update'),
    path('dbuser/<int:pk>/delete', UserDeleteView.as_view(), name='user_delete'),

    path('addroom/create', RoomCreateView.as_view(), name='create_room'),
    path('dbroom/<int:pk>/edit', RoomUpdateView.as_view(), name='room_update'),
    path('dbroom/<int:pk>/delete', RoomDeleteView.as_view(), name='room_delete'),

    path('addappointment/create', Appointment2CreateView.as_view(), name='create_appointment'),
    path('dbappointment/<int:pk>/edit', Appointment2UpdateView.as_view(), name='appointment_update'),
    path('dbappointment/<int:pk>/delete', Appointment2DeleteView.as_view(), name='appointment_delete'),

    path('addoffer/create', SpecialOfferCreateView.as_view(), name='create_offer'),
    path('dboffer/<int:pk>/edit', SpecialOfferUpdateView.as_view(), name='offer_update'),
    path('delete_offer/<int:pk>/delete', SpecialOffer2DeleteView.as_view(), name='delete_offer'),

    path('addfeedback/create', FeedbackCreateView.as_view(), name='create_feedback'),
    path('dbfeedback/<int:pk>/edit', FeedbackUpdateView.as_view(), name='feedback_update'),
    path('delete_feed/<int:pk>/delete', Feedback2DeleteView.as_view(), name='delete_feed'),

    path('home/', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('rooms/', RoomPageView.as_view(), name='rooms'),
    path('room/', RoomSliderPageView.as_view(), name='room'),
    path('contact/', ContactPageVew.as_view(), name='contact'),
    path('faqs/', FAQsPageView.as_view(), name='faqs'),
    path('terms/', TermsAndConditionView.as_view(), name='terms'),
    path('privacy/', PrivacyPolicyPageView.as_view(), name='privacy'),
    path('reviews/', FeedbackListView.as_view(), name='feedback_list'),
    path('partners/', PartnersPageView.as_view(), name='partners'),
    path('footer/', FooterPageView.as_view(), name='footer'),

]
