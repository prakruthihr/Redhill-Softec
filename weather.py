import requests
from bs4 import BeautifulSoup

def get_weather_data(city):
    # Google's weather URL format
    url = f'https://www.google.com/search?q=weather+{city}'

    # Send a GET request to the URL
    response = requests.get(url)

   
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

      
        temperature = soup.find('div', class_='BNeawe iBp4i AP7Wnd').text
        condition = soup.find('div', class_='BNeawe tAd8D AP7Wnd').text

        # Print the weather data
        print(f'Weater in {city}: {temperature}, {condition}')
    else:
        print(f'Failed to retrieve weather data. Status code: {response.status_code}')

# Test the function
city = input('Enter the city: ')
get_weather_data(city)
