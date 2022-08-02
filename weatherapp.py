from tkinter import *
from configparser import ConfigParser
from tkinter import messagebox
from tkinter.font import BOLD
import requests
from webbrowser import BackgroundBrowser
from tkinter import messagebox
import requests

url_api="https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
api_file="myweatherapi.key"
file_a=ConfigParser()
file_a.read(api_file)
api_key =file_a['api_key']['key']

def get_weather(city):
    final=requests.get(url_api.format(city,api_key))
    if final:
        json=final.json()
        city=json['name']
        country_name = json['sys']['country']
        temp_kelvin= json['main']['temp']
        temp_celsius= temp_kelvin - 273.15
        temp_Fahrenheit = temp_celsius*1.8+32
        weather_type=json['weather'][0]['main']
        humidity_status =json['main']['humidity']
        feels_like=json['main']['feels_like'] -273.15
        result =(city,country_name,temp_celsius,temp_Fahrenheit,weather_type,humidity_status,feels_like)
        
        return result
    else:
        return None

def show_weather():
    city=search_city.get()
    weather = get_weather(city)

    if weather:
        location['text'] ='{}, {}'.format(weather[0],weather[1])
        temperature['text'] ='{:.2f} C, {:.2f} F'.format(weather[2],weather[3])
        weather_entry['text'] = f"weather type - {weather[4]}, humidity {weather[5]}" +'\n' + 'feels like {:.2f} C'.format(weather[6])
    else:
        messagebox.showerror('Error',"Please enter a valid name. cannot found")


root=Tk()
root.title("my weather app")
root.config(background="green")
root.geometry("800x400")
search_city=StringVar()
enter_city=Entry(root,textvariable=search_city, fg="blue" ,font=("Calibri",25,"bold"))
enter_city.pack()
search_button=Button(root, text='Search Weather' ,width=20,bg='red',fg='white',font=('Arial',10,'bold'),command=show_weather)
search_button.pack()
location =Label(root,text='city,country',font=("Calibri",20,"bold"),bg="lightpink")
location.pack()
temperature=Label(root, text='',font=("Arial",20,"bold"),bg="lightpink")
temperature.pack()
weather_entry=Label(root,text='',font=("Arial",15,"bold"),bg="lightgreen")
weather_entry.pack()
root.mainloop()