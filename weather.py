import requests
from bs4 import BeautifulSoup

city = input("Enter your city: ")
city_formatted = city.lower().replace(" ", "-")

url = f"https://www.timeanddate.com/weather/Nigeria/{city_formatted}"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

try:
    temperature = soup.find("div", class_="h2").get_text(strip=True)
    description = soup.find("div", class_="h2").find_next("p").get_text(strip=True)
    # print(f"The current temperature in {city} is {temperature} and {description}.")

    print(f"The current Weather in {city}:")
    print(f"Temperature in {city} is {temperature}.")
    print(f"Condition: {description}")

except AttributeError:
    print("Could not find weather information for the specified city, Please check the city name and try again.")



    