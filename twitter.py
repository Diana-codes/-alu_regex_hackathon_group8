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

def print_twitter_handles(text):
  """
  Prints all Twitter handles from the text on separate lines.
  """
  pattern = r"@[\w]+"
  matches = re.findall(pattern, text)
  for match in matches:
      print(match)
print("Twitter handles are:")
print_twitter_handles(text)
