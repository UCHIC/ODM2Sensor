from django.test.runner import DiscoverRunner
from sensordatainterface import models
from sensordatainterface import migrations
import inspect

class SQLServerDiscoverRunner(DiscoverRunner):
        def run_tests(self, test_labels, extra_tests=None, **kwargs):
            clearSchemas()
            super(SQLServerDiscoverRunner, self).run_tests(test_labels, extra_tests, **kwargs)

def clearSchemas():
    """Remove Schemas from all models before setting up test database.
    This is because pyodbc doesn't support the creation of schemas in SQL Server"""
    model_classes = inspect.getmembers(models, inspect.isclass)
    for name, model in model_classes:
        if name != 'Sysdiagrams':
            table = model._meta.db_table
            model._meta.db_table = table[table.index('[')+1:]
