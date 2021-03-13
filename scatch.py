import pdfplumber

import re

example = '''
3402321020
102-230-1234

'''

pattern = re.compile(r'\d{3}-\d{3}-\d{3}')
matches = pattern.finditer(example)

for match in matches:
    print(match)