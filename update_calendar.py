#!/usr/bin/env python3
"""Fetch VU iCalendar and attach Europe/Vilnius to floating event dates."""
import os
import re
import urllib.request
from pathlib import Path

URL = os.environ['VU_ICS_URL']
req = urllib.request.Request(URL, headers={'User-Agent': 'VU-calendar-timezone-fix/1.0'})
with urllib.request.urlopen(req, timeout=45) as response:
    raw = response.read()
text = raw.decode('utf-8-sig')
if 'BEGIN:VCALENDAR' not in text or 'END:VCALENDAR' not in text:
    raise ValueError('Response is not a complete iCalendar file')
# Keep the original file content and line endings, changing only floating DATE-TIME properties.
newline = '\r\n' if '\r\n' in text else '\n'
lines = text.splitlines()
inside_event = False
count = 0
out = []
for line in lines:
    if line == 'BEGIN:VEVENT':
        inside_event = True
    if inside_event:
        match = re.fullmatch(r'(DTSTART|DTEND)(?:;VALUE=DATE-TIME)?:(\d{8}T\d{6})', line)
        if match:
            line = f'{match.group(1)};TZID=Europe/Vilnius:{match.group(2)}'
            count += 1
    out.append(line)
    if line == 'END:VEVENT':
        inside_event = False
if count == 0:
    raise ValueError('No floating event start/end timestamps found; source format may have changed')
Path('docs').mkdir(exist_ok=True)
Path('docs/calendar.ics').write_bytes((newline.join(out) + newline).encode('utf-8'))
print(f'Updated {count} date-time properties')
