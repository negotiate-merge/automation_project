#!/usr/bin/env python3

# Gain familiarity from https://docs.reportlab.com/reportlab/userguide/ch5_platypus/

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
# from reportlab.lib import colors
# from reportlab.pdfgen import canvas

def generate_report(filename, title, body):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(filename)        # Creates the file
    report_title = Paragraph(title, styles['h1'])
    report_body = Paragraph(body, styles['BodyText'])
    empty_line = Spacer(1, 20)
    report.build([report_title, empty_line, report_body])





''' TODO 
Using the reportlab Python library, define the method generate_report to build the PDF reports. We have already covered how to generate PDF 
reports in an earlier lesson; you will want to use similar concepts to create a PDF report named processed.pdf

Layout:
Processed Update on <date today>

name: apple
weight: 500 lbs

name: Avocado
weight: 200 lbs

...

'''
