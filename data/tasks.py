from celery import shared_task
from .models import Task
import csv
import os
from celery.task.control import revoke
from atlan.settings import BASE_DIR


@shared_task
def interchange_column(name, pointer=1):
    t = Task.objects.get(name=name)
    file_dir = os.path.join(BASE_DIR, 'files/file.csv')
    new_file_dir = os.path.join(BASE_DIR, 'files/reordered.csv')
    with open(file_dir, 'r') as infile, open(new_file_dir, 'a') as outfile:
        # output dict needs a list for new column ordering
        fieldnames = ['Order ID', 'Country', 'Item Type',
                      'Sales Channel', 'Order Priority', 'Order Date', 'Region', 'Ship Date', 'Units Sold', 'Unit Price', 'Unit Cost', 'Total Revenue', 'Total Cost', 'Total Profit']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        # reorder the header first
        writer.writeheader()
        for row in csv.DictReader(infile):
            # writes the reordered rows to the new file
            writer.writerow(row)
            t.pointer = pointer
            t.save()
            pointer += 1
    return
