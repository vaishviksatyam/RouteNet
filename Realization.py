#This Python Script is the create a natural behavior of robots over the course of time

#Weather defines how often robot shivers
#Freshness defines how fast robot responds to voice
#Life defines breaking in Speed and with how much stiffness he walks with
#Exploration how often robot gets distracted
#Cheerful how often he jumps
#Active How fast he walks and turns

from datetime import date,datetime
import xlrd

Book_of_Life = ("Book_of_Life.xlsx")
workbook = xlrd.open_workbook(Book_of_Life)

def Current_Behaviour(): # Fetch data from Table
	today = date.today()
	now = datetime.now()
	Current_hour = now.strftime("%H")
	Current_date=today.strftime("%d")
	Current_month=today.strftime("%m")
	Current_year=today.strftime("%Y")
	#Current_hour=1
	#Current_date=20
	#Current_month=10
	#Current_year=2032
	print(Current_hour,Current_date,Current_month,Current_year)
	sheet0 = workbook.sheet_by_index(0)
	sheet1 = workbook.sheet_by_index(1)
	sheet2 = workbook.sheet_by_index(2)
	sheet3 = workbook.sheet_by_index(3)
	Weather=sheet0.cell_value(int(Current_month), 1)
	Freshness=sheet0.cell_value(int(Current_month), 2)
	Life_Level=sheet1.cell_value(int(Current_year)-2019, 1)
	Exploration=sheet1.cell_value(int(Current_year)-2019, 2)
	Cheerful=sheet2.cell_value(int(Current_date), 1)
	Active=sheet3.cell_value(int(Current_hour)+1, 1)

	#Weather=0.9
	#Freshness=0.9
	#Life_Level=0.1
	#Exploration=0.9
	#Cheerful=0.9
	#Active=0.9

	print("Weather:",Weather)
	print("Freshness:",Freshness)
	print("Life_Level:",Life_Level)
	print("Exploration:",Exploration)
	print("Cheerful:",Cheerful)
	print("Active:",Active)

def Walk(Life,Active,cheerful_delay):
	pass
	#Define id,Type,Complience,Speed,Delay for motors and its walk cycle
def Standby(Weather_delay,Life,Exploration_delay):
	pass
	#How often it will react to weather, Exploration and how stiff it will be.
def Voice(Freshness):
	pass
	#Reaction time
def going_to_sleep(Life,Active):
	pass
	#How stiff is he and how fast
def waking_up(Life,Active):
	pass
	#How stiff he is and how fast
def Explore(Life,Weather,Active,Exploration_delay):
	pass
	#Random Walking with stiffness and speed,and usualy Head Movement.
def Play_time(Active):
	pass
	#How frequenctly it changes its action
