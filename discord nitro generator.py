import random
import string

# it prints links for getting nitro for free. Wydm?
letters = string.ascii_letters
numbers = string.digits
link = print('https://discord.gift/')
code = print( ''.join(random.choice(letters+numbers) for i in range(20)) )

