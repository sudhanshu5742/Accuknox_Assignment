# Yes, Django signals run in the same thread as the caller by default. To prove this, we can compare the thread IDs of both the caller (the view) and the signal handler.

# The thread IDs are identical, confirming that both the view and the signal handler run in the same thread

# Output
View thread ID: 140735691822080
Signal handler thread ID: 140735691822080
