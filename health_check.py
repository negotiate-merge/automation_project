#!/usr/bin/env python3

import psutil
import socket
import emails

errors = []

# Report an error if CPU usage is over 80%
if psutil.cpu_percent() > 80:
    errors.append(("CPU usage is over 80%", "Error - CPU usage is over 80%"))

# Report an error if available disk space is lower than 20%
if psutil.disk_usage('/').percent > 80:
    errors.append(("Available disk space is lower than 20%", "Error - Available disk space is less than 20%"))

# Report an error if available memory is less than 500MB
if psutil.virtual_memory().available / 1000000 < 500:
    errors.append(("available memory is less than 500MB", "Error - Available memory is less than 500MB"))

# Report an error if the hostname "localhost" cannot be resolved to "127.0.0.1"
local_addr = socket.gethostbyname('localhost')
if local_addr != '127.0.0.1':
    errors.append(('hostname "localhost" cannot be resolved to "127.0.0.1"', 'Error - localhost cannot be resolved to 127.0.0.1'))

sender = 'automaition@example.com'
recipient = '@example.com'       # Enter username from lab specs 
body = 'Please check your system and resolve the issue as soon as possible.'

for e in errors:
    subject = e[1]
    message  = emails.generate_email(sender, recipient, subject, body)
    # emails.send(message)      # requires the smtp to be configured on localhost, lab specific.
    print(message)