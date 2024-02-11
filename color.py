#!/usr/bin/python
import re
def print_hex_color(text):
  """
  Prints all hex colors from the text on separate lines.
  """
  pattern = r"#[A-Fa-f0-9]{6}"
  matches = re.findall(pattern, text)
  for match in matches:
      print(match)
print("The hex colors are:")
print_hex_color(text)
