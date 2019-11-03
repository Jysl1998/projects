import tkinter as tk
import requests

#pixels
HEIGHT = 600
WIDTH = 500

###### FUNCTIONS ########
def get_weather(city):
    weather_key = '61a0dbca3badbbb154bbf4d1020ca4a1'
    url = 'https://api.openweathermap.org/data/2.5/forecast'
    params = {'APPID': weather_key, 'q': city, 'units': 'fahrenheit'}
    response = requests.get(url,params = params)
    print(response.json())
    #api.openweathermap.org/data/2.5/forecast?q={city name},{country code}
    
    
root = tk.Tk()

canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

frame = tk.Frame(root, bg = '#88c1ff')
#relx and rely is what keeps it centered, creates the border
frame.place(relx = 0.1, rely = 0.1, relwidth= 0.8, relheight= 0.8)

#lambda temporary fills it in
button = tk.Button(frame, text = "Get Weather", bg = 'green',fg = 'white', command = lambda: get_weather(city.get()))
#fg = font color
#bg = button color
button.place(relx = 0.7, rely = 0.2, relwidth = 0.25, relheight = 0.05)
#button pack makes the button appear
#button.pack(side = "left")
#button.grid(row = 0, column = 0)

##label = tk.Label(frame, text = "This is a Label", bg = 'yellow')
###label.pack(side = "left")
###label.grid(row = 0, column = 1)
##label.place(relx = 0.3, rely = 0, relwidth = 0.50, relheight = 0.05)

label = tk.Label(frame, bg = 'white')
label.place(relx = 0.2, rely = 0.3, relwidth = 0.60, relheight = 0.6)

entry = tk.Entry(frame, bg = 'white')
#entry.pack(side = "left")
#entry.grid(row = 0, column = 2)
entry.place(relx = 0.1, rely = 0.2, relwidth = 0.60, relheight = 0.05)


root.mainloop()

