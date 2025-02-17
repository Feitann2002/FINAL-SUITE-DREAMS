from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .forms import UserRegistrationForm, FeedbackForm, AppointmentUpdateForm
from .models import User, Admin, Appointment, SpecialOffer, Room, Feedback
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = form.cleaned_data['password']
            user.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'app/register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
            if user.password == password:
                request.session['user_id'] = user.id
                return redirect('user_splash')
            else:
                messages.error(request, "Invalid username or password.")
        except User.DoesNotExist:
            messages.error(request, "Invalid username or password.")

    return render(request, 'app/login.html')


def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            admin = Admin.objects.get(username=username)
            if admin.password == password:
                request.session['admin_id'] = admin.id
                request.session['admin_username'] = admin.username
                return redirect('database')
            else:
                messages.error(request, "Invalid username or password.")
        except Admin.DoesNotExist:
            messages.error(request, "Invalid username or password.")

    return render(request, 'app/admin_login.html')


class BasePageView(TemplateView):
    template_name = 'app/base.html'


class DatabasePageView(TemplateView):
    template_name = 'app/database.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['admins'] = Admin.objects.all()
        context['users'] = User.objects.all()
        context['appointments'] = Appointment.objects.select_related('user', 'room').all()
        context['rooms'] = Room.objects.all()
        context['offers'] = SpecialOffer.objects.all()
        context['feedbacks'] = Feedback.objects.all()

        admin_username = self.request.session.get('admin_username')
        context['admin_username'] = admin_username
        return context


class UserSplashView(TemplateView):
    template_name = 'app/user_splash.html'


class HomePageView(TemplateView):
    template_name = 'app/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['offers'] = SpecialOffer.objects.all()
        return context


class OfferListView(ListView):
    model = SpecialOffer
    context_object_name = 'offers'
    template_name = 'app/home.html'


class OfferDetailView(DetailView):
    model = SpecialOffer
    context_object_name = 'offer'
    template_name = 'app/detail_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['offers'] = SpecialOffer.objects.all()
        return context

class AboutPageView(TemplateView):
    template_name = 'app/about.html'


class RoomPageView(TemplateView):
    template_name = 'app/room.html'


class RoomSliderPageView(TemplateView):
    template_name = 'app/room_slider.html'


class ContactPageVew(TemplateView):
    template_name = 'app/contact.html'


class FAQsPageView(TemplateView):
    template_name = 'app/faq.html'


class TermsAndConditionView(TemplateView):
    template_name = 'app/terms_and_conditions.html'


class PrivacyPolicyPageView(TemplateView):
    template_name = 'app/privacy_policy.html'


class PartnersPageView(TemplateView):
    template_name = 'app/partners.html'


class FooterPageView(TemplateView):
    template_name = 'app/footer.html'


class UserListView(ListView):
    model = User
    template_name = 'app/database.html'


class AdminListView(ListView):
    model = Admin
    template_name = 'app/database.html'


class AdminCreateView(CreateView):
    model = Admin
    fields = ['firstname', 'lastname', 'username', 'email', 'password']
    template_name = 'app/dbadmin.html'

    def get_success_url(self):
        return reverse_lazy('database') + '?section=admins'


class UserCreateView(CreateView):
    model = User
    fields = ['name', 'username', 'email', 'password']
    template_name = 'app/adduser.html'

    def get_success_url(self):
        return reverse_lazy('database') + '?section=users'


class RoomCreateView(CreateView):
    model = Room
    fields = ['room_number', 'room_type', 'capacity', 'price_per_hour']
    template_name = 'app/addroom.html'

    def get_success_url(self):
        return reverse_lazy('database') + '?section=rooms'


class Appointment2CreateView(CreateView):
    model = Appointment
    fields = ['user', 'room', 'start_date', 'end_date']
    template_name = 'app/addappointment.html'

    def get_success_url(self):
        return reverse_lazy('database') + '?section=appointments'


class SpecialOfferCreateView(CreateView):
    model = SpecialOffer
    fields = ['room', 'discount_percentage', 'start_date', 'end_date', 'description']
    template_name = 'app/addoffers.html'

    def get_success_url(self):
        return  reverse_lazy('database') + '?section=offers'


class FeedbackCreateView(CreateView):
    model = Feedback
    fields = ['user', 'rating', 'comments']
    template_name = 'app/addfeedback.html'

    def get_success_url(self):
        return reverse_lazy('database') + '?section=feedbacks'


class AdminUpdateView(UpdateView):
    model = Admin
    fields = ['firstname', 'lastname', 'username', 'email', 'password']
    template_name = 'app/admin_update.html'

    def get_success_url(self):
        return reverse_lazy('database') + '?section=admins'


class UserUpdateView(UpdateView):
    model = User
    fields = ['name', 'username', 'email', 'password']
    template_name = 'app/user_update.html'

    def get_success_url(self):
        return reverse_lazy('database') + '?section=users'


class RoomUpdateView(UpdateView):
    model = Room
    fields = ['room_number', 'room_type', 'capacity', 'price_per_hour']
    template_name = 'app/room_update.html'

    def get_success_url(self):
        return reverse_lazy('database') + '?section=rooms'


class Appointment2UpdateView(UpdateView):
    model = Appointment
    fields = ['user', 'room', 'start_date', 'end_date']
    template_name = 'app/update_appointment.html'

    def get_success_url(self):
        return reverse_lazy('database') + '?section=appointments'


class SpecialOfferUpdateView(UpdateView):
    model = SpecialOffer
    fields = ['room', 'discount_percentage', 'start_date', 'end_date', 'description']
    template_name = 'app/offer_update.html'

    def get_success_url(self):
        return  reverse_lazy('database') + '?section=offers'


class FeedbackUpdateView(UpdateView):
    model = Feedback
    fields = ['user', 'rating', 'comments']
    template_name = 'app/feedback_update.html'

    def get_success_url(self):
        return reverse_lazy('database') + '?section=feedbacks'


class AdminDeleteView(DeleteView):
    model = Admin
    template_name = 'app/admin_delete.html'

    def get_success_url(self):
        return  reverse_lazy('database') + '?section=admins'


class UserDeleteView(DeleteView):
    model = User
    template_name = 'app/user_delete.html'

    def get_success_url(self):
        return reverse_lazy('database') + '?section=users'


class RoomDeleteView(DeleteView):
    model = Room
    template_name = 'app/room_delete.html'

    def get_success_url(self):
        return reverse_lazy('database') + '?section=rooms'


class Appointment2DeleteView(DeleteView):
    model = Appointment
    template_name = 'app/appointment_delete.html'

    def get_success_url(self):
        return reverse_lazy('database') + '?section=appointments'


class SpecialOffer2DeleteView(DeleteView):
    model = SpecialOffer
    template_name = 'app/delete_offer.html'

    def get_object(self, queryset=None):
        return get_object_or_404(SpecialOffer, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['offer'] = self.get_object()
        return context

    def get_success_url(self):
        return reverse_lazy('database') + '?section=offers'


class Feedback2DeleteView(DeleteView):
    model = Feedback
    template_name = 'app/delete_feedback.html'

    def get_object(self, queryset=None):
        obj = get_object_or_404(Feedback, pk=self.kwargs['pk'])
        return obj

    def get_success_url(self):
        return reverse_lazy('database') + '?section=feedbacks'


class AppointmentCreateView(CreateView):
    model = Appointment
    fields = ['room', 'start_date', 'end_date']
    template_name = 'app/book_appointment.html'

    def form_valid(self, form):
        user_id = self.request.session.get('user_id')
        if not user_id:
            messages.error(self.request, "You must be logged in to book an appointment.")
            return redirect('login')

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            messages.error(self.request, "User does not exist.")
            return redirect('login')

        form.instance.user = user
        appointment = form.save(commit=False)
        appointment.user = user
        appointment.save()

        messages.success(self.request, "Your appointment has been booked successfully!")
        return redirect('account_settings')

    def get_success_url(self):
        return reverse_lazy('account_settings')


class AppointmentDetailView(DetailView):
    model = Appointment
    template_name = 'app/appointment_detail.html'
    context_object_name = 'appointment'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        appointment = self.object

        total_cost = appointment.calculate_total_cost()
        context['total_cost'] = total_cost

        special_offers = SpecialOffer.objects.filter(
            room=appointment.room,
            start_date__lte=appointment.start_date,
            end_date__gte=appointment.end_date
        )
        context['special_offers'] = special_offers

        return context


class AppointmentUpdateView(UpdateView):
    model = Appointment
    form_class = AppointmentUpdateForm
    template_name = 'app/edit_appointment.html'

    def get_object(self, queryset=None):
        appointment = super().get_object(queryset=queryset)
        if appointment.user.id != self.request.session.get('user_id'):
            raise Http404("You are not authorized to edit this appointment.")
        return appointment

    def form_valid(self, form):
        user_id = self.request.session.get('user_id')
        if not user_id:
            return redirect('login')
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return redirect('login')
        appointment = form.save(commit=False)
        appointment.user = user
        appointment.save()
        return redirect('account_settings')

    def get_success_url(self):
        return reverse_lazy('account_settings')


def account_settings(request):
    if 'user_id' not in request.session:
        return redirect('login')

    user_id = request.session['user_id']
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        raise Http404("User does not exist")

    appointments = Appointment.objects.filter(user=user)

    return render(request, 'app/account_settings.html', {
        'user': user,
        'appointments': appointments
    })


class FeedbackListView(ListView):
    model = Feedback
    template_name = 'app/feedback.html'
    context_object_name = 'feedbacks'
    paginate_by = 3

    queryset = Feedback.objects.all().order_by('-created_at')


def add_feedback(request):
    if 'user_id' not in request.session:
        messages.error(request, "You must be logged in to submit feedback.")
        return redirect('login')

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            user_id = request.session['user_id']
            try:
                user = User.objects.get(id=user_id)
            except User.DoesNotExist:
                messages.error(request, "User does not exist.")
                return redirect('login')

            feedback = form.save(commit=False)
            feedback.user = user
            feedback.save()
            return redirect('feedback_list')
    else:
        form = FeedbackForm()

    return render(request, 'app/add_feedback.html', {'form': form})
