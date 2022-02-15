from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

temperature = poco(pos2 = [1420, 202]).get_attr('text')

highTemperature = int(temperature.split('～',1)[1][:-2])
temperatureUnit = temperature[-1:]
if  temperatureUnit == '℃' and highTemperature in range(-50,50):
    pass
else:
    error('wrong high temperature display')
