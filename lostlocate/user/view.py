from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings
from django.utils import timezone
from user.models import RegistrationCode, CustomUser
import uuid
import datetime

def send_test_email(request):
    # Create or get a test user
    user, created = CustomUser.objects.get_or_create(
        username='testuser',
        role= 'testrole',
        email='testuser@example.com',
        defaults={'password': 'testpassword123'}
    )
    # Generate a verification code
    code = RegistrationCode(
        user=user,  # Assign the user to the verification code
        code=uuid.uuid4(),  # Generate a new UUID code
        created_at=timezone.now(),
        expires_at=timezone.now() + datetime.timedelta(minutes=10)  # Code valid for 10 minutes
    )
    code.save()  # Save the verification code to the database
    # Prepare email details
    subject = 'Your Registration Code'
    message = f'Your registration code is {code.code}. It expires in 10 minutes.'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ['unyolohannah@gmail.com']  # Replace with a valid email address
    try:
        # Send email
        send_mail(subject, message, from_email, recipient_list)
        return HttpResponse('Test email with verification code sent successfully.')
    except Exception as e:
        return HttpResponse(f'Failed to send email: {e}')