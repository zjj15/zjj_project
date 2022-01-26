from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'


temperature = poco(pos2 = [1120, 261]).get_attr('text')

lowerTemperature = int(temperature.split('～',1)[0])
temperatureUnit = temperature[-1:]
if  temperatureUnit == '℃' and lowerTemperature in range(-50,50):
    pass
else:
    error('wrong lower temperature display')
