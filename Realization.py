# This Python Script is the create a natural behavior of robots over the course of time
from datetime import date
from datetime import datetime

class Behaviour:

	def Current_Behaviour(): # Fetch data from Table
		today = date.today()
		now = datetime.now()
		Current_minute = now.strftime("%M")
		Current_hour = now.strftime("%H")
		Current_date=today.strftime("%d")
		Current_month=today.strftime("%m")
		Current_year=today.strftime("%Y")
		

