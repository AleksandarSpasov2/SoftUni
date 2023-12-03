import re

message = input()

pattern = r'^(\$|%)[A-Z][a-z]{2,}\1:\s(\[\d+\]\|){3}$'
