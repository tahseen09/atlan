import csv
import os

file_dir = os.path.join(BASE_DIR, 'files/file.csv')
new_file_dir = os.path.join(BASE_DIR, 'files/reordered.csv')
with open(file_dir, 'r') as infile, open(new_file_dir, 'a') as outfile:
    # output dict needs a list for new column ordering
    fieldnames = ['Order ID', 'Country', 'Item Type',
                  'Sales Channel', 'Order Priority', 'Order Date', 'Region', 'Ship Date', 'Units Sold', 'Unit Price', 'Unit Cost', 'Total Revenue', 'Total Cost', 'Total Profit']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    # reorder the header first
    writer.writeheader()
    pointer = 1
    for row in csv.DictReader(infile):
        # writes the reordered rows to the new file
        writer.writerow(row)
        # Task(pointer=pointer).save()
        print(pointer)
        pointer += 1
