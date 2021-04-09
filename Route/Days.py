from datetime import date

today = date.today()
def Alive_Days(a,b,c):
	date_of_birth = date(a, b, c)
	birthday = date(today.year, date_of_birth.month, date_of_birth.day)
	days_until_birthday = (birthday-today).days
	days = (today-date_of_birth).days
	return f'You are {(days)} days old'
	
def Birthday_Days(a,b,c):
	date_of_birth = date(a, b, c)
	birthday = date(today.year, date_of_birth.month, date_of_birth.day)
	days_until_birthday = (birthday-today).days
	days = (today-date_of_birth).days
	if days_until_birthday > 0:
		med  = 'Its ' + str(days_until_birthday) + ' days until your Birthday'
	elif days_until_birthday == 0:
		med = 'Happy Birthday!'
	else:
		med = f"It is {365+days_until_birthday} days from your birthday"

	return med




