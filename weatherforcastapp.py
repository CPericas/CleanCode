class WeatherDataFetcher:
    def __init__(self):
        self.weather_data = {
            "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50, "city": "New York"},
            "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65, "city": "London"},
            "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70, "city": "Tokyo"}
        }

    def fetch(self, city):
        print(f"Fetching weather data for {city}...")
        return self.weather_data.get(city, {})

class DataParser:
    @staticmethod
    def parse(data):
        if not data:
            return "Weather data not available"
        city = data["city"]
        temperature = data["temperature"]
        condition = data["condition"]
        humidity = data["humidity"]
        return f"Weather in {city}: {temperature} degrees, {condition}, Humidity: {humidity}%"

class UserInterface:
    def __init__(self):
        self.fetcher = WeatherDataFetcher()
        self.parser = DataParser()

    def get_detailed_forecast(self, city):
        data = self.fetcher.fetch(city)
        return self.parser.parse(data)

    def display_weather(self, city):
        data = self.fetcher.fetch(city)
        if not data:
            print(f"Weather data not available for {city}")
        else:
            weather_report = self.parser.parse(data)
            print(weather_report)

    def main(self):
        while True:
            city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
            if city.lower() == 'exit':
                break
            detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
            if detailed == 'yes':
                forecast = self.get_detailed_forecast(city)
            else:
                forecast = self.display_weather(city)
            print(forecast)

if __name__ == "__main__":
    ui = UserInterface()
    ui.main()
