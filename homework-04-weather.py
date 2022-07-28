# %% [markdown]
# # WeatherAPI (Weather)
#
# Answer the following questions using [WeatherAPI](http://www.weatherapi.com/). I've added three cells for most questions but you're free to use more or less! Hold `Shift` and hit `Enter` to run a cell, and use the `+` on the top left to add a new cell to a notebook.
#
# Be sure to take advantage of both the documentation and the API Explorer!
#
# ## 0) Import any libraries you might need
#
# - *Tip: We're going to be downloading things from the internet, so we probably need `requests`.*
# - *Tip: Remember you only need to import requests once!*

# %%
import requests

# %%
weather_api_key = "6e398a633db74946801165709221306"

# %% [markdown]
# ## 1) Make a request to the Weather API for where you were born (or lived, or want to visit!).
#
# - *Tip: The URL we used in class was for a place near San Francisco. What was the format of the endpoint that made this happen?*
# - *Tip: Save the URL as a separate variable, and be sure to not have `[` and `]` inside.*
# - *Tip: How is north vs. south and east vs. west latitude/longitude represented? Is it the normal North/South/East/West?*
# - *Tip: You know it's JSON, but Python doesn't! Make sure you aren't trying to deal with plain text.*
# - *Tip: Once you've imported the JSON into a variable, check the timezone's name to make sure it seems like it got the right part of the world!*

# %%
sf_url = "http://api.weatherapi.com/v1/current.json?key=6e398a633db74946801165709221306&q=94114&aqi=no"


# %%
sf_weather = requests.get(sf_url)
sf_weather = sf_weather.json()
sf_weather

# %% [markdown]
# ## 2) What's the current wind speed? How much warmer does it feel than it actually is?
#
# - *Tip: You can do this by browsing through the dictionaries, but it might be easier to read the documentation*
# - *Tip: For the second half: it **is** one temperature, and it **feels** a different temperature. Calculate the difference.*

# %%
# sf_weather['current'].keys()
sf_weather['current']['wind_mph']
sf_weather['current'].keys()


# %%
print(
    f"The current wind speed in San Francisco's Mission District is {sf_weather['current']['wind_mph']} mph.\nThe current temperature is {sf_weather['current']['temp_f']}°F, but it feels {round(sf_weather['current']['temp_f'] - sf_weather['current']['feelslike_f'], 1)} degrees colder than it actually is."
)

# %%


# %%


# %% [markdown]
# ## 3) What is the API endpoint for moon-related information? For the place you decided on above, how much of the moon will be visible tomorrow?
#
# - *Tip: Check the documentation!*
# - *Tip: If you aren't sure what something means, ask in Slack*

# %%
sf_astro_url = "http://api.weatherapi.com/v1/astronomy.json?key=6e398a633db74946801165709221306&q=94114&dt=2022-06-21"
sf_astro = requests.get(sf_astro_url)
sf_astro = sf_astro.json()
print(f"The endpoint for San Francisco moon info is {sf_astro_url}\nTomorrow, the moon will be {sf_astro['astronomy']['astro']['moon_illumination']}% visible.")

# %%


# %%


# %% [markdown]
# ## 4) What's the difference between the high and low temperatures for today?
#
# - *Tip: When you requested moon data, you probably overwrote your variables! If so, you'll need to make a new request.*

# %%
sf_forecast_url = "http://api.weatherapi.com/v1/forecast.json?key=6e398a633db74946801165709221306&q=94114&days=3&aqi=no&alerts=no"
sf_forecast = requests.get(sf_forecast_url)
sf_forecast = sf_forecast.json()


# %%
forecast_today = sf_forecast['forecast']['forecastday'][0]['day']
print(
    f"The difference between San Francisco's forecasted high and low temperatures on {sf_forecast['forecast']['forecastday'][0]['date']} is {round(forecast_today['maxtemp_f'] - forecast_today['mintemp_f'], 1)}°F."
)

# %% [markdown]
# ## 4.5) How can you avoid the "oh no I don't have the data any more because I made another request" problem in the future?
#
# What variable(s) do you have to rename, and what would you rename them?

# %%


# %%


# %% [markdown]
# ## 5) Go through the daily forecasts, printing out the next three days' worth of predictions.
#
# I'd like to know the **high temperature** for each day, and whether it's **hot, warm, or cold** (based on what temperatures you think are hot, warm or cold).
#
# - *Tip: You'll need to use an `if` statement to say whether it is hot, warm or cold.*

# %%
forecast_tomorrow = sf_forecast['forecast']['forecastday'][1]['day']
forecast_day_after = sf_forecast['forecast']['forecastday'][2]['day']
if forecast_tomorrow['maxtemp_f'] > 90:
    temp = "hot"
elif forecast_tomorrow['maxtemp_f'] > 70:
    temp = "warm"
else: temp = "cool"

if forecast_day_after['maxtemp_f'] > 90:
    next_temp = "hot"
elif forecast_day_after['maxtemp_f'] > 70:
    next_temp = "warm"
else: next_temp = "cool"

# %%
print(
    f"Tomorrow, the forecasted high will be {forecast_tomorrow['maxtemp_f']}°F, which I think is kind of {temp}.\nThe day after tomorrow, the forecasted high will be {forecast_day_after['maxtemp_f']}°F, which I think is kinda {next_temp}."
)

# %%


# %% [markdown]
# ## 5b) The question above used to be an entire week, but not any more. Try to re-use the code above to print out seven days.
#
# What happens? Can you figure out why it doesn't work?
#
# * *Tip: it has to do with the reason you're using an API key - maybe take a look at the "Air Quality Data" introduction for a hint? If you can't figure it out right now, no worries.*

# %%


# %%


# %%


# %% [markdown]
# ## 6) What will be the hottest day in the next three days? What is the high temperature on that day?

# %%
max_three = []
if forecast_today['maxtemp_f'] > forecast_tomorrow['maxtemp_f'] and forecast_day_after['maxtemp_f']:
    print(
        f"Today's forecasted high temperature, {forecast_today['maxtemp_f']}, is the highest of the next three days."
    )
elif forecast_tomorrow['maxtemp_f'] > forecast_today['maxtemp_f'] and forecast_day_after['maxtemp_f']:
    print(
        f"Tomorrow's forecasted high temperature, {forecast_tomorrow['maxtemp_f']}, is the highest of the next three days."
    )
elif forecast_day_after['maxtemp_f'] > forecast_today['maxtemp_f'] and forecast_tomorrow['maxtemp_f']:
    print(
        f"The day after tomorrow's forecasted high temperature, {forecast_tomorrow['maxtemp_f']}, is the highest of the next three days."
    )

# %%


# %%


# %% [markdown]
# ## 7) What's the weather looking like for the next 24+ hours in Miami, Florida?
#
# I'd like to know the temperature for every hour, and if it's going to have cloud cover of more than 50% say "{temperature} and cloudy" instead of just the temperature.
#
# - *Tip: You'll only need one day of forecast*

# %%
miami_24_url = "http://api.weatherapi.com/v1/forecast.json?key=6e398a633db74946801165709221306&q=miami, fl&days=1&aqi=no&alerts=no"
miami_24 = requests.get(miami_24_url)
miami_24 = miami_24.json()

for hour_counter, _ in enumerate(range(24)):
    miami_hour = miami_24['forecast']['forecastday'][0]['hour'][hour_counter]
    if miami_hour['cloud'] > 50:
        print(
            f"{miami_hour['time'][-5:]} — {miami_hour['temp_f']}°F and cloudy"
        )
    else:
        print(
            f"{miami_hour['time'][-5:]} — {miami_hour['temp_f']}°F."
        )
hot = []
for hour_counter, _ in enumerate(range(24)):
    miami_hour = miami_24['forecast']['forecastday'][0]['hour'][hour_counter]
    if miami_hour['temp_f'] > 80:
        hot.append(hour_counter)
# %%
print(
    f"For the next 24ish hours in miami, it will be above 85 degrees {round(float(len(hot) / 24 * 100))}% of the time."
)

# %%


# %% [markdown]
# ## 9) How much will it cost if you need to use 1,500,000 API calls?
#
# You are only allowed 1,000,000 API calls each month. If you were really bad at this homework or made some awful loops, WeatherAPI might shut down your free access.
#
# * *Tip: this involves looking somewhere that isn't the normal documentation.*

# %% [markdown]
# $4 per month.

# %%


# %% [markdown]
# ## 10) You're too poor to spend more money! What else could you do instead of give them money?
#
# * *Tip: I'm not endorsing being sneaky, but newsrooms and students are both generally poverty-stricken.*

# %% [markdown]
# Make a burner email account and sign up for another API!
