import random
import string

# it prints links for getting nitro for free. Wydm?
letters = string.ascii_letters
numbers = string.digits

for i in range (60):
    base = ('https://discord.gift/') 
    array = ( ''.join(random.choice(letters+numbers) for i in range(20)) )

for i in range (1): #this function is unused because i dont know how it works :hyperLaugh:
    print(base + array)
