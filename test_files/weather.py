# Delacre a function called report_weather that takes a temperature and a function as its two arguments.
# Declare two other functions, each of which takes a temperature as an argument.
# Function 1 is called as_sun_lover and it should return 'great' if the temp is 25C or above.
# Function 2 is called as_snow_lover and it should return 'great' if the temp is 0C or below.
# Combine the functions to generate customised weather reports.

def as_sun_lover(temperature):
    if temperature >= 25:
        return "great"
    else:
        return "not great"

def as_snow_lover(temperature):
    if temperature <= 0:
        return "great"
    else:
        return "not great"

def report_weather(temperature, preference):
    return preference(temperature)


print(report_weather(25, as_sun_lover))