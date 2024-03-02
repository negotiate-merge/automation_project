#!/usr/bin/env python3

import os
import datetime
import reports

'''
    Ideally we would call this function from run.py as an exit point to send a report once the upload was complete.
'''

filename = f'{os.getcwd()}/report.pdf'

os.chdir('supplier-data/descriptions')

items = os.listdir('.')
report_body = ''
for item in items:
    with open(item, 'r') as f:
        lines = f.readlines()
        name = lines[0].strip()
        weight = lines[1].strip()
    report_body += f'name: {name}<br/>weight: {weight}<br/><br/>'

title = f"Processed Update on {datetime.date.today()}"
reports.generate_report(filename, title, report_body)



