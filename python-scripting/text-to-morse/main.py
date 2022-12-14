import json

with open('morse.json') as f:
  code = f.read()
  morse_dict = json.JSONDecoder().decode(code)

user_input = input("Enter a string to convert to morse code: ").lower()
encoded_str = ''.join([morse_dict[c]+' ' if c in morse_dict else c for c in user_input])

print(encoded_str)
