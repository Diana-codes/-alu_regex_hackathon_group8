#!/usr/bin/python
def print_ip_address(text):
  """
  Prints all hex colors from the text on separate lines.
  """
  pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
  matches = re.findall(pattern, text)
  for match in matches:
      print(match)

print("The ip addresses are:")
print_ip_address(text)      
