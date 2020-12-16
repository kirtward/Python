import random

# shuffle password
def shuffle(string):
	tempList = list(string)
	random.shuffle(tempList)
	return ''.join(tempList) 
	
# Upcase section creation
uc1=chr(random.randint(65,90))
uc2=chr(random.randint(65,90))

# Lowercase section creation
lc1=chr(random.randint(97,122))
lc2=chr(random.randint(97,122))
lc3=chr(random.randint(97,122))
lc4=chr(random.randint(97,122))
lc5=chr(random.randint(97,122))

# Digit section creation
d1=chr(random.randint(48,57))
d2=chr(random.randint(48,57))

# Special Character
spe = ['$', '#', '@', '_']
s1=str(random.choice(spe))

# Create whole password and pass to shuffle
password = uc1 + uc2 + lc1 + lc2 + lc3 + lc4 +lc5 + d1 + d2 + s1
password = shuffle(password)

#Output
print(password)
