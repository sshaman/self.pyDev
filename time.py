import datetime


# fetch current datetime, ret array
def getDate():
	date = datetime.datetime.now()
	ctime = [date.hour, date.minute]
	return ctime


# make shift time ( +10min) from current, return it
def compDate(currDate):
	temp = currDate 
	tempH = currDate[0] # temp hours
	tempM = currDate[1] # temp mins
	shiftM = tempM + 10 # shift time
	if shiftM > 60:     # if mins overflow 60
		tempH = tempH +1 # make hours increment
		tempM = tempM - 50 # and get new minuter state
	else:
		tempM = tempM + 10 # if not overflow summ it
	newtime = [tempH, tempM]  # return array HRS, MIN
	return newtime
	
	


print getDate()
templ = getDate()
print compDate(templ)





