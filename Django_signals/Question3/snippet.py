# Code to define a model to log actions
# This is models.py file
from django.db import models

class Log(models.Model):
    message = models.CharField(max_length=255)

    def __str__(self):
        return self.message




# code to define the signal handler
# this is signals.py file
from django.dispatch import Signal, receiver
from .models import Log

# Define a custom signal
my_signal = Signal()

# Define a signal handler
@receiver(my_signal)
def my_signal_handler(sender, **kwargs):
    Log.objects.create(message="Signal handler executed")
    print("Signal handler: Log created")




# to trigger the signal and raise an exception in the view
# this is views.py file
from django.http import HttpResponse
from django.db import transaction
from .models import Log
from .signals import my_signal

def trigger_signal(request):
    try:
        with transaction.atomic():  # Start a transaction block
            Log.objects.create(message="View executed")
            print("View: Log created")

            # Send the signal
            my_signal.send(sender=None)

            # Intentionally raise an exception to trigger rollback
            raise Exception("Error in view")

    except Exception as e:
        print(f"Exception: {e}")
        return HttpResponse("Transaction failed and rolled back.")

    return HttpResponse("Signal triggered.")
