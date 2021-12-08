"""
To make this work create account in open weathe map website and get the api.
Then set the api to api_key variable and set your city name at city_name variable.
Feel free to modify this code as you like.
This is my beginer project's, hope I made it nicely.
"""
from tkinter import *

import requests
from pprint import pprint


city_name = ""
api_key = ""


# def get_weather(api_key, city):
# 	url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city, api_key)
	
# 	response = requests.get(url)
# 	data = response.json()
# 	temp = data['main']['temp']
# 	temp = temp - 273.15
# 	pprint(round(temp))
# 	weather = data['weather'][0]
# 	pprint(weather)
	

#get_weather(api_key, city_name)



# GUI settings
window = Tk()
window.title("WeatherGui")
window.geometry("600x400")
window.config(bg="#f1f1f1")
icon = PhotoImage(file="logo.png")
window.iconphoto(True, icon)


url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city_name, api_key)

# get the weather data from the site
response = requests.get(url)
data = response.json()

# widgets
current_temp = data['main']['temp']
current_temp = current_temp - 273.15
current_temp = round(current_temp)
current_weather = data['weather'][0]['main']

temp_label = Label(window,text="Tempreture: ",font=("Calibri",30),bg="#f1f1f1")
weather_label = Label(window,text="Weather: ",font=("Calibri",30),bg="#f1f1f1")

temp = Label(window,text="{} c".format(current_temp),font=("Calibri",30),bg="#f1f1f1")
weather = Label(window,text=current_weather,font=("Calibri",30),bg='#f1f1f1')

# Grid settings
temp_label.grid(row=1,column=0)
weather_label.grid(row=2,column=0)

temp.grid(row=1,column=1,padx=30)
weather.grid(row=2,column=1)

# recognize the weather and show the perfect img according to the weather status
if current_weather.lower() == 'clouds':
	img = PhotoImage(file="cloud.png")
	cloud_img = Label(window,image=img,bg="#1e1e1e")
	cloud_img.grid(row=2,column=2)
elif current_weather.lower() == 'rain':
	img = PhotoImage(file="rain.png")
	cloud_img = Label(window,image=img,bg="#1e1e1e")
	cloud_img.grid(row=2,column=2)
	


# setting the logo for the gui
logo = Label(window,image=icon)
logo.grid(row=0,column=1,pady=30)


window.mainloop()
