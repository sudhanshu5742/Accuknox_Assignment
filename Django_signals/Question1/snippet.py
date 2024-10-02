# This will be signals.py file
from django.dispatch import Signal, receiver
import time

# This is used to define a custom signal
my_signal = Signal()

# Define a signal handler
@receiver(my_signal)
def my_signal_handler(sender, **kwargs):
    print("Signal handler started...")
    time.sleep(5)  # Simulate a long-running task
    print("Signal handler finished after 5 seconds.")



# This will be views.py file 
from django.http import HttpResponse
from .signals import my_signal
import time

def trigger_signal(request):
    print("View started...")
    start_time = time.time()

    # To Send the signal
    my_signal.send(sender=None)

    end_time = time.time()
    print(f"View finished after {end_time - start_time} seconds.")
    
    return HttpResponse("Signal triggered.")
