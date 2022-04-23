'''
pypi.org/
docs.python.org/3/library/index.html

https://pypi.org/project/emoji/
https://www.webfx.com/tools/emoji-cheat-sheet/
http://www.unicode.org/emoji/charts/full-emoji-list.html
'''

import random
import emoji # installed using PIP 

n = random.random()
m = random.randint(1, 10)

print(n)
print(m)
print(emoji.emojize('I love Python :alien:', language='alias'))
