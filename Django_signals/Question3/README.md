# By default, Django signals run in the same database transaction as the caller. If an exception is raised in the caller, the signal handler’s database changes will also be rolled back.

# Output

# In the terminal:
View: Log created
Signal handler: Log created
Exception: Error in view

# In the database (no records should be created due to the rollback):
from myapp.models import Log
Log.objects.all() 


# This proves that both the view and the signal handler’s database changes are part of the same transaction, and if the transaction fails, all changes are rolled back
