#This is signals.py file
from django.dispatch import Signal, receiver
import threading

#used to define a custom signal
my_signal = Signal()

#used define a signal handler
@receiver(my_signal)
def my_signal_handler(sender, **kwargs):
    print("Signal handler thread ID:", threading.get_ident())



#This is views.py file
from django.http import HttpResponse
from .signals import my_signal
import threading

def trigger_signal(request):
    print("View thread ID:", threading.get_ident())

    #To Send the signal
    my_signal.send(sender=None)

    return HttpResponse("Signal triggered.")
