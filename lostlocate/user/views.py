from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.utils import timezone
from .models import RegistrationCode, CustomUser  # Import CustomUser if needed
from .forms import VerificationCodeForm
import datetime

# Simulate database (user_data dictionary as in your example)
user_data = {}

# User registration
def user_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        role = request.POST['role']
        phone_number = request.POST['phone_number']
        password = request.POST['password']
        
        # Save the phone number in user_data (simulating database)
        user_data['phone_number'] = phone_number  # Storing the phone number
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Generate and send verification code
            code = RegistrationCode.objects.create(
                user=user,
                expires_at=timezone.now() + datetime.timedelta(minutes=10)  # Code valid for 10 minutes
            )
            send_mail(
                'Your Registration Code',
                f'Your registration code is {code.code}. It expires in 10 minutes.',
                'from@example.com',
                [user.email],
                fail_silently=False,
            )
            request.session['user_id'] = user.id
            return redirect('verify_code')
        else:
            return render(request, 'register.html', {'error': 'Invalid registration details'})
    return render(request, 'register.html')

@login_required
def verify_code(request):
    if request.method == 'POST':
        form = VerificationCodeForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            phone_number = form.cleaned_data.get('phone_number')
            try:
                verification_code = RegistrationCode.objects.get(code=code, user_id=request.session['user_id'])
                user = verification_code.user

                # Compare stored phone number with the input phone number during login
                if user_data.get('phone_number') != phone_number:
                    return render(request, 'verify_code.html', {'form': form, 'error': 'Phone number does not match.'})

                if not verification_code.is_expired():
                    login(request, user)
                    return redirect('home')  # Redirect to a protected page
                else:
                    return render(request, 'verify_code.html', {'form': form, 'error': 'Code expired'})
            except RegistrationCode.DoesNotExist:
                return render(request, 'verify_code.html', {'form': form, 'error': 'Invalid code'})
    else:
        form = VerificationCodeForm()
    return render(request, 'verify_code.html', {'form': form})

