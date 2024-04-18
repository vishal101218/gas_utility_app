from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .forms import ServiceRequestForm, UserRegistrationForm
from .models import ServiceRequest

def custom_login(request):
    if request.method == 'POST':
        # Handle login form submission
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to base.html after successful login
            return redirect('base')  # Replace 'base' with the appropriate URL name

    return render(request, 'base.html')
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.user = request.user
            service_request.save()
            return redirect('submit_success')
    else:
        form = ServiceRequestForm()
    return render(request, 'submit_request.html', {'form': form})

def track_requests(request):
    service_requests = ServiceRequest.objects.filter(user=request.user)
    return render(request, 'track_requests.html', {'service_requests': service_requests})

def submit_success(request):
    return render(request, 'submit_success.html')
