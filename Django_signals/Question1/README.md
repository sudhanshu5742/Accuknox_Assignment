# By default, Django signals are executed synchronously. This means that the signal handler blocks the execution of the caller until it finishes.

# This output shows that the signal handler executes synchronously and blocks the view from finishing until the handler completes.

# output
View started...
Signal handler started...
Signal handler finished after 5 seconds.
View finished after 5.00 seconds.
