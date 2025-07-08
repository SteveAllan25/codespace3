from django.shortcuts import render, get_object_or_404, redirect
from .models import Event
from .forms import RegistrationForm

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import SignUpForm




# View to list all events
def event_list(request):
    events = Event.objects.all().order_by('date')
    return render(request, 'events/event_list.html', {'events': events})

# View to show details for a specific event
def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'events/event_detail.html', {'event': event})

# View to handle event registration
@login_required
def register_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save(commit=False)
            registration.event = event
            if request.user.is_authenticated:
                registration.user = request.user
            registration.save()
            messages.success(request, 'Registration successful!')
            return redirect('event_list')
    else:
        form = RegistrationForm()
    return render(request, 'events/registration_form.html', {'form': form, 'event': event})

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after sign-up
            messages.success(request, "Account created successfully!")
            return redirect('event_list')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

