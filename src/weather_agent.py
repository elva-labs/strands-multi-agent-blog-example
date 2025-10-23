import random
from strands import Agent, tool

# Define a specialized system prompt
WEATHER_AGENT_PROMPT = """
You are a specialized weather assistant. You can provide current weather
information and forecasts for any location. Use the weather API tool to
fetch weather data and present it in a clear, user-friendly format.
"""


@tool
def get_weather_data(location: str, unit: str = "celsius") -> str:
    """
    Simulate an external API call to fetch weather data for a given location.

    This tool simulates calling a weather service API (like OpenWeatherMap)
    to retrieve current weather conditions.

    Args:
        location: The city or location name to get weather for (e.g., "London", "New York")
        unit: Temperature unit, either "celsius" or "fahrenheit" (default: "celsius")

    Returns:
        A JSON-formatted string containing simulated weather data
    """
    try:
        # Simulate API call delay and response
        # In a real implementation, this would be: requests.get(f"https://api.weather.com/data?location={location}")

        # Generate simulated weather data
        temperature = (
            random.randint(-10, 35) if unit == "celsius" else random.randint(14, 95)
        )
        conditions = random.choice(
            ["Sunny", "Cloudy", "Partly Cloudy", "Rainy", "Stormy", "Snowy"]
        )
        humidity = random.randint(30, 90)
        wind_speed = random.randint(5, 40)

        weather_data = {
            "location": location,
            "temperature": temperature,
            "unit": unit,
            "conditions": conditions,
            "humidity": humidity,
            "wind_speed": wind_speed,
            "wind_unit": "km/h",
        }

        # Return formatted string (simulating API JSON response)
        return str(weather_data)
    except Exception as e:
        return f"Error fetching weather data: {str(e)}"


@tool
def weather_assistant(query: str) -> str:
    """
    Process and respond to weather-related queries.

    This agent can answer questions about current weather conditions,
    forecasts, and provide weather information for specific locations.

    Args:
        query: A weather-related question (e.g., "What's the weather in Paris?")

    Returns:
        A detailed weather response with current conditions
    """
    try:
        weather_agent = Agent(
            system_prompt=WEATHER_AGENT_PROMPT,
            tools=[get_weather_data],
        )

        response = weather_agent(query)
        return str(response)
    except Exception as e:
        return f"Error in weather assistant: {str(e)}"


if __name__ == "__main__":
    result = weather_assistant("What's the weather like in London?")
    print(result)
