from django.urls import path
from . import views
from .views import (BasePageView, DatabasePageView, HomePageView, AboutPageView, ContactPageVew,
                    FAQsPageView, PrivacyPolicyPageView, TermsAndConditionView, FeedbackListView,
                    UserSplashView, AdminCreateView, AdminUpdateView, AdminDeleteView, AppointmentDetailView,
                    register, login, admin_login, account_settings, AppointmentUpdateView, AppointmentCreateView,
                    PartnersPageView, FooterPageView, RoomSliderPageView, RoomPageView)

urlpatterns = [
    path('', BasePageView.as_view(), name='base'),
    path('register/', register, name='register'),
    path('user_login/', login, name='login'),
    path('user_splash/', UserSplashView.as_view(), name='user_splash'),
    path('admin_login/', admin_login, name='admin_login'),
    path('database/', DatabasePageView.as_view(), name='database'),
    path('feedback/add/', views.add_feedback, name='add-feedback'),
    path('account_settings/', account_settings, name='account_settings'),
    path('appointments/edit/<int:pk>/', AppointmentUpdateView.as_view(), name='edit_appointment'),
    path('book_appointment/', AppointmentCreateView.as_view(), name='book_appointment'),

    path('appointment/<int:pk>/', AppointmentDetailView.as_view(), name='appointment_detail'),
    path('dbadmin/create', AdminCreateView.as_view(), name='create_admin'),
    path('dbadmin/<int:pk>/edit', AdminUpdateView.as_view(), name='admin_update'),
    path('dbadmin/<int:pk>/delete', AdminDeleteView.as_view(), name='admin_delete'),

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
