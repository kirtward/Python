#Basic random password generator, 8 characters (2 upper, 2 lower, 2 digits & 2 special)
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

# Digit section creation
d1=chr(random.randint(48,57))
d2=chr(random.randint(48,57))

# Special Character 
s1=chr(random.randint(33,47))
s2=chr(random.randint(33,47))

# Create whole password and pass to shuffle
password = uc1 + uc2 + lc1 + lc2 + d1 + d2 + s1 + s2
password = shuffle(password)

#Output
print(password)
