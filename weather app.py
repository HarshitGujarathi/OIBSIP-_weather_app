import tkinter as tk
from tkinter import messagebox
import requests

def get_weather(city):
   

    api_key = "f4fd505b2e44bd59087b2254002800b3"   
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()   
        return response.json()
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Error fetching weather data: {e}")
        return None

def fetch_weather_and_display():
    try:
        city = city_entry.get()
        weather_data = get_weather(city)

        if weather_data is None:
            return

        if weather_data["cod"] == "404":
            messagebox.showinfo("City Not Found", "City not found. Please check the spelling and try again.")
        else:
            temp = weather_data["main"]["temp"]
            humidity = weather_data["main"]["humidity"]
            desc = weather_data["weather"][0]["desc"]

            result_label.config(text=f"**temp:** {temp}°C\n**Humidity:** {humidity}%\n**Condition:** {desc}")

    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")

# GUI setup
root = tk.Tk()
root.title("Weather Forecast APP")

city_label = tk.Label(root, text="Enter City:")
city_label.pack()

city_entry = tk.Entry(root)
city_entry.pack()

fetch_button = tk.Button(root, text="Fetch Weather", command=fetch_weather_and_display)
fetch_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
