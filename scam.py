import os
import random
import string
import json
from time import sleep

chars = string.ascii_letters + string.digits + '!@#$%^&*()'

url = 'https://www.blahblahblah.com'
names = json.loads(open('names.json').read())

for name in names:
	name_extra = ''.join(random.choice(string.digits))

	username = name.lower() + name_extra + '@yahoo.com'
	password = ''.join(random.choice(chars) for i in range(8))

	print('sending username',username, password, 'to', url)
	sleep(1)