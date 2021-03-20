import tkinter as tk
from tkinter import font
import requests

HEIGHT = 700
WIDTH = 800

def format_response(weather):
    #Try, except is basically used for user-defined exceptions
    try:
        date = weather['list'][0]['dt_txt']
        name = weather['city']['name']
        desc = weather['list'][1]['weather'][0]['description']
        temp = weather['list'][0]['main']['temp']

        #"Percent notation". %s means it's placeholder for a string, and \n means new line
        final_str = "Date: %s \nCity: %s \nConditions: %s \nTemperature (°C): %s" % (date, name, desc, temp)
    except:
        final_str = "There was an error retrieving the information, maybe you spelled wrong?"

    return final_str

def get_weather(city):
    weather_key = "e59c492ddfb48a0430c7a124177da081"
    url = "https://api.openweathermap.org/data/2.5/forecast"
    #Which parameters are needed is stated in the API documentation
    params = {"APPID": weather_key, "q": city, "units": "metric"}
    #Response is what we get back from our request
    response = requests.get(url, params=params)
    weather = response.json()
    print(weather)
    
    label["text"] = format_response(weather)
        


#Pack places the widget in the parent widget, has parameters such as side="TOP", "LEFT" etc to determine which side of the parent widget it packs against
#Fill fills extra space allocated to it. fill="X" fills horisontally, fill="Y" fills vertically and fill="both" fills both
#Expand gives the widget more space

#Grid is kinda like the same in html/css. Parameters are row and column. 

#Main window, all code should be between root and root mainloop
root = tk.Tk()

#First parameter always represent the parent window the widget is placed in
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file="new-history-forecast-bulk.png")
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

#Frame is a container used to organise other widgets
frame = tk.Frame(root, bd=5)
#Anchor = "n" makes the "relx" command start from "North" or the center from above
frame.place(relx=0.5, rely=0.16, relwidth=0.75, relheight=0.05, anchor="n")

#Entry is used to get input from users
entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

#Button is obviously a button
#The reason for using lambda instead of "command=get_weather" is because get_weather updates our entry constantly so we won't get a result by using it
#The lambda expression is updated only when the button is clicked, hence why we get a result
button = tk.Button(frame, text="Get Weather", font=40, command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bd=5)
lower_frame.place(relx=0.5, rely=0.23, relwidth=0.75, relheight=0.6, anchor="n")


#Label is basically a text widget
label = tk.Label(lower_frame, font=("", 18))
label.place(relwidth=1, relheight=1)

root.mainloop()