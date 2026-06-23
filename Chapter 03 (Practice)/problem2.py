letter = '''Dear <|Name|>,
You are selected!
<|Date|>
'''

print(letter.replace("<|Name|>", "Farman Rajper").replace("<|Date|>", "'25th Jan 2001'"))