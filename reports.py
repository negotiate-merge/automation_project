#!/usr/bin/env python3

# Gain familiarity from https://docs.reportlab.com/demos/hello_world/hello_world/ 

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.pdfgen import canvas

# styles = getSampleStyleSheet()

c = canvas.Canvas("rl-hello_again.pdf", pagesize=(595.27, 841.89))
c.drawString(50, 780, "Hello Again")
c.showPage()
c.save()




''' TODO 
Using the reportlab Python library, define the method generate_report to build the PDF reports. We have already covered how to generate PDF reports in an earlier lesson; you will want to use similar concepts to create a PDF report named processed.pdf
'''
