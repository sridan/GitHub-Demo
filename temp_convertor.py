def celsius_to_kelvin(temp):
  return temp + 273.15  

temp = float(input('Enter the temperature in degrees celsius:'))
temp_kelvin = celsius_to_kelvin(temp)
print(f'Your Temperature in Kelvin is:{temp_kelvin}')
