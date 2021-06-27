from tkinter import *
import requests
app = Tk()
def get_weather():
    city = cityField.get()
    key = 'e17310358b3df05b457529f8d91cec22'
    url = 'http://api.openweathermap.org/data/2.5/weather?units=metric'
    params = {'APPID':key, 'q':city, 'units':'metrics'}
    result = requests.get(url, params=params)
    weather = result.json()
    info['text'] = f'{str(weather["name"])}: {weather["main"]["temp"]}'
app.title('Weather')
app.geometry('300x250')
app.resizable(width=False, height=False)
frame_top = Frame(app, bg='#fff')
frame_top.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.25)

frame_bottom = Frame(app, bg='#fff')
frame_bottom.place(relx=0.15, rely=0.55, relwidth=0.7, relheight=0.1)

cityField = Entry(frame_top, bg='#fff', font=30)
cityField.pack()

btn = Button(frame_top, text='Check weather', command=get_weather)
btn.pack()

info= Label(frame_bottom, text='info', bg='#fff', font=40)
info.pack()
app.mainloop()