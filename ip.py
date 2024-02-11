#!/usr/bin/python
import re
text = """Movie: Inception (2010)
Song: [Verse 1] Just a small town girl
Twitter: @user123
ISBN: ISBN 123-4-567-89012-3
Joke: Why did the chicken cross the road? Because it wanted to get to the other side.
Episode: Friends S02E05: The One with Five Steaks and an Eggplant
Date: 10-Jan-2023
Color: #FFA500
IP: 192.168.1.1
Movie: The Shawshank Redemption (1994)
Song: [Verse 2] Don't stop believin'
Twitter: @john_doe123
ISBN: ISBN 456-7-890-12345-6
Joke: Why did the tomato turn red? Because it saw the salad dressing.
Episode: Breaking Bad S03E12: Half Measures
Date: 25-Dec-2022
Color: #00FF00
IP: 127.0.0.1
Movie: The Godfather (1972)
Song: [Verse 3] I'm a Barbie girl, in a Barbie world
Twitter: @user456
ISBN: ISBN 789-0-123-45678-9
Joke: Why did the scarecrow win an award? Because he was outstanding in his field.
Episode: Game of Thrones S05E03: High Sparrow
Date: 15-Nov-2021
Color: #0000FF
IP: 192.168.0.1
Movie: Pulp Fiction (1994)
Song: [Verse 1] Sweet Caroline, ba ba ba
Twitter: @jsmith789
ISBN: ISBN 012-3-456-78901-2
Joke: Why did the math book sad? Because it had too many problems.
Episode: The Office S02E03: Office Olympics
Date: 03-Oct-2020
Color: #FF0000
IP: 10.0.0.1
"""
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
